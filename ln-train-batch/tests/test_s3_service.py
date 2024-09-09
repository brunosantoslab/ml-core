import sys
import os
import unittest
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src directory to system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.infrastructure.services.s3_service import S3Service
from src.app.core.config import config 
from src.app.utils.file_utils import ensure_directory_exists  

class TestS3Service(unittest.TestCase):
    def setUp(self):
        self.s3_service = S3Service()
        self.test_file = os.path.join(config.INPUT_DATA_PATH, 'test_file.csv')
        self.s3_key = 'test/test_file.csv'

        # Ensure input and output directories exist
        ensure_directory_exists(config.INPUT_DATA_PATH)
        ensure_directory_exists(config.MODEL_OUTPUT_PATH)

        # Create a dummy file for testing
        with open(self.test_file, 'w') as f:
            f.write('feature1,feature2,target\n1.0,2.0,5.0\n2.0,3.0,7.0\n3.0,4.0,9.0')

    def test_upload_and_download_file(self):
        self.s3_service.upload_file(self.test_file, self.s3_key)

        downloaded_file = os.path.join(config.MODEL_OUTPUT_PATH, 'downloaded_test_file.csv')
        ensure_directory_exists(os.path.dirname(downloaded_file))
        self.s3_service.download_file(self.s3_key, downloaded_file)

        self.assertTrue(os.path.exists(downloaded_file))

        # Cleanup: remove the downloaded file after the test
        if os.path.exists(downloaded_file):
            os.remove(downloaded_file)

    def tearDown(self):
        # Cleanup: remove the test file after the test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == '__main__':
    unittest.main()
