public override string KeyVaultName => "studio-scus-MAML-1";

        public override Certificate StorageClientCertificate
        {
            get
            {
               return new KeyVaultCertificate("StorageClientCertificate") { SecretName = "studio-prod-scus-storage--storageclientcertificate/3f1db752ee8c41b596d4d8dd34573983", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate StorageServiceSSL
        {
            get
            {
               return new KeyVaultCertificate("StorageServiceSSL") { SecretName = "studio-prod-scus-storage--storageservicessl/73fcf7adb7564b3585ff2980f85bc50b", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate PIIPrimaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIIPrimaryCert") { SecretName = "studio-prod-scus-storage--StoragePIIPrimaryCert/8a051620946a48eda3e1e0ab8f4ff4c5", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate PIISecondaryCert
        {
            get
            {
               return new KeyVaultCertificate("PIISecondaryCert") { SecretName = "studio-prod-scus-storage--StoragePIIPrimaryCert/827a6a278a4f4c358f3bbf0a56396570", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate MdmCertificate
        {
            get
            {
               return new KeyVaultCertificate("MdmCertificate") { SecretName = "studio-prod--mdmcert/2b1b8417ac384d10ad08f609b52a5bba", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

        public override Certificate DecryptCert
        {
            get
            {
               return new KeyVaultCertificate("ServiceConfig") { SecretName = "studio-prod--serviceconfigcert-ar/69e4548409204adca3bfd305b24f8581", Owner = StudioProdStorageUSCentralEuapKeyVaultOwner };
            }
        }

        public override Certificate GCSCert
        {
            get
            {
               return new KeyVaultCertificate("GCSCertificate") { SecretName = "studio-prod--gcscert/485999a2e3a942d99e4484621598f579", Owner = StudioProdCommonKeyVaultOwner };
            }
        }

