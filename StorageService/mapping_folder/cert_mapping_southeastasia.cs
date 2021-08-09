public override string KeyVaultName => "studio-sea-MAML-1";

        public override Certificate StorageClientCertificate
        {
            get
            {
               return new KeyVaultCertificate("StorageClientCertificate") { SecretName = "studio-prod-sea-storage--storageclientcertificate/4ff8779b75e640ebbbb28f0f6200c8fb", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate StorageServiceSSL
        {
            get
            {
               return new KeyVaultCertificate("StorageServiceSSL") { SecretName = "studio-prod-sea-storage--storageservicessl/209be57d5ad24753943c63a675ae8f41", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate PIIPrimaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIIPrimaryCert") { SecretName = "studio-prod-sea-storage--StoragePIIPrimaryCert/380aa1ed421c4e2d878613065d78a7c0", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate PIISecondaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIISecondaryCert") { SecretName = "studio-prod-sea-storage--StoragePIIPrimaryCert/af4142b4bfb34f89b5db6c02efbf2d99", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate MdmCertificate
        {
            get
            {
               return new KeyVaultCertificate("MdmCertificate") { SecretName = "studio-prod--mdmcert/e442e306d324472182227d084674ee45", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate ServiceConfig
        {
            get
            {
               return new KeyVaultCertificate("ServiceConfig") { SecretName = "studio-prod--serviceconfigcert-ar/7978c0144dbc4781af1057e9db494534", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate GCSCertificate
        {
            get
            {
               return new KeyVaultCertificate("GCSCertificate") { SecretName = "studio-prod--gcscert/aa543c445c0d46d99e6619edd2384708", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

