# main.py
import os

import mlflow
from data_pipeline import DataPipeline, DataPreprocessor
from mlflow_logger import MLFlowLogger
from model_registry import ModelRegistryManager
from sklearn.metrics import classification_report
from trainer_factory import TrainerFactory


def main():
    """
    Executes the main pipeline for water potability classification.

    Steps:
    - Sets up the experiment in MLflow
    - Loads and preprocesses the data
    - Trains a Random Forest model using Optuna
    - Logs results with MLflow
    - Registers the trained model in the MLflow Registry
    """

    # Set up experiment in MLflow
    experiment_name = MLFlowLogger.setup_experiment(
        'water_potability_classification_test'
    )

    print(f'main -> experiment_name (base) = {experiment_name}')

    # Load and preprocess the data
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    data_path = os.path.join(base_dir, 'data', 'water_potability.csv')

    data_pipeline = DataPipeline(data_path)

    df = data_pipeline.load_and_clean_data()
    preprocessor = DataPreprocessor(df, target='Potability')
    X_train, X_test, y_train, y_test = preprocessor.split_data()
    X_train, y_train = preprocessor.apply_smote(X_train, y_train)

    # Create trainer via Factory (Random Forest)
    trainer = TrainerFactory.create_trainer(
        'random_forest', X_train, X_test, y_train, y_test
    )
    study_rf = trainer.run_optuna(n_trials=50)
    best_model, rf_accuracy, signature = trainer.save_best_model(study_rf.best_params)
    print('Accuracy:', rf_accuracy)
    print(classification_report(y_test, best_model.predict(X_test)))

    # Register the model in the MLflow Registry (Singleton)
    registry_manager = ModelRegistryManager()
    run_id = mlflow.search_runs(order_by=['start_time DESC']).iloc[0].run_id
    model_uri = f'runs:/{run_id}/random_forest'
    model_name = 'water_potability_rf'
    registry_manager.register_and_transition(
        model_uri=model_uri,
        model_name=model_name,
        description='Water potability classification model using Random Forest',
    )


if __name__ == '__main__':
    main()
