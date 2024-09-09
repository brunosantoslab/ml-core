import os
import pickle
from app.utils.file_utils import ensure_directory_exists

class FileDAO:
    """
    DAO responsible for file operations like saving, loading, and deleting files.
    """

    def save(self, file_path: str, data):
        """
        Saves data to a file.
        
        Args:
            file_path (str): The path to save the file.
            data: The data to be saved.
        """
        ensure_directory_exists(os.path.dirname(file_path))
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)

    def load(self, file_path: str):
        """
        Loads data from a file.
        
        Args:
            file_path (str): The path of the file to load.
        
        Returns:
            Loaded data.
        """
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    def delete(self, file_path: str):
        """
        Deletes a file if it exists.
        
        Args:
            file_path (str): The path of the file to delete.
        """
        if os.path.exists(file_path):
            os.remove(file_path)