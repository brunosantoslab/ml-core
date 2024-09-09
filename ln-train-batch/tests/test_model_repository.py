import sys
import os
import unittest
from unittest.mock import MagicMock

# Add src directory to system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.infrastructure.repositories.model_repository import ModelRepository
from src.infrastructure.persistence.file_dao import FileDAO
from src.app.utils.file_utils import ensure_directory_exists  # Reutilização do file_utils


class TestModelRepository(unittest.TestCase):
    def setUp(self):
        # Mock the FileDAO and initialize the ModelRepository with it
        self.dao = MagicMock(FileDAO)
        self.model_repository = ModelRepository(self.dao)

        # Ensure necessary directories exist
        ensure_directory_exists('/tmp')

    def test_save_model(self):
        """
        Test if the model is saved correctly.
        """
        model = MagicMock()  # Mock the trained model
        file_path = os.path.join('/tmp', 'mock-model.pkl')
        self.model_repository.save(model, file_path)
        self.dao.save.assert_called_once_with(file_path, model)

    def test_load_model(self):
        """
        Test if the model is loaded correctly.
        """
        file_path = os.path.join('/tmp', 'mock-model.pkl')
        self.model_repository.load(file_path)
        self.dao.load.assert_called_once_with(file_path)


if __name__ == '__main__':
    unittest.main()