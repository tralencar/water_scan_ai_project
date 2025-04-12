# mlflow_logger.py
import os
from datetime import datetime

import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    classification_report,
    confusion_matrix,
)


class MLFlowLogger:
    """
    Facade for MLflow setup and logging.

    This class provides static methods to configure experiments,
    save artifacts, and log visualizations such as:
    - classification reports
    - confusion matrices
    - feature importance
    """

    @staticmethod
    def setup_experiment(experiment_name: str) -> str:
        """
        Creates a new MLflow experiment with the current timestamp and sets the tracking URI.

        Args:
            experiment_name (str): Base name of the experiment.

        Returns:
            str: Full experiment name with date and time.
        """
        now = datetime.now()
        current_time = now.strftime('%d/%m/%Y - %H:%M:%S')
        mlflow.set_tracking_uri('http://localhost:5001/')
        experiment_name_full = f'{experiment_name} ({current_time})'

        print('___________________________________________________________')
        print(f'Experiment name = {experiment_name_full}')
        print('___________________________________________________________')

        mlflow.set_experiment(experiment_name_full)
        return experiment_name_full

    @staticmethod
    def log_artifacts_and_plots(trial_number, y_test, y_pred, X_train, model):
        """
        Saves and logs the following artifacts to MLflow:
        - Classification report
        - Confusion matrix
        - Feature importance plot

        Args:
            trial_number (int): Trial number during Optuna optimization.
            y_test (array-like): True target values.
            y_pred (array-like): Predicted values from the model.
            X_train (DataFrame): Training set (used to extract feature names).
            model (sklearn model): Trained model with `feature_importances_` attribute.
        """
        # Classification Report
        cls_report = classification_report(y_test, y_pred, output_dict=False)
        report_path = f'classification_report_trial_{trial_number}.txt'
        with open(report_path, 'w') as f:
            f.write(cls_report)
        mlflow.log_artifact(report_path)

        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.title('Confusion Matrix')
        plt.tight_layout()
        cm_path = f'confusion_matrix_trial_{trial_number}.png'
        plt.savefig(cm_path)
        mlflow.log_artifact(cm_path)
        plt.close()

        # Feature Importance
        importances = model.feature_importances_
        plt.figure(figsize=(8, 5))
        plt.barh(X_train.columns, importances)
        plt.xlabel('Importance')
        plt.title('Feature Importance')
        plt.tight_layout()
        fi_path = f'feature_importance_trial_{trial_number}.png'
        plt.savefig(fi_path)
        mlflow.log_artifact(fi_path)
        plt.close()

        # Limpeza dos arquivos locais
        for path in [report_path, cm_path, fi_path]:
            if os.path.exists(path):
                os.remove(path)
