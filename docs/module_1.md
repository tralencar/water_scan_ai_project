# 📚 Technical Reference of the Modules

## 🔹 1) `water_scan_main.py`
Main script that orchestrates the entire pipeline:
- Initializes experiment in MLflow
- Loads and processes the data
- Creates a trainer using `TrainerFactory`
- Optimizes hyperparameters with Optuna
- Saves the model in MLflow
- Registers the model in the Model Registry (production)

### ::: src.water_scan_main

[⬅ Back to Home Page](index.md)
