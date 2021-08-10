public override string KeyVaultName => "studio-usce-MAML-1";

        public override Certificate StorageClientCertificate
        {
            get
            {
               return new KeyVaultCertificate("StorageClientCertificate") { SecretName = "studio-prod-usce-storage--storageclientcertificate/049efb17264040cb935e1ae2b8939a9f", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate StorageServiceSSL
        {
            get
            {
               return new KeyVaultCertificate("StorageServiceSSL") { SecretName = "studio-prod-usce-storage--storageservicessl/96a300cccf09461dbd257c6c9a7575b1", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate PIIPrimaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIIPrimaryCert") { SecretName = "studio-prod-usce-storage--StoragePIIPrimaryCert/3ce3484916c547f296ec75e566d800a0", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate PIISecondaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIISecondaryCert") { SecretName = "studio-prod-usce-storage--StoragePIIPrimaryCert/0d71000fb7654ceebe18536a06a6babe", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate MdmCertificate
        {
            get
            {
               return new KeyVaultCertificate("MdmCertificate") { SecretName = "studio-prod--mdmcert/7c5db7d2f9994eca8e883ef352ff0410", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate DecryptCert
        {
            get
            {
               return new KeyVaultCertificate("ServiceConfig") { SecretName = "studio-prod--serviceconfigcert-ar/8ed4e2e8fab04df49b14b279dfc499a3", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate GCSCert
        {
            get
            {
               return new KeyVaultCertificate("GCSCertificate") { SecretName = "studio-prod--gcscert/e089af93f0ab4e3da467e75927ff6be8", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

