# Water Scan AI

💧 **Water Scan AI** is a Machine Learning project that classifies water potability using preprocessing techniques, class balancing, hyperparameter optimization, and model versioning with MLflow.

- **Project Name**: `water_scan_ai`
- **Author**: `tralencar`
- **Version**: "1.0.1"
- **License**: `MIT`
- **Keywords**: `quality`, `water`
- **Data Source**: [Dataset (Water Quality)](https://www.kaggle.com/datasets/adityakadiwal/water-potability/data) from Kaggle.

## 🔹 Features

✅ Programming Language: `Python` <br>
✅ Structured using the `Factory Method Pattern` for trainer creation <br>
✅ Uses the `Facade Pattern` in the logging module with MLflow (`MLFlowLogger`) <br>
✅ Uses the `Singleton Pattern` to manage entries in the MLflow Registry <br>
✅ Hyperparameter optimization with `Optuna` <br>
✅ Class balancing with `SMOTE` (imblearn) <br>
✅ Logging and tracking of experiments using `MLflow` <br>
✅ Model registration and versioning with `MLflow Model Registry` <br>
✅ Metric and artifact visualization with `matplotlib` and `MLflow` <br>
✅ Evaluation using `scikit-learn` metrics <br>
✅ Supports `Random Forest` models, with structure ready for XGBoost and LightGBM <br>
✅ Code quality tools: `Pre-commit`, `Ruff`, `Black`, `Flake8`, `Isort` <br>
✅ Task automation using `Makefile` <br>
✅ Semantic version control with `bump2version` <br>
✅ Automated testing with `Pytest` + `Pytest-Cov` <br>
✅ Auto-generated documentation using `MkDocs` + `MkDocs Material` <br>
✅ Automatic formatting and linting with `Ruff`, `Black`, and `Isort` <br>
✅ Git hook support for code validation using `Pre-commit` <br>
✅ Code structured using the `Singleton Pattern` for model registry management <br>
✅ Modular and reusable architecture using `Poetry` for dependency management <br>
✅ **Continuous Integration (CI)** with `GitHub Actions` for code quality validation, including: <br>
🔹 - Automated quality checks on every `push` or `pull request` to the `main` branch <br>
🔹 - Python environment setup with `Poetry` <br>
🔹 - Automatic installation of development dependencies <br>
🔹 - Execution of `make quality` rule to ensure code standardization <br>

## 🔹 Documentation Structure
- **[Installation](installation.md)**: How to set up the environment.
- **[Project Usage](usage.md)**: How to run the scraper.
- **[Project Structure](project_structure.md)**: File structure explanation.
- **[Methodology (CRISP-DM)](crisp_dm_stages.md)**: CRISP-DM methodology used in the project.
- **[Project Modules](modules_index.md)**: Technical reference.
- **[Contributing](contributing.md)**: How to contribute to the project.
- **[Tests](tests.md)**: Tests used in the project.
- **[Changelog](changelog.md)**: Version history.
