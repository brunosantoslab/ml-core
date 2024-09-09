import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration class for loading environment variables.
    Contains paths, AWS credentials, SQS queue, and log level configuration.
    """
    def __init__(self):
        self.AWS_REGION = os.getenv('AWS_REGION')
        self.S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
        self.INPUT_DATA_PATH = os.getenv('LOCAL_DATA_PATH')
        self.MODEL_OUTPUT_PATH = os.getenv('MODEL_OUTPUT_PATH')
        self.LOG_LEVEL = os.getenv('LOG_LEVEL')

config = Config()
