from abc import ABC, abstractmethod

class CloudStorageService(ABC):
    """
    Abstract interface for cloud storage services.
    """

    @abstractmethod
    def download_file(self, storage_key: str, local_path: str):
        """
        Downloads a file from the cloud storage.

        Args:
            storage_key (str): The storage key for the file.
            local_path (str): Local path to save the file.
        """
        pass

    @abstractmethod
    def upload_file(self, local_path: str, storage_key: str):
        """
        Uploads a file to the cloud storage.

        Args:
            local_path (str): Local path of the file.
            storage_key (str): Storage key to upload the file.
        """
        pass
