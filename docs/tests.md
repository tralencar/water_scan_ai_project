# Automated Testing with Pytest

This project uses the **[Pytest](https://docs.pytest.org/en/stable/)** library to perform automated tests, ensuring code quality, reliability, and maintainability.

## 🔹 Test Structure

The tests are organized in the `tests/` directory, separated by component:

<pre>📂 WATER_SCAN_AI                           ✅ (Project root directory)</pre>
<pre>├── 📂 tests                               ✅ (Test folder)</pre>
<pre>│    ├── conftest.py                       📌 Reusable fixtures (e.g., mock data)</pre>
<pre>│    ├── test_data_pipeline.py             📌 Tests for the data pipeline</pre>
<pre>│    ├── test_model_trainer.py             📌 Tests for training with RandomForest + Optuna</pre>
<pre>│    ├── test_trainer_factory.py           📌 Tests for the trainer factory</pre>

## 🔹 Tools Used

* `pytest`: main testing framework
* `pytest-cov`: code coverage analysis
* `monkeypatch`: mocking of external functions and methods
* `tmp_path fixture`: creation of temporary test files

## 🔹 Fixtures (conftest.py)

The `conftest.py` file defines reusable data and configuration for multiple tests.

## 🔹 Tests Created

✅ 1) `test_data_pipeline.py` <br>

* `test_pipeline_load_and_clean` <br>
🧪 Tests reading a CSV and handling missing values. <br>
📝 **Note:**
Simulates a `.csv` file with missing values and checks whether the `fillna(median)` method in `DataPipeline` correctly removes NaNs. Ensures the pipeline starts with clean data — essential to avoid model errors.

* `test_data_preprocessing_split_and_smote` <br>
🧪 Verifies train/test split and SMOTE application. <br>
📝 **Note:**
Checks that the data is split with stratification (maintaining the `Potability` proportion) and that SMOTE correctly balances the classes. This guarantees balanced training and prevents bias toward the majority class.

✅ 2) `test_trainer_factory.py` <br>

* `test_create_trainer_success` <br>
🧪 Tests successful creation of a RandomForest trainer. <br>
📝 **Note:**
Verifies that the factory returns the correct instance (`RandomForestTrainer`) when receiving `random_forest` as the input. A key test for validating the modularity of the system through the Factory pattern.

* `test_create_trainer_invalid_model` <br>
⚠️ Tests error handling when providing an invalid model. <br>
📝 **Note:**
Ensures the system raises a `ValueError` when an unsupported model type is passed. Important for protecting the API from misuse and anticipating production failures.

✅ 3) `test_model_trainer.py` <br>

* `test_optuna_fake` <br>
🧪 Tests Optuna optimization execution using monkeypatch, without running a real session. <br>
📝 **Note:**
Uses `monkeypatch` to replace the `objective()` method and force a fixed return (e.g., `0.9`). This enables testing the Optuna optimization flow without running the actual training or MLflow logging. Ideal for reducing execution time and safely simulating real environments.

## 🔹 Running the Tests

You can run the tests with:

```bash
make test
```

Or directly using Poetry:

`poetry run pytest --cov=src --cov-report=term-missing`

## 🔹 Code Coverage

Test coverage is automatically generated via `pytest-cov`. To view it:

`poetry run pytest --cov=src --cov-report=term-missing`

💡 Use --cov-fail-under=27 to require a minimum of 27% coverage.

## 🔹 Configuração do Pytest

The project uses the `.pytest.ini` file to configure the correct path.

📌 Notes (Best practices followed): <br>
✅ Modular test structure <br>
✅ Use of fixtures to avoid repetition <br>
✅ Component mocking with `monkeypatch` <br>
✅ Independent and isolated tests <br>
✅ Code coverage with `pytest-cov` <br>
