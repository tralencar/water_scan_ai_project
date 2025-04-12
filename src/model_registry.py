# model_registry.py
import mlflow
from mlflow.tracking.client import MlflowClient


class Singleton(type):
    """
    Metaclass for implementing the Singleton pattern.

    Ensures that only one instance of the class is created and shared
    throughout the application's lifecycle.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Checks if an instance already exists.  
        If not, creates a new one and stores it in the _instances dictionary.

        Returns:
            The unique instance of the class.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ModelRegistryManager(metaclass=Singleton):
    """
    Class responsible for registering and managing model versions in the MLflow Registry.

    Uses the Singleton metaclass to ensure that only one instance
    of the MLflowClient connection is used throughout the pipeline execution.
    """

    def __init__(self):
        """
        Initializes the client for communication with the MLflow Tracking Server.
        """
        self.client = MlflowClient()

    def register_and_transition(
        self,
        model_uri: str,
        model_name: str,
        description: str,
        transition_stage='Production',
    ):
        """
        Registers the trained model in the MLflow Registry and transitions it to a specified stage.

        Args:
            model_uri (str): URI of the saved model (e.g., "runs:/<run_id>/model_name").
            model_name (str): Unique name for the model in the registry.
            description (str): Description of the model (used in both the version and name).
            transition_stage (str, optional): Stage to transition to. Default: "Production".

        Returns:
            model_details: Object containing information about the registered version.
        """
        model_details = mlflow.register_model(model_uri=model_uri, name=model_name)
        self.client.update_registered_model(name=model_name, description=description)
        self.client.update_model_version(
            name=model_name,
            version=model_details.version,
            description='Optimized version via Optuna with SMOTE',
        )
        self.client.transition_model_version_stage(
            name=model_name,
            version=model_details.version,
            stage=transition_stage,
            archive_existing_versions=True,
        )
        print(
            f"✅ Model '{model_name}' (version {model_details.version}) promoted to '{transition_stage}'."
        )
        return model_details
