""" Migrate Certs from source key vault to destination key vault.
   input parameter json = > cert url => key vault and cert name/version => get cert and import to dest cert """


import re
import base64
import json
import glob
import subprocess
import os

from azure.identity import AzureCliCredential
from azure.keyvault.certificates import CertificateClient
from azure.keyvault.secrets import SecretClient
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.common.credentials import get_azure_cli_credentials
from azure.core.exceptions import ResourceNotFoundError

# TODO: The following parameters need to be updated by region/service.
FOLDER_NAME = "officeapps"
SUB_SERIES = "MAML-4-comm"
# change FILE_NAME_FORMAT according to parameter files under one service folder
FILE_NAME_FORMAT = "{}/*1_*_Parameters.json".format(FOLDER_NAME, FOLDER_NAME)
# Object id of your own microsoft account.
OBJECT_ID = "8f919de4-02b0-48de-ba4c-a13be2e19c33"
DEST_RESOURCE_GROUP_NAME = "studio-migration"
#############################################################################################

global DEST_LOCATION
MAPPING_FOLDER = 'mapping_folder'
if not os.path.exists(rf'{FOLDER_NAME}\{MAPPING_FOLDER}'):
    os.mkdir(rf'{FOLDER_NAME}\{MAPPING_FOLDER}')

LOCATION_TO_SUB_IDs = {
    "centraluseuap": {
        "MAML-1": "1220ed94-c61b-4690-b5c6-acc242a69250",
        "MAML-2": "8402e523-a30f-4d05-917e-fb5a74b3ff5a",
    },
    "westcentralus": {
        "MAML-1": "c1f017cf-6887-4b7b-901b-efd8647d04c6",
        "MAML-2": "4ee2639f-70ee-4e6f-99f6-b4361dbe4ce1",
    },
    "westeurope": {
        "MAML-1": "db252142-caa2-4ea2-83cb-04677720fe1f",
        "MAML-2": "cdb0a04a-e5cd-4cfa-8dcf-fd5678880640",
    },
    "southcentralus": {
        "MAML-1": "a0e9f47a-2fbb-4dca-8071-169298ff7f6a",
        "MAML-2": "3a4d3ed0-61ec-41ab-956b-91f3168c1e0f",
    },
    "southeastasia": {
        "MAML-1": "6c54c4ca-e743-45a6-ba22-c4ecff8c06d1",
        "MAML-2": "212b350a-9910-41d7-906d-4689ed4977db",
    },
    "japaneast": {
        "MAML-1": "697346b9-61f2-4685-9c98-5703480f5370",
        "MAML-2": "d56631dc-e554-4a36-8096-ab25a16cb612",
    },
    "eastus2": {
        "MAML-2": "3a70124c-988d-4a70-ae83-ddc4c203da75"
    }
}
LOCATION_TO_SUB_IDs['uscentraleuap'] = LOCATION_TO_SUB_IDs['centraluseuap']
LOCATION_TO_SUB_IDs['uswestcentral'] = LOCATION_TO_SUB_IDs['westcentralus']
LOCATION_TO_SUB_IDs['europewest'] = LOCATION_TO_SUB_IDs['westeurope']
LOCATION_TO_SUB_IDs['ussouthcentral'] = LOCATION_TO_SUB_IDs['southcentralus']
LOCATION_TO_SUB_IDs['asiasoutheast'] = LOCATION_TO_SUB_IDs['southeastasia']
LOCATION_TO_SUB_IDs['useast2'] = LOCATION_TO_SUB_IDs['eastus2']

MAML_Production_4_Community_ID = "6c868b6a-900a-4b5d-8c03-2d5506291b33"
MAML_Production_13_Web_Service_Management_UX_ID = "4d3bdb9c-a8d4-4a75-9ce4-cd4244c00d64"
LOCATION_SHORT_NAME = {
    "centraluseuap": "usce",
    "uscentraleuap": "usce",
    "westcentralus": "wcus",
    "uswestcentral": "wcus",
    "westeurope": "weu",
    "europewest": "weu",
    "southcentralus": "scus",
    "ussouthcentral": "scus",
    "southeastasia": "sea",
    "asiasoutheast": "sea",
    "japaneast": "jae",
    "eastus2": "eus2",
    "useast2": "eus2",
    "eastus": "eus",
    "eastasia": "ea",
    "asiaeast": "ea",
    "northeurope": "neu",
    "westus": "wus",
    "uswest": "wus"
}
SUB_SERIES_WHITE_LIST = ["MAML-1", "MAML-2", "MAML-4-comm", "MAML-13-UX"]
TENANT_ID = "72f988bf-86f1-41af-91ab-2d7cd011db47"
# Application used for ev2 deployment in release pipeline.
DEPLOYMENT_APP_OBJECT_ID = "cbdda706-d154-4831-85c5-58f6a3765b3f"

# TODO: change parse policy to automatically get location fro file name
def _get_location_from_file_name(file):
    # NOTE: need to change here
    location = file.split("-")[2]
    return location


def get_subscription_id(location: str, sub_series: str) -> str:
    if sub_series not in SUB_SERIES_WHITE_LIST:
        raise ValueError(f"Parameter sub_series must be one of {SUB_SERIES_WHITE_LIST}. Got {sub_series}")

    if sub_series in ["MAML-1", "MAML-2"]:
        sub_id = LOCATION_TO_SUB_IDs.get(location).get(sub_series)
        if not sub_id:
            raise Exception(f"Subscription not found for location {location} and sub_series {sub_series}")
        return sub_id

    elif sub_series == "MAML-4-comm":
        return MAML_Production_4_Community_ID

    elif sub_series == "MAML-13-UX":
        return MAML_Production_13_Web_Service_Management_UX_ID


def get_dest_vault_name(location: str, sub_series: str) -> str:
    if sub_series not in SUB_SERIES_WHITE_LIST:
        raise ValueError(f"Parameter sub_series must be one of {SUB_SERIES_WHITE_LIST}. Got {sub_series}")

    location_short_name = LOCATION_SHORT_NAME.get(location)
    if not location_short_name:
        raise ValueError(f"Location short name not found for location {location}")

    return f"studio-{location_short_name}-{sub_series}"


def _create_dest_key_vault():
    """Create destination key vault. If exists, do nothing."""
    credential, _ = get_azure_cli_credentials()
    # Create or update resource group.
    client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
    try:
        client.resource_groups.get(DEST_RESOURCE_GROUP_NAME)
    except:
        print(f"Creating resource group {DEST_RESOURCE_GROUP_NAME} "
              f"in location {DEST_LOCATION} in sub {SUBSCRIPTION_ID}")
        client.resource_groups.create_or_update(DEST_RESOURCE_GROUP_NAME, {'location': DEST_LOCATION})

    # Create or update destination key vault.
    client = KeyVaultManagementClient(credential, SUBSCRIPTION_ID)
    try:
        client.vaults.get(DEST_RESOURCE_GROUP_NAME, DEST_VAULT_NAME)
    except:
        print(f"Creating key vault {DEST_VAULT_NAME} in resource group {DEST_RESOURCE_GROUP_NAME} "
              f"in location {DEST_LOCATION} in sub {SUBSCRIPTION_ID}")
        operation = client.vaults.create_or_update(
            DEST_RESOURCE_GROUP_NAME,
            DEST_VAULT_NAME,
            {
                'location': DEST_LOCATION,
                'properties': {
                    'sku': {
                        'name': 'standard'
                    },
                    'tenant_id': TENANT_ID,
                    'access_policies': [
                        {
                            'object_id': OBJECT_ID,
                            'tenant_id': TENANT_ID,
                            'permissions': {
                                'certificates': ['all'],
                                'secrets': ['all']
                            }
                        },
                        {
                            'object_id': DEPLOYMENT_APP_OBJECT_ID,
                            'tenant_id': TENANT_ID,
                            'permissions': {
                                'certificates': ['all'],
                                'secrets': ['all']
                            }
                        }
                    ],
                    "enabledForDeployment": True
                }
            }
        )
        return operation.result()
    return client.vaults.get(DEST_RESOURCE_GROUP_NAME, DEST_VAULT_NAME)


def _get_certificate_section(complete_json_str: str) -> list:
    """Get certificate section from the input parameter json file."""
    start_target = '"Certificates": '
    start_index = complete_json_str.find(start_target) + len(start_target)
    end_index = complete_json_str.find(']', start_index) + 1  # +1 to include the ] string.
    cert_str = complete_json_str[start_index: end_index]

    try:
        return json.loads(cert_str)
    # Possibly caused because of the comma after the last element
    except json.decoder.JSONDecodeError:
        # Remove the last comma
        cert_str = cert_str[::-1].replace(",", "", 1)[::-1]
        return json.loads(cert_str)


def _create_certificate_client(vault_url: str) -> CertificateClient:
    """Create and cache certificate client."""
    if cert_client_cache_dict.get(vault_url) is not None:
        return cert_client_cache_dict.get(vault_url)

    credential = AzureCliCredential()
    certificate_client = CertificateClient(vault_url=vault_url, credential=credential)
    cert_client_cache_dict.update({vault_url: certificate_client})
    return certificate_client


def _create_secret_client(vault_url: str) -> SecretClient:
    """Create and cache secret client."""
    if secret_client_cache_dict.get(vault_url) is not None:
        return secret_client_cache_dict.get(vault_url)

    credential = AzureCliCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    secret_client_cache_dict.update({vault_url: client})
    return client


def _parse_vault_url(url: str) -> (str, str, str):
    """Get base vault url, cert name and cert version from cert url."""
    vault_url_pattern = "^(.+?)(:443|/secrets)"
    cert_name_version_pattern = "/secrets/(.*)"
    try:
        vault_url = re.search(vault_url_pattern, url).group(1)
        cert_name_version = re.search(cert_name_version_pattern, url).group(1)
        cert_name_version = cert_name_version.split("/")
        if len(cert_name_version) == 2:
            return vault_url, cert_name_version[0], cert_name_version[1]

        else:
            return vault_url, cert_name_version[0], None

    except:
        raise ValueError(f"Failed to parse url: {url}")


def _parse_vault_name(vault_url: str) -> str:
    p = "https://(.*).vault"
    return re.search(p, vault_url).group(1)


def _get_cert_section_from_input_file(file_path: str) -> dict:
    with open(file_path, "r") as f:
        d = f.read()
    return _get_certificate_section(d)


def _get_thumbprint(vault_base_url: str, cert_name: str, cert_version: str) -> bytes:
    """Get x509 thumbrprint."""
    client = _create_certificate_client(vault_base_url)
    if cert_version:
        cert = client.get_certificate_version(certificate_name=cert_name, version=cert_version)
    else:
        cert = client.get_certificate(certificate_name=cert_name)
    return cert.properties.x509_thumbprint


def _check_if_certificate_in_secrets_section(vault_base_url: str, cert_name: str, cert_version: str) -> bool:
    """Check if the certificate is stored in key vault's secret section."""
    cert_client = _create_certificate_client(vault_base_url)
    try:
        if cert_version:
            cert_client.get_certificate_version(certificate_name=cert_name, version=cert_version)
        else:
            cert_client.get_certificate(certificate_name=cert_name)
    except ResourceNotFoundError:
        secret_client = _create_secret_client(vault_base_url)
        versions = secret_client.list_properties_of_secret_versions(name=cert_name)
        if any(cert_version in v.version for v in versions):
            return True
    return False


def _check_if_certificate_has_imported(source_vault_url, source_cert_name, source_cert_version, dest_cert_name) -> bool:
    """Check if the certificate has already been imported into destination key vault."""
    dest_cert_client = _create_certificate_client(DEST_VAULT_URL)
    cert_versions = dest_cert_client.list_properties_of_certificate_versions(certificate_name=dest_cert_name)

    if cert_versions:
        source_cert_thumbprint = _get_thumbprint(source_vault_url, source_cert_name, source_cert_version)
        for cv in cert_versions:
            if cv.x509_thumbprint == source_cert_thumbprint:
                return True
    return False


def _get_certificate_version_in_dest_key_vault(
        source_vault_url, source_cert_name, source_cert_version, dest_cert_name) -> str:
    """Get cert version in destination key vault."""
    dest_cert_client = _create_certificate_client(DEST_VAULT_URL)
    cert_versions = dest_cert_client.list_properties_of_certificate_versions(certificate_name=dest_cert_name)
    if cert_versions:
        source_cert_thumbprint = _get_thumbprint(source_vault_url, source_cert_name, source_cert_version)
        for cv in cert_versions:
            if cv.x509_thumbprint == source_cert_thumbprint:
                return cv.version
    raise Exception(f"Failed to find certificate {source_cert_name} in key vault {DEST_VAULT_NAME}")


def _get_files():
    file_name_format = FILE_NAME_FORMAT
    files = glob.glob(file_name_format)
    print("All parameter files:", files)
    return files


def _assign_kv_policy():
    # assign kv access policy
    secret_permissions = "get list set delete backup restore recover"
    certificate_permissions = "get list delete create import update managecontacts getissuers listissuers setissuers " \
                              "deleteissuers manageissuers recover backup restore"
    command = "az keyvault set-policy " \
              "--name {} " \
              "--secret-permissions {} " \
              "--certificate-permissions {} " \
              "--subscription {} " \
              "--object-id {}"\
        .format(DEST_VAULT_NAME, secret_permissions, certificate_permissions, SUBSCRIPTION_ID, OBJECT_ID)
    try:
        subprocess.check_call(command, shell=True)
        print(f'Addded your access to Key Vault {DEST_VAULT_NAME}')
    except Exception as e:
        raise Exception(f"Adding access failed: {e}")


def source_dest_url_mapping(input_parameter_json):
    source_dest_url_mapping = []
    cert_section = _get_cert_section_from_input_file(input_parameter_json)

    for c in cert_section:
        mapping_dict = {
            "name": c["Name"],
            "sourceUrl": c["ContentReference"],
        }

        cert_url = c["ContentReference"]
        print(f"Retrieving cert from {cert_url}...")

        source_vault_url, source_cert_name, source_cert_version = _parse_vault_url(cert_url)

        source_secret_client = _create_secret_client(source_vault_url)
        source_cert = source_secret_client.get_secret(name=source_cert_name, version=source_cert_version)

        # Put source vault name into the cert name in destination vault.
        # This helps cert rotation.
        source_vault_name = _parse_vault_name(source_vault_url)
        dest_cert_name = source_vault_name + "--" + source_cert_name

        if _check_if_certificate_in_secrets_section(source_vault_url, source_cert_name, source_cert_version):
            print(f"Cert name {source_cert_name} and version {source_cert_version} is stored in key vault "
                  f"{source_vault_url} as a secret. Need to import manually.")

            mapping_dict.update({"destUrl": "Cert is in key vaults's secret section. Import manually."})
            source_dest_url_mapping.append(mapping_dict)
            continue

        if _check_if_certificate_has_imported(source_vault_url, source_cert_name, source_cert_version, dest_cert_name):
            print(f"Skip import. Cert name {source_cert_name} and version {source_cert_version} has already been "
                  f"imported into key vault {DEST_VAULT_NAME}.")
        else:
            print(f"Importing cert name {source_cert_name} and version {source_cert_version} into key vault "
                  f"{DEST_VAULT_NAME}...")
            dest_cert_client = _create_certificate_client(DEST_VAULT_URL)
            dest_cert_client.import_certificate(certificate_name=dest_cert_name,
                                                certificate_bytes=base64.b64decode(source_cert.value))

        # Get the cert url of imported cert.
        dest_cert_version = _get_certificate_version_in_dest_key_vault(
            source_vault_url, source_cert_name, source_cert_version, dest_cert_name)
        dest_cert_url = DEST_VAULT_URL + ":443/secrets/" + dest_cert_name + "/" + dest_cert_version

        # Update the mapping dict.
        mapping_dict.update({"destUrl": dest_cert_url})
        source_dest_url_mapping.append(mapping_dict)

    with open(OUTPUT_CERT_MAPPING_JSON, "w") as f:
        print(f"Writing mapping json into file {OUTPUT_CERT_MAPPING_JSON}...")
        json.dump(source_dest_url_mapping, f, indent=4)


if __name__ == "__main__":
    files = _get_files()
    for file in files:
        DEST_LOCATION = _get_location_from_file_name(file)
        print("DEST_LOCATION:", DEST_LOCATION)
        DEST_VAULT_NAME = get_dest_vault_name(DEST_LOCATION, SUB_SERIES)
        DEST_VAULT_URL = f"https://{DEST_VAULT_NAME}.vault.azure.net"
        OUTPUT_CERT_MAPPING_JSON = rf".\{FOLDER_NAME}\{MAPPING_FOLDER}\cert_mapping_{DEST_LOCATION}.json"
        secret_client_cache_dict = {}
        cert_client_cache_dict = {}
        SUBSCRIPTION_ID = get_subscription_id(DEST_LOCATION, SUB_SERIES)
        _assign_kv_policy()
        source_dest_url_mapping(file)
