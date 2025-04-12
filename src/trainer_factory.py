# trainer_factory.py
from model_trainer import RandomForestTrainer


class TrainerFactory:
    """
    Trainer factory that instantiates the appropriate model
    based on the requested type.

    Currently supports only Random Forest, but can be extended
    to include other types such as XGBoost, LightGBM, etc.
    """

    @staticmethod
    def create_trainer(model_type: str, X_train, X_test, y_train, y_test):
        """
        Creates and returns an instance of the trainer corresponding to the specified model type.

        Args:
            model_type (str): Name of the desired model (e.g., "random_forest").
            X_train (DataFrame): Training features.
            X_test (DataFrame): Testing features.
            y_train (Series): Training target.
            y_test (Series): Testing target.

        Returns:
            A trainer object with training and saving interface.

        Raises:
            ValueError: If the model type is not supported.
        """
        if model_type.lower() == 'random_forest':
            return RandomForestTrainer(X_train, X_test, y_train, y_test)
        # Other trainers can be added here (e.g., XGBoostTrainer, LGBMTrainer, etc.)
        raise ValueError(f"Modelo do tipo '{model_type}' não suportado.")
