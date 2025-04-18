# Project Structure

<pre>📂 WATER_SCAN_AI                                       ✅ (Project root directory)</pre>
<pre>├── 📂 .github/workflows                               ✅ (CI/CD workflows with GitHub Actions)</pre>
<pre>│    ├── quality-check.yml                             📌 (Code quality check pipeline)</pre>
<pre>├── 📂 data                                            ✅ (Data used or generated by the project)</pre>
<pre>│    ├── water_potability.csv                          📌 (Input dataset)</pre>
<pre>├── 📂 docs                                            ✅ (Project documentation generated with MkDocs)</pre>
<pre>│    ├── 📂 assets/images                              📌 (Technical documentation images)</pre>
<pre>│    │    ├── 📂 crisp_dm                              📌 (Images from CRISP-DM stages)</pre>
<pre>│    │    │    ├── 2.2.1 - Dataset overview.png</pre>
<pre>│    │    │    ├── 2.2.2 - Checking types and missing values.png</pre>
<pre>│    │    │    ├── 2.2.3 - Missing values visualization.png</pre>
<pre>│    │    │    ├── 2.2.4 - Descriptive statistics.png</pre>
<pre>│    │    │    ├── 2.2.5 - Target variable distribution.png</pre>
<pre>│    │    │    ├── 2.2.6 - Target class percentage.png</pre>
<pre>│    │    │    ├── 2.2.7 - Histograms of variable distributions.png</pre>
<pre>│    │    │    ├── 2.2.8 - Boxplots to detect outliers.png</pre>
<pre>│    │    │    ├── 2.2.9 - Variable correlation heatmap.png</pre>
<pre>│    │    │    ├── 2.2.10 - KDE plots by class.png</pre>
<pre>│    │    │    ├── 5.1 - Model evaluation.png</pre>
<pre>│    │    │    ├── crisp_dm_introduction.png</pre>
<pre>│    │    ├── minio_configuration_access.png</pre>
<pre>│    │    ├── minio_configuration_buckets_part_1.png</pre>
<pre>│    │    ├── minio_configuration_buckets_part_2.png</pre>
<pre>│    ├── 📄 changelog.md                               📌 (Change log)</pre>
<pre>│    ├── 📄 contributing.md                            📌 (Contribution guide)</pre>
<pre>│    ├── 📄 index.md                                   📌 (Main documentation page)</pre>
<pre>│    ├── 📄 crisp_dm_stages.md                         📌 (Project methodology using CRISP-DM)</pre>
<pre>│    ├── 📄 installation.md                            📌 (Installation guide)</pre>
<pre>│    ├── 📄 usage.md                                   📌 (How to use the project)</pre>
<pre>│    ├── 📄 project_structure.md                       📌 (Project structure)</pre>
<pre>│    ├── 📄 modules_index.md                           📌 (Modules index)</pre>
<pre>│    ├── 📄 module_1.md                                📌 (Module 1: water_scan_main.py)</pre>
<pre>│    ├── 📄 module_2.md                                📌 (Module 2: data_pipeline.py)</pre>
<pre>│    ├── 📄 module_3.md                                📌 (Module 3: mlflow_logger.py)</pre>
<pre>│    ├── 📄 module_4.md                                📌 (Module 4: model_registry.py)</pre>
<pre>│    ├── 📄 module_5.md                                📌 (Module 5: model_trainer.py)</pre>
<pre>│    ├── 📄 module_6.md                                📌 (Module 6: trainer_factory.py)</pre>
<pre>├── 📂 mlflow-minio-setup                              ✅ (MLflow + MinIO setup scripts and configs)</pre>
<pre>│    ├── docker-compose.yml                            📌 (Docker Compose configuration file)</pre>
<pre>├── 📂 notebooks                                       ✅ (Project's interactive notebooks)</pre>
<pre>│    ├── crisp_dm_stages.ipynb                         📌 (Notebook for CRISP-DM methodology)</pre>
<pre>├── 📂 src                                             ✅ (Main Python modules of the project)</pre>
<pre>│    ├── __init__.py </pre>
<pre>│    ├── data_pipeline.py                              📌 (Preprocessing pipeline)</pre>
<pre>│    ├── mlflow_logger.py                              📌 (MLflow logging module)</pre>
<pre>│    ├── model_registry.py                             📌 (Model registry management)</pre>
<pre>│    ├── model_trainer.py                              📌 (Model training functions)</pre>
<pre>│    ├── trainer_factory.py                            📌 (Factory for selecting training algorithms)</pre>
<pre>│    ├── water_scan_main.py                            📌 (Main execution script)</pre>
<pre>├── 📂 tests                                           ✅ (Test folder)</pre>
<pre>│    ├── __init__.py </pre>
<pre>│    ├── conftest.py                                   📌 Reusable fixtures (e.g., mock data)</pre>
<pre>│    ├── test_data_pipeline.py                         📌 Tests for data pipeline</pre>
<pre>│    ├── test_model_trainer.py                         📌 Tests for training with RandomForest + Optuna</pre>
<pre>│    ├── test_trainer_factory.py                       📌 Tests for trainer factory</pre>
<pre>├── .gitignore                                         📌 (Files and folders ignored by Git)</pre>
<pre>├── .pre-commit-config.yaml                            ✅ (Pre-commit hooks configuration)</pre>
<pre>├── .pytest.ini                                        ✅ (Pytest configuration)</pre>
<pre>├── .python-version                                    📌 (Python version used)</pre>
<pre>├── bumpversion.cfg                                    ✅ (bump2version configuration)</pre>
<pre>├── Makefile                                           ✅ (Automation commands for the project)</pre>
<pre>├── mkdocs.yml                                         ✅ (MkDocs configuration file)</pre>
<pre>├── pyproject.toml                                     ✅ (Project dependency and build management)</pre>
<pre>├── README.md                                          📌 (Project overview and main instructions)</pre>

[⬅ Back to Home Page](index.md)
