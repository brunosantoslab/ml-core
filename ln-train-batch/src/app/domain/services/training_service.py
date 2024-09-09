from app.domain.models.linear_regression_model import LinearRegressionModel
from app.shared.value_objects.dataset import Dataset
from infrastructure.repositories.model_repository import ModelRepository
from app.core.logging_config import logger
from app.utils.file_utils import ensure_directory_exists

class TrainingService:
    """
    Service responsible for training the linear regression model.
    """

    def __init__(self, model_repository: ModelRepository):
        self.model_repository = model_repository

    def train_model(self, dataset: Dataset):
        """
        Train the linear regression model using the provided dataset.

        Args:
            dataset (Dataset): The dataset containing features and target for training.

        Returns:
            LinearRegressionModel: The trained model.
        """
        # Create and train the model
        model = LinearRegressionModel()
        model.train(dataset.features, dataset.target)

        # Save the trained model using the model repository
        self.model_repository.save(model)
        
        logger.info("Model trained and saved successfully.")
        return model