public override string KeyVaultName => "studio-wcus-MAML-1";

        public override Certificate StorageClientCertificate
        {
            get
            {
               return new KeyVaultCertificate("StorageClientCertificate") { SecretName = "studio-prod-uswc-storage--storageclientcertificate/4a46fd16c88c434486584a721faf37a8", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate StorageServiceSSL
        {
            get
            {
               return new KeyVaultCertificate("StorageServiceSSL") { SecretName = "studio-prod-uswc-storage--storageservicessl/a5afed9d7d1b4221b4e6e4450d42b89f", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate PIIPrimaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIIPrimaryCert") { SecretName = "studio-prod-uswc-storage--StoragePIIPrimaryCert/a8d77a516cf24da9a7775d2e9dd4da66", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate PIISecondaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIISecondaryCert") { SecretName = "studio-prod-uswc-storage--StoragePIIPrimaryCert/53171327d2d14e6abb4cb94eae4d3cb4", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate MdmCertificate
        {
            get
            {
               return new KeyVaultCertificate("MdmCertificate") { SecretName = "studio-prod--mdmcert/8267ccc540b344b3995c843e2b4edc5c", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate DecryptCert
        {
            get
            {
               return new KeyVaultCertificate("ServiceConfig") { SecretName = "studio-prod--serviceconfigcert-ar/3af441b165bd4edcba9ea21109f93936", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate GCSCert
        {
            get
            {
               return new KeyVaultCertificate("GCSCertificate") { SecretName = "studio-prod--gcscert/5c0a4afd29f842b2ad143504e566246a", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

