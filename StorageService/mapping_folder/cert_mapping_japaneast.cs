public override string KeyVaultName => "studio-jae-MAML-1";

        public override Certificate StorageClientCertificate
        {
            get
            {
               return new KeyVaultCertificate("StorageClientCertificate") { SecretName = "studio-prod-jae-storage--storageclientcertificate/ac4dcf7d51234425b95f86a945668f6a", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate StorageServiceSSL
        {
            get
            {
               return new KeyVaultCertificate("StorageServiceSSL") { SecretName = "studio-prod-jae-storage--storageservicessl/36db88f1ad1e4ed68ba27de935bebece", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate PIIPrimaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIIPrimaryCert") { SecretName = "studio-prod-jae-storage--StoragePIIPrimaryCert/3b2bad93289e4e2797a44624d25547fe", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate PIISecondaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIISecondaryCert") { SecretName = "studio-prod-jae-storage--StoragePIIPrimaryCert/345c1bce5e3348b2b199d442782a6266", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate MdmCertificate
        {
            get
            {
               return new KeyVaultCertificate("MdmCertificate") { SecretName = "studio-prod--mdmcert/0e02b7e00bc4472c97c4b882b644862e", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate DecryptCert
        {
            get
            {
               return new KeyVaultCertificate("ServiceConfig") { SecretName = "studio-prod--serviceconfigcert-ar/58210ca8c08443a5b3d5bfacee831de4", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate GCSCert
        {
            get
            {
               return new KeyVaultCertificate("GCSCertificate") { SecretName = "studio-prod--gcscert/48aa2c487981495ab5340bf9b12b32a9", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

