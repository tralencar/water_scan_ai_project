# model_trainer.py
import os
from functools import partial

import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
import numpy as np
import optuna
from mlflow.models.signature import infer_signature
from mlflow_logger import MLFlowLogger
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


class RandomForestTrainer:
    """
    Class responsible for training and evaluating a RandomForestClassifier model,
    including hyperparameter optimization with Optuna and logging with MLflow.
    """

    def __init__(self, X_train, X_test, y_train, y_test):
        """
        Initializes the trainer with training and testing datasets.

        Args:
            X_train (DataFrame): Training set - features.
            X_test (DataFrame): Test set - features.
            y_train (Series): Training set - target.
            y_test (Series): Test set - target.
        """
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

    def objective(self, trial):
        """
        Objective function used by Optuna to test combinations of hyperparameters.

        Args:
            trial (optuna.trial): Optuna trial object.

        Returns:
            float: Model accuracy with the tested hyperparameters.
        """
        params = {
            'n_estimators': trial.suggest_int('n_estimators', 50, 200),
            'max_depth': trial.suggest_categorical('max_depth', [10, 20, None]),
            'min_samples_split': trial.suggest_int('min_samples_split', 2, 10),
            'random_state': 42,
        }

        model = RandomForestClassifier(**params)
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)

        acc = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred, zero_division=0)
        recall = recall_score(self.y_test, y_pred, zero_division=0)
        f1 = f1_score(self.y_test, y_pred, zero_division=0)
        bal_acc = balanced_accuracy_score(self.y_test, y_pred)
        try:
            roc_auc = roc_auc_score(self.y_test, model.predict_proba(self.X_test)[:, 1])
        except Exception:
            roc_auc = np.nan

        metrics = {
            'accuracy': acc,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'balanced_accuracy': bal_acc,
            'roc_auc': roc_auc,
        }

        try:
            if mlflow.active_run():
                mlflow.end_run()
            with mlflow.start_run(run_name=f'RF_Optuna_Trial_{trial.number}'):
                mlflow.set_tag('optuna_trial_number', trial.number)
                mlflow.log_params(params)
                mlflow.log_metrics(metrics)

                input_example = self.X_train.iloc[:1]
                signature = infer_signature(self.X_train, model.predict(self.X_train))
                mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path='random_forest',
                    input_example=input_example,
                    signature=signature,
                )

                MLFlowLogger.log_artifacts_and_plots(
                    trial.number, self.y_test, y_pred, self.X_train, model
                )
        except Exception as e:
            print(f'[Erro no MLflow - trial {trial.number}] {e}')
        finally:
            if mlflow.active_run():
                mlflow.end_run()

        return acc

    def run_optuna(self, n_trials=10):
        """
        Runs the hyperparameter optimization process using Optuna.

        Args:
            n_trials (int): Number of optimization trials.

        Returns:
            optuna.Study: Study containing the results of the trials.
        """
        study = optuna.create_study(direction='maximize')
        study.optimize(partial(self.objective), n_trials=n_trials)
        print('Melhores parâmetros:', study.best_params)
        return study

    def save_best_model(self, best_params):
        """
        Trains the final model using the best hyperparameters found,
        logs metrics and artifacts to MLflow, and returns the final model.

        Args:
            best_params (dict): Dictionary containing the best hyperparameters.

        Returns:
            Tuple[sklearn model, float, mlflow.models.signature]: Model, final accuracy, and model signature.
        """
        model = RandomForestClassifier(**best_params, random_state=42)
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)

        acc = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred, zero_division=0)
        recall = recall_score(self.y_test, y_pred, zero_division=0)
        f1 = f1_score(self.y_test, y_pred, zero_division=0)
        bal_acc = balanced_accuracy_score(self.y_test, y_pred)
        try:
            roc_auc = roc_auc_score(self.y_test, model.predict_proba(self.X_test)[:, 1])
        except Exception:
            roc_auc = np.nan

        metrics = {
            'final_accuracy': acc,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'balanced_accuracy': bal_acc,
            'roc_auc': roc_auc,
        }

        input_example = self.X_train.iloc[:1]
        signature = infer_signature(self.X_train, model.predict(self.X_train))

        try:
            if mlflow.active_run():
                mlflow.end_run()
            with mlflow.start_run(run_name='BestModel_Final'):
                mlflow.set_tag('model_version', 'final')
                mlflow.log_params(best_params)
                mlflow.log_metrics(metrics)
                mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path='random_forest',
                    input_example=input_example,
                    signature=signature,
                )

                cls_report = classification_report(
                    self.y_test, y_pred, output_dict=False
                )
                report_file = 'classification_report.txt'
                with open(report_file, 'w') as f:
                    f.write(cls_report)
                mlflow.log_artifact(report_file)

                from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix

                cm = confusion_matrix(self.y_test, y_pred)
                disp = ConfusionMatrixDisplay(confusion_matrix=cm)
                disp.plot()
                plt.title('Confusion Matrix')
                plt.tight_layout()
                cm_file = 'confusion_matrix.png'
                plt.savefig(cm_file)
                mlflow.log_artifact(cm_file)
                plt.close()

                importances = model.feature_importances_
                plt.figure(figsize=(8, 5))
                plt.barh(self.X_train.columns, importances)
                plt.xlabel('Importance')
                plt.title('Feature Importance')
                plt.tight_layout()
                fi_file = 'feature_importance.png'
                plt.savefig(fi_file)
                mlflow.log_artifact(fi_file)
                plt.close()
        except Exception as e:
            print(f'[Erro ao salvar modelo final] {e}')
        finally:
            if mlflow.active_run():
                mlflow.end_run()

        for file in [
            'classification_report.txt',
            'confusion_matrix.png',
            'feature_importance.png',
        ]:
            if os.path.exists(file):
                os.remove(file)
        return model, acc, signature
