# Introdução a documentação do projeto Water Scan AI

A documentação completa do projeto foi feita com o mkDocs e esta disponível no seguinte site oficial [Water Scan AI](https://tralencar.github.io/water_scan_ai/).

## Versão
version = "1.0.1"

## 🔹 Sobre o Projeto
💧 **Water Scan AI** é um projeto de Machine Learning que classifica a potabilidade da água utilizando técnicas de pré-processamento, balanceamento de classes, otimização de hiperparâmetros e versionamento de modelos com MLflow.

- **Nome do Projeto**: `water_scan_ai`
- **Autor**: `tralencar`
- **version** = "1.0.1"
- **Licença**: `MIT`
- **Palavras-chave**: `quality`, `water`
- **Fonte dos dados**: [Dataset (Water Quality)](https://www.kaggle.com/datasets/adityakadiwal/water-potability/data) do Kaggle.

---

## 🔹 Recursos

✅ Linguagem de programação: `Python` <br>
✅ Estruturado com `Padrão Factory Method` para criação de treinadores <br>
✅ Uso do `Padrão Facade` no módulo de logging com MLflow (MLFlowLogger) <br>
✅ Uso do `Padrão Singleton` para o gerenciamento de registros no MLflow Registry <br>
✅ Otimização de hiperparâmetros com `Optuna` <br>
✅ Balanceamento de classes com `SMOTE` (imblearn) <br>
✅ Logging e tracking de experimentos com `MLflow` <br>
✅ Registro e versionamento de modelos com `MLflow Model Registry` <br>
✅ Visualização de métricas e artefatos com `matplotlib` e `MLflow` <br>
✅ Avaliação com métricas de `scikit-learn` <br>
✅ Suporte a modelos `Random Forest`, com estrutura pronta para XGBoost e LightGBM <br>
✅ Qualidade de código com `Pre-commit`, `Ruff`, `Black`, `Flake8`, `Isort` <br>
✅ Automação de tarefas com `Makefile` <br>
✅ Controle de versão semântico com `bump2version` <br>
✅ Testes automatizados com `Pytest` + `Pytest-Cov` <br>
✅ Documentação gerada automaticamente com `MkDocs` + `MkDocs Material` <br>
✅ Formatação e linting automáticos com `Ruff`, `Black` e `Isort` <br>
✅ Suporte a hooks Git para validação de código com `Pre-commit` <br>
✅ Código organizado com o `Padrão Singleton` para gerenciar o registro de modelos <br>
✅ Estrutura modular e reutilizável com `Poetry` para dependências <br>
✅ **Integração Contínua (CI)** com `GitHub Actions` para validação de código e qualidade com as seguintes etapas: <br>
🔹 - Automatiza a execução de verificações de qualidade a cada `push` ou `pull request` na branch `main`. <br>
🔹 - Configuração do ambiente `Python` com `Poetry`. <br>
🔹 - Instalação automática de dependências de desenvolvimento. <br>
🔹 - Execução da regra `make quality` para garantir a padronização do código. <br>

---

## 🔹 Estrutura da Documentação
- **[Instalação](https://tralencar.github.io/water_scan_ai/installation/)**: Como configurar o ambiente.
- **[Uso do projeto](https://tralencar.github.io/water_scan_ai/usage/)**: Como rodar o scraper.
- **[Estrutura do projeto](https://tralencar.github.io/water_scan_ai/project_structure/)**: Explicação dos arquivos.
- **[Metodologia utilizada (CRISP-DM)](https://tralencar.github.io/water_scan_ai/crisp_dm_stages/)**: Metodologia CRISP-DM utilizada no projeto.
- **[Módulos do projeto](https://tralencar.github.io/water_scan_ai/modules_index/)**: Referência técnica.
- **[Contribuição](https://tralencar.github.io/water_scan_ai/contributing/)**: Como contribuir com o projeto.
- **[Testes](https://tralencar.github.io/water_scan_ai/tests/)**: Testes utilizados no projeto.
- **[Histórico das alterações](https://tralencar.github.io/water_scan_ai/changelog/)**: Histórico de versões.

---

## 🔹 Pré-requisitos

Antes de instalar o projeto, certifique-se de que seu ambiente atende aos seguintes requisitos:

- **Python** `>=3.9, <4.0`
- **Git** instalado
- **Poetry** para gerenciamento de dependências
- **Make** (`makefile` foi adicionado às dependências)

---

## 🔹 Instalando as Dependências

### **1️⃣ Clone o repositório**

`git clone https://github.com/tralencar/water_scan_ai.git`

`cd water_scan_ai`

---

### 2️⃣ Instale o Poetry (se ainda não tiver)

`pip install poetry`

---

### 3️⃣ Configure o Poetry para criar ambientes virtuais no diretório do projeto

`poetry config virtualenvs.in-project true`

📌 Observação:
* Isso criará a pasta `.venv/` dentro do projeto, facilitando o isolamento e a portabilidade do ambiente.

---

### 4️⃣ Ative o ambiente virtual

`poetry shell`

---

### 5️⃣ Instale as dependências

`poetry install`

📌 Observações: <br>

* Isso instalará todas as bibliotecas listadas no `pyproject.toml`, incluindo: <br>
* Scraping e processamento de dados: `pandas`, `seaborn` <br>
* Machine Learning e Otimização: `scikit-learn`, `xgboost`, `lightgbm`, `optuna`, `imblearn` <br>
* Rastreamento e versionamento de experimentos: `mlflow` <br>
* Notebooks interativos: `jupyter` <br>
* Qualidade e formatação de código: `black`, `isort`, `flake8`, `ruff`, `interrogate` <br>
* Testes: `pytest`, `pytest-cov` <br>
* Controle de versão: `bump2version` <br>
* Pré-commit: `pre-commit` <br>
* Documentação: `mkdocs`, `mkdocs-material`, `mkdocstrings-python`, `pymdown-extensions`, `mkdocs-bootstrap386`

---
### 🔹 Configuração do pre-commit

O pre-commit ajuda a manter a qualidade do código. Para ativá-lo, execute:

`poetry run pre-commit install`

📌 Observação: <br>

* Agora, todas as vezes que você fizer um commit, os hooks do `pre-commit` rodarão automaticamente.

---
### 🔹 Verificando a Instalação

Para garantir que tudo foi instalado corretamente, execute:

`poetry run python -c "import pandas; print('Instalação bem-sucedida!')"`

📌 Observação: <br>

* Se a mensagem **"Instalação bem-sucedida"** aparecer, tudo está configurado corretamente.

---

## 🔹 Configuração da integração MinIO + MLflow

A configuração da integração do MinIO e MLflow pode ser acessada no seguinte site oficial [Water Scan AI](https://tralencar.github.io/water_scan_ai/installation/#configuracao-da-integracao-minio-mlflow).
