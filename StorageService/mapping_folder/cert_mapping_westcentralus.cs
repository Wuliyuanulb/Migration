public override string KeyVaultName => "studio-wcus-MAML-1";

        public override Certificate StorageClientCertificate
        {
            get
            {
               return new KeyVaultCertificate("StorageClientCertificate") { SecretName = "studio-prod-uswc-storage--storageclientcertificate/487e82acc6af4a86bebc552e8bd7c72e", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate StorageServiceSSL
        {
            get
            {
               return new KeyVaultCertificate("StorageServiceSSL") { SecretName = "studio-prod-uswc-storage--storageservicessl/ba67d4c80ca84d09bc60be2d32b9f506", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate PIIPrimaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIIPrimaryCert") { SecretName = "studio-prod-uswc-storage--StoragePIIPrimaryCert/f8e61288e82a4165b8722c9d6e23e675", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate PIISecondaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIISecondaryCert") { SecretName = "studio-prod-uswc-storage--StoragePIIPrimaryCert/53171327d2d14e6abb4cb94eae4d3cb4", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate MdmCertificate
        {
            get
            {
               return new KeyVaultCertificate("MdmCertificate") { SecretName = "studio-prod--mdmcert/8267ccc540b344b3995c843e2b4edc5c", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate ServiceConfig
        {
            get
            {
               return new KeyVaultCertificate("ServiceConfig") { SecretName = "studio-prod--serviceconfigcert-ar/3af441b165bd4edcba9ea21109f93936", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate GCSCertificate
        {
            get
            {
               return new KeyVaultCertificate("GCSCertificate") { SecretName = "studio-prod--gcscert/5c0a4afd29f842b2ad143504e566246a", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

