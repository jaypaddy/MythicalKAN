# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import logging

import time

# create logger
logger = logging.getLogger()

class BlobOperator:
    """Class for Blob operations
    """

    def __init__(self, blob_connstring=None):
        """Initialize the class

        Args:
        """
        self.blob_connstring =  blob_connstring
        self.blob_service_client = None

    def connect_to_blob(self):
        """Connect to Blob

        Args:
        """
        try:
            blob_service_client = BlobServiceClient.from_connection_string(self.blob_connstring)
            print("[INFO] Connected to Azure Blob Storage on Edge using ConnString as blob:\t" + self.blob_connstring)
        except Exception as e:
            print("[ERROR] Unexpected error %s " % e )
            return False
        
        self.blob_service_client = blob_service_client
        return True

    def upload_file(self, srcfilename, tgtfilename, blobcontainername):
        try:
            blob_service_client = BlobServiceClient.from_connection_string(self.blob_connstring)
            logger.info("Uploading to Azure Blob Storage on Edge using ConnString as blob:\t" + tgtfilename)
            blob_client = blob_service_client.get_blob_client(container=blobcontainername, blob=tgtfilename) 
            with open(srcfilename, 'rb') as f:                       
                blob_client.upload_blob(f)            
            logger.info("DONE Uploading to Azure Blob Storage on Edge as blob:\t" + tgtfilename)

        except Exception as e:
            logger.info("Unexpected error %s " % e )

        return
