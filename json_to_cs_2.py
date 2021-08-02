import glob
import json

FOLDER_NAME = "StorageService"


def format_to_cs(file):
    with open(file, 'r') as f:
        mapping = json.load(f)

    cs_file_name = file[:-5] + '.txt'
    with open(cs_file_name, 'w') as f:
        kv_info = mapping[0].get('destUrl')
        kv = kv_info.split('.')[0][len('https://'):]
        f.write('public override string KeyVaultName => "{0}";\n\n'.format(kv))
        for map in mapping:
            name = map.get('name')
            destUrl = map.get('destUrl').split('/')
            value = destUrl[-2] + '/' + destUrl[-1]
            cs_format = \
                f'        public override Certificate {name}\n' \
                '         {\n' \
                '            get\n' \
                '            {\n' \
                f'               return new KeyVaultCertificate("{name}") {{ SecretName = "{value}", Owner = StudioProdCommonKeyVaultOwner }};\n' \
                '            }\n' \
                '         }\n\n'

            f.write(cs_format)


def _get_files():
    file_name_format = rf'{FOLDER_NAME}\mapping_folder\*.json'
    files = glob.glob(file_name_format)
    print("All files:", files)
    return files


if __name__ == '__main__':
    files = _get_files()
    for file in files:
        format_to_cs(file)
