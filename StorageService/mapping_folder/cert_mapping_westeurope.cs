public override string KeyVaultName => "studio-weu-MAML-1";

        public override Certificate StorageClientCertificate
        {
            get
            {
               return new KeyVaultCertificate("StorageClientCertificate") { SecretName = "studio-prod-weu-storage--storageclientcertificate/c793ed7116af4ce0bd9e42f5224cdfd6", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate StorageServiceSSL
        {
            get
            {
               return new KeyVaultCertificate("StorageServiceSSL") { SecretName = "studio-prod-weu-storage--storageservicessl/5d9e5ab4a319496dbaac1d37a61ce57c", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate PIIPrimaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIIPrimaryCert") { SecretName = "studio-prod-weu-storage--StoragePIIPrimaryCert/ab74b2b7b7934a2faaa2a32c8a7411d9", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate PIISecondaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIISecondaryCert") { SecretName = "studio-prod-weu-storage--StoragePIIPrimaryCert/1eadf0e88f3c4f928a9f58de2a19b3e4", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate MdmCertificate
        {
            get
            {
               return new KeyVaultCertificate("MdmCertificate") { SecretName = "studio-prod--mdmcert/c15025f4788242f6baa1a34c2a74bb97", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate ServiceConfig
        {
            get
            {
               return new KeyVaultCertificate("ServiceConfig") { SecretName = "studio-prod--serviceconfigcert-ar/5a038a02c27f4e65afb74abda3d6a299", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate GCSCertificate
        {
            get
            {
               return new KeyVaultCertificate("GCSCertificate") { SecretName = "studio-prod--gcscert/66f9bd7f61b34b33a1eac3c9cc471220", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

