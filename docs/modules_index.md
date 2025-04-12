# 📚 Technical Reference of the Modules

## 🔹 **[water_scan_main.py](module_1.md)**
Main script that orchestrates the entire pipeline:
- Initializes an experiment in MLflow
- Loads and processes the data
- Creates a trainer via `TrainerFactory`
- Optimizes hyperparameters using Optuna
- Saves the model in MLflow
- Registers the model in the Model Registry (production)

## 🔹 **[data_pipeline.py](module_2.md)**
Contains two main classes:

### DataPipeline
Responsible for:
- Loading the CSV dataset
- Handling missing values

### DataPreprocessor
Responsible for:
- Train/test split using `train_test_split`
- Data balancing using SMOTE

## 🔹 **[mlflow_logger.py](module_3.md)**
Facade that encapsulates logging functions in MLflow:
- Experiment setup
- Artifact logging:
  - `classification_report`
  - `confusion_matrix`
  - `feature_importance`

## 🔹 **[model_registry.py](module_4.md)**
Uses the Singleton pattern to register models in the MLflow Registry:
- Register the model URI
- Add a description and transition to production
- Archive previous versions

## 🔹 **[model_trainer.py](module_5.md)**
Main class: `RandomForestTrainer`

Functions:
- Optimizes hyperparameters with Optuna
- Logs to MLflow (params, metrics, model)
- Logs artifacts (report, matrix, importance)
- Saves the best model with complete logging

## 🔹 **[trainer_factory.py](module_6.md)**
Implements the Factory pattern to instantiate trainers.
Currently implemented:
- `"random_forest"`: returns an instance of `RandomForestTrainer`

[⬅ Back to Home Page](index.md)
