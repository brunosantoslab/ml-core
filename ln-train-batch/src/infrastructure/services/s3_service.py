import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from app.core.config import config
from app.core.logging_config import logger
from infrastructure.services.cloud_storage_service import CloudStorageService
from app.utils.file_utils import ensure_directory_exists

class S3Service(CloudStorageService):
    """
    Service responsible for interacting with S3 for file uploads and downloads.
    """

    def __init__(self):
        self.s3_client = boto3.client('s3', region_name=config.AWS_REGION)

    def download_file(self, storage_key: str, local_path: str):
        """
        Downloads a file from S3.
        
        Args:
            storage_key (str): S3 key for the file.
            local_path (str): Local path to save the file.
        """
        try:
            self.s3_client.download_file(config.S3_BUCKET_NAME, storage_key, local_path)
            logger.info(f"Downloaded {storage_key} to {local_path}")
        except (NoCredentialsError, PartialCredentialsError) as e:
            logger.error(f"Failed to download {storage_key} from S3: {e}")

    def upload_file(self, local_path: str, storage_key: str):
        """
        Uploads a file to S3.
        
        Args:
            local_path (str): Local path of the file.
            storage_key (str): S3 key to upload the file.
        """
        try:
            ensure_directory_exists(os.path.dirname(local_path))
            self.s3_client.upload_file(local_path, config.S3_BUCKET_NAME, storage_key)
            logger.info(f"Uploaded {local_path} to {storage_key}")
        except (NoCredentialsError, PartialCredentialsError) as e:
            logger.error(f"Failed to upload {local_path} to S3: {e}")
