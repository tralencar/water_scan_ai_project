# Introduction to the Water Scan AI Project Documentation

The full project documentation was built using **mkDocs** and is available at the official site: [Water Scan AI](https://tralencar.github.io/water_scan_ai_project/).

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

## 🔹 Visual Identity of the Water Scan AI logo

> The *Water Scan AI* logo is more than just a visual representation; it encapsulates the project’s core mission of **leveraging artificial intelligence to ensure water potability**.
> As a brand, it conveys **trust, innovation, and environmental responsibility**, positioning the solution as a **cutting-edge tool** for **water quality analysis and management**.
> The logo effectively combines elements of **technology** and **sustainability**, emphasizing the project’s commitment to **solving global water challenges** while ensuring the **accuracy and reliability** of its data-driven insights.

<p align="center">
  <img src="https://raw.githubusercontent.com/tralencar/water_scan_ai_project/main/docs/assets/images/water_scan_ai_logo.png" alt="Water Scan AI logo" width="300"/>
</p>

### 1. Simplicity and Clear Connection with Water
The central **water droplet icon** is universally recognized, instantly communicating the focus of the project on **water potability**. This symbol serves as a direct representation of the project’s mission to ensure access to safe drinking water.

- **Blue color**: Evokes **freshness, purity**, and **trust**, aligning with the values of sustainability and technological advancement. It represents **stability and reliability**, key factors for a project handling critical environmental data.

### 2. Geometric and Modern Lines: Representing Artificial Intelligence
The **geometric lines** surrounding the water droplet subtly represent **artificial intelligence** and **machine learning**. These modern shapes imply **precision, control**, and **advanced technology**.

- The clean, sharp lines suggest that the project is **data-driven** and powered by **AI**, reinforcing its technical sophistication and differentiation from traditional environmental monitoring systems.

### 3. The Blend of Technology and Sustainability
The integration of the water element with technology-centric lines and shapes visually represents the union of **environmental sustainability** and **innovative AI solutions**.

- This dual representation highlights the project’s aim to **solve environmental problems through advanced technologies** and demonstrates its commitment to **sustainable practices** in the realm of **water management**.

### 4. Integrated Branding Strategy
The visual identity of *Water Scan AI* is designed to **translate the project’s business goals into graphic elements**:

- **Technological innovation** (AI-driven data analysis)
- **Environmental sustainability** (focus on water quality and accessibility)
- **Global impact** (ensuring access to clean water)

This direct connection between **visual brand** and **project mission** improves **communication with stakeholders, partners, and users**, while enhancing **brand recognition**. It positions *Water Scan AI* as a **trustworthy, impactful, and cutting-edge solution** in the field of **water quality management**.

---

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

---

## 🧪 Development Tools

- `ruff` — Linting and formatting
- `black` — Code formatter
- `isort` — Import ordering
- `flake8` — Linting
- `interrogate` — Docstring coverage checker
- `pytest`, `pytest-cov` — Unit testing and coverage
- `pre-commit` — Git hooks for automated code checks
- `bump2version` — Semantic version control
- `Optuna` — Hyperparameter optimization for model training
- `MLflow` — Experiment tracking and model management
- `Poetry` — Dependency management and virtual environment creation
- `Makefile` — Task automation for project workflows
- `Docker` — Containerization for environment consistency and service orchestration
- `MinIO` — Object storage for MLflow artifacts

---

## 🔹 Documentation Structure

- **[Home](https://tralencar.github.io/water_scan_ai_project/)**: Project overview
- **[Installation](https://tralencar.github.io/water_scan_ai_project/installation/)**: How to set up the environment
- **[Project Usage](https://tralencar.github.io/water_scan_ai_project/usage/)**: How to run the project
- **[Project Structure](https://tralencar.github.io/water_scan_ai_project/project_structure/)**: File structure explained
- **[CRISP-DM Methodology](https://tralencar.github.io/water_scan_ai_project/crisp_dm_stages/)**: CRISP-DM stages applied to the project
- **[Project Modules](https://tralencar.github.io/water_scan_ai_project/modules_index/)**: Technical reference
- **[Contributing](https://tralencar.github.io/water_scan_ai_project/contributing/)**: How to contribute
- **[Tests](https://tralencar.github.io/water_scan_ai_project/tests/)**: Testing framework used
- **[Changelog](https://tralencar.github.io/water_scan_ai_project/changelog/)**: Version history

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
git clone https://github.com/tralencar/water_scan_ai_project.git
cd water_scan_ai_project
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

For instructions on how to set up MinIO and MLflow integration, visit the official site: [Water Scan AI](https://tralencar.github.io/water_scan_ai_project/installation/#configuracao-da-integracao-minio-mlflow).
