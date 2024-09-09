from infrastructure.persistence.file_dao import FileDAO

class ModelRepository:
    """
    Repository responsible for persisting and retrieving the trained model.
    """

    def __init__(self, dao: FileDAO):
        self.dao = dao

    def save(self, model, file_path: str):
        """
        Saves the model using the DAO.
        
        Args:
            model: Trained model instance.
            file_path (str): Path to save the model.
        """
        self.dao.save(file_path, model)

    def load(self, file_path: str):
        """
        Loads the model using the DAO.
        
        Args:
            file_path (str): Path to load the model.
        
        Returns:
            Loaded model.
        """
        return self.dao.load(file_path)