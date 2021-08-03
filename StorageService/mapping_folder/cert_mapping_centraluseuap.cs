public override string KeyVaultName => "studio-usce-MAML-2";

        public override Certificate StorageClientCertificate
        {
            get
            {
               return new KeyVaultCertificate("StorageClientCertificate") { SecretName = "studio-prod-usce-storage--storageclientcertificate/3f351a8fba4e439689712a947aa6d488", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate StorageServiceSSL
        {
            get
            {
               return new KeyVaultCertificate("StorageServiceSSL") { SecretName = "studio-prod-usce-storage--storageservicessl/91c8b7b6f679489ba76f93b8bd6a3825", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate PIIPrimaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIIPrimaryCert") { SecretName = "studio-prod-usce-storage--StoragePIIPrimaryCert/6d14f6ddc25545ea9e65df073ad58d8c", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate PIISecondaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIISecondaryCert") { SecretName = "studio-prod-usce-storage--StoragePIIPrimaryCert/91e260c1852c496ca3602322aa863bae", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate MdmCertificate
        {
            get
            {
               return new KeyVaultCertificate("MdmCertificate") { SecretName = "studio-prod--mdmcert/03372a70f78c4bfdb11473244a5b99d2", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate ServiceConfig
        {
            get
            {
               return new KeyVaultCertificate("ServiceConfig") { SecretName = "studio-prod--serviceconfigcert-ar/fc792085c10b42e5a14103ae25f23296", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate GCSCertificate
        {
            get
            {
               return new KeyVaultCertificate("GCSCertificate") { SecretName = "studio-prod--gcscert/d7ae7bfff7154c538a2a6863926ca895", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

