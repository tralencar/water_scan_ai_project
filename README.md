# Introduction to the Water Scan AI Project Documentation

The full project documentation was built using **mkDocs** and is available at the official site: [Water Scan AI](https://tralencar.github.io/water_scan_ai/).

## Version  
`version = "1.0.1"`

## 🔹 About the Project  
💧 **Water Scan AI** is a Machine Learning project that classifies water potability using preprocessing techniques, class balancing, hyperparameter optimization, and model versioning with MLflow.

- **Project Name**: `water_scan_ai`  
- **Author**: `tralencar`  
- **Version**: `1.0.1`  
- **License**: `MIT`  
- **Keywords**: `quality`, `water`  
- **Data Source**: [Dataset (Water Quality)](https://www.kaggle.com/datasets/adityakadiwal/water-potability/data) from Kaggle.

---

## 🔹 Features

✅ Programming Language: `Python`  
✅ Structured with the `Factory Method Pattern` for trainer creation  
✅ Implements `Facade Pattern` in the logging module using MLflow (MLFlowLogger)  
✅ Implements `Singleton Pattern` for managing entries in the MLflow Registry  
✅ Hyperparameter optimization using `Optuna`  
✅ Class balancing with `SMOTE` (imblearn)  
✅ Experiment logging and tracking with `MLflow`  
✅ Model registration and versioning with `MLflow Model Registry`  
✅ Metrics and artifacts visualization with `matplotlib` and `MLflow`  
✅ Evaluation using `scikit-learn` metrics  
✅ Support for `Random Forest` models, with structure ready for `XGBoost` and `LightGBM`  
✅ Code quality enforcement using `Pre-commit`, `Ruff`, `Black`, `Flake8`, `Isort`  
✅ Task automation with `Makefile`  
✅ Semantic versioning with `bump2version`  
✅ Automated testing with `Pytest` + `Pytest-Cov`  
✅ Auto-generated documentation with `MkDocs` + `MkDocs Material`  
✅ Automatic formatting and linting with `Ruff`, `Black`, and `Isort`  
✅ Git hooks support for code validation using `Pre-commit`  
✅ Code organized with `Singleton Pattern` to manage model registry  
✅ Modular and reusable architecture using `Poetry` for dependency management  
✅ **Continuous Integration (CI)** via `GitHub Actions`, with the following steps:  
🔹 - Automated quality checks on every `push` or `pull request` to the `main` branch  
🔹 - Python environment setup with `Poetry`  
🔹 - Automatic installation of development dependencies  
🔹 - Execution of `make quality` rule to ensure code standardization  

---

## 🔹 Documentation Structure

- **[Installation](https://tralencar.github.io/water_scan_ai/installation/)**: How to set up the environment  
- **[Project Usage](https://tralencar.github.io/water_scan_ai/usage/)**: How to run the scraper  
- **[Project Structure](https://tralencar.github.io/water_scan_ai/project_structure/)**: File structure explained  
- **[CRISP-DM Methodology](https://tralencar.github.io/water_scan_ai/crisp_dm_stages/)**: CRISP-DM stages applied to the project  
- **[Project Modules](https://tralencar.github.io/water_scan_ai/modules_index/)**: Technical reference  
- **[Contributing](https://tralencar.github.io/water_scan_ai/contributing/)**: How to contribute  
- **[Tests](https://tralencar.github.io/water_scan_ai/tests/)**: Testing framework used  
- **[Changelog](https://tralencar.github.io/water_scan_ai/changelog/)**: Version history  

---

## 🔹 Prerequisites

Before installing the project, make sure your environment meets the following requirements:

- **Python** `>=3.9, <4.0`  
- **Git** installed  
- **Poetry** for dependency management  
- **Make** (Makefile support is required)  

---

## 🔹 Installing Dependencies

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/tralencar/water_scan_ai.git
cd water_scan_ai
```

---

### 2️⃣ Install Poetry (if not installed)

`pip install poetry`

---

### 3️⃣ Configure Poetry to create virtual environments inside the project folder

`poetry config virtualenvs.in-project true`

📌 Note:
This will create the `.venv/` folder inside the project directory, making environment management easier and more portable.

---

### 4️⃣ Activate the virtual environment

`poetry shell`

---

### 5️⃣ Install the dependencies

`poetry install`

📌 Observações: <br>

📌 Notes:
* This will install all libraries listed in pyproject.toml, including:
* Data scraping and processing: pandas, seaborn
* Machine Learning and optimization: scikit-learn, xgboost, lightgbm, optuna, imblearn
* Experiment tracking and versioning: mlflow
* Interactive notebooks: jupyter
* Code quality and formatting: black, isort, flake8, ruff, interrogate
* Testing: pytest, pytest-cov
* Version control: bump2version
* Pre-commit validation: pre-commit
* Documentation: mkdocs, mkdocs-material, mkdocstrings-python, pymdown-extensions, mkdocs-bootstrap386

---
### 🔹 Pre-commit Configuration

Pre-commit helps enforce code quality standards. To enable it, run:

`poetry run pre-commit install`

📌 Note:

From now on, every time you make a commit, pre-commit hooks will automatically run.

---
### 🔹 Verifying Installation

To ensure everything was installed correctly, run:

`poetry run python -c "import pandas; print('Instalação bem-sucedida!')"`

📌 Note: <br>

* If the message "Installation successful!" appears, everything is correctly configured.

---

## 🔹 MinIO + MLflow Integration Configuration

For instructions on how to set up MinIO and MLflow integration, visit the official site: [Water Scan AI](https://tralencar.github.io/water_scan_ai/installation/#configuracao-da-integracao-minio-mlflow).
