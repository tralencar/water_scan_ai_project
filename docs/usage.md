# Project Usage

This project includes automations via **Makefile** to simplify the execution of the main tasks. Below are the commands to run the classifier, check code quality, run tests, and update the documentation.

---

## 🔹 **Setting up the environment with Poetry**

Before running any command in this project, it is **highly recommended** to properly configure the Poetry virtual environment. This ensures that all dependencies are correctly installed and managed within the project.

## 🔹 **Create the virtual environment inside the project**

By default, **Poetry** creates the virtual environment outside the project directory. To keep the virtual environment within the repository, run:

`poetry config virtualenvs.in-project true`

📌 Notes: <br>
➡ This ensures that the virtual environment is created inside the `.venv/` folder, making management easier. <br>
➡ Useful for maintaining isolated environments for each project. <br>
➡ Avoids conflicts between different dependency versions.

## 🔹 **Activate the virtual environment**

To activate the virtual environment and enter the Poetry shell, run:

`poetry shell`

---

## 🔹 **Running the Water Scan AI Classifier**

To run the Water Scan AI classifier, execute:

`make run`

or directly via Poetry:

`poetry install`

`poetry run python src/water_scan_main.py`

📌 Notes: <br>
➡ This command handles data loading, preprocessing, training, MLflow logging, and model registration. <br>
➡ It ensures that all dependencies are installed before execution.

---

## 🔹 Checking Code Quality

To run code quality checks using pre-commit, execute:

`make quality`

This command runs:

* Black (automatic code formatting)  
* Isort (import sorting)  
* Flake8 (code linting)  
* Ruff (optimized linter)  
* Pre-commit hooks to prevent broken commits

If you prefer to run it manually:

`poetry run pre-commit run --all-files`

📌 Notes: <br>
➡ Running `make quality` before committing helps prevent formatting issues and poor code quality. <br>
➡ Helps maintain a consistent code standard across the project. <br>
➡ Avoids CI/CD pipeline failures by catching errors early.

---

## 🔹 Running MkDocs Documentation

To preview the documentation locally:

`make doc`

or directly via Poetry:

`poetry run mkdocs serve`

Now, open `http://127.0.0.1:8000/` in your browser.

📌 Notes: <br>
➡ Useful for previewing the documentation before publishing. <br>
➡ Keeps the documentation always accessible to the team. <br>
➡ Prevents formatting issues and broken links before deployment. <br>

---

## 🔹 Publishing the Documentation Online (GitHub Pages)

After making changes to the documentation, you can publish it online to GitHub Pages using the following command:

`poetry run mkdocs gh-deploy`

This will perform the following: <br>
1️⃣ Builds the documentation and converts the Markdown (.md) files to HTML. <br>
2️⃣ Creates a new commit on the `gh-pages` branch with the latest version of the documentation. <br>
3️⃣ Updates the public project page available on GitHub Pages. <br>

If the project is properly configured, the documentation will be available at:

`https://tralencar.github.io/water_scan_ai/`

---

## 🔹 Updating the Project Version (bump2version)

If you want to bump the project version, use:

```bash
poetry run bump2version patch   # For small changes
poetry run bump2version minor   # For minor updates
poetry run bump2version major   # For major updates
```

This will automatically update the project version in `pyproject.toml`.

📌 Notes: <br>
➡ Used to maintain version control as the project evolves. <br>
➡ Important for teams that follow semantic versioning (semver). <br>
➡ Ensures traceability of code changes.

---

## 🔹 Running Tests (pytest)

To run unit tests and check code coverage, execute:

`make test`

This command:

* Installs development dependencies  
* Runs `pytest` with a minimum required coverage of 27%  
* Displays a coverage report

📌 Notes: <br>
➡ Prevents broken code from reaching production. <br>
➡ Ensures correct functionality before adding new features. <br>
➡ The minimum coverage of 8% can be adjusted as more tests are added. This change must be made in the `Makefile`.

---

## 🔹 Running Poetry Lock

If you need to update the `poetry.lock` file, execute:

`make lock`

or directly via Poetry:

`poetry lock`

📌 Notes: <br>
➡ Useful when adding or updating packages in `pyproject.toml`. <br>
➡ Ensures that all dependencies are properly locked. <br>
➡ Prevents conflicts when working in teams.

---

## 🔹 Managing MLflow with Docker Compose

This project uses Docker Compose to run MLflow Tracking and MinIO services in an automated way. <br>

## 🔧 Building the containers:

`make build`

📌 Note: <br>
➡ Builds and starts the services defined in `mlflow-minio-setup/docker-compose.yml` in the background.

## ⛔ Stopping the services:

`make end`

📌 Note: <br>
➡ Stops the running containers, such as MLflow and MinIO.

## 🧹 Cleaning Up All Docker Containers:

`make clear_all`

📌 Notes: <br>
➡ Forcefully removes all stopped or running containers. <br>
➡ ⚠ Use with caution, as it removes all local containers, including those from other projects. <br>

---

[⬅ Back to Home Page](index.md)
