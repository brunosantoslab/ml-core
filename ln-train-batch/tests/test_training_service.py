import sys
import os
import unittest
import numpy as np

# Add src directory to system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest.mock import MagicMock
from src.app.domain.services.training_service import TrainingService
from src.app.shared.value_objects.dataset import Dataset
from src.infrastructure.repositories.model_repository import ModelRepository
from src.app.utils.file_utils import ensure_directory_exists  # Reutilização do file_utils

class TestTrainingService(unittest.TestCase):
    def setUp(self):
        # Mock the model repository and create a dataset for testing
        self.model_repository = MagicMock(ModelRepository)
        self.training_service = TrainingService(self.model_repository)
        self.dataset = Dataset(
            features=np.array([[1.0, 2.0], [3.0, 4.0]]),
            target=np.array([5.0, 6.0])
        )

        # Ensure necessary directories exist
        ensure_directory_exists('/tmp')

    def test_train_model_success(self):
        """
        Test if the model is successfully trained and saved.
        """
        model = self.training_service.train_model(self.dataset)
        self.model_repository.save.assert_called_once_with(model)


if __name__ == '__main__':
    unittest.main()