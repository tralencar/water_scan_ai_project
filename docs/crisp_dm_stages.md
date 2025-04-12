# Introduction

In this water potability classification project, the **CRISP-DM (Cross Industry Standard Process for Data Mining)** methodology was adopted due to its well-defined, iterative structure and its wide recognition in the data science industry.

![Dataset Overview](assets/images/crisp_dm/crisp_dm_introduction.png)

CRISP-DM guided all stages of the project according to the following:

* 1) **Business Understanding:** The main goal was defined as predicting water potability based on physicochemical parameters.
* 2) **Data Understanding:** An exploratory analysis was conducted to understand the structure, quality, and imbalance of the dataset.
* 3) **Data Preparation:** Included handling missing values, applying SMOTE, and splitting the data into training and testing sets.
* 4) **Modeling:** Models such as Random Forest and XGBoost were optimized using Optuna.
* 5) **Evaluation:** Model performance was compared using metrics like accuracy, recall, and F1-score.
* 6) **Deployment:** The best-performing model was registered in the MLflow Registry and is ready for production use.

Choosing CRISP-DM ensured organization, reproducibility, and alignment between technical and business objectives, making it ideal for structured data science projects like this one.

---

# Part 1) Business Understanding (Problem): Water Potability Prediction

### Project Objective

Develop a **supervised classification** model capable of predicting whether a water sample is **potable (1)** or **not potable (0)** based on physicochemical variables.
This solution aims to support public policies in sanitation, health, and environmental monitoring, contributing directly to access to safe water, as recommended by the World Health Organization (WHO).

---

### Context

Access to safe drinking water is a **fundamental human right** and a crucial component of public health policies.
Water quality has a direct impact on population health, hospital costs, and economic productivity.
In many regions, improvements in supply systems and quality monitoring result in net economic benefits by reducing waterborne diseases.

Based on a dataset of **3,276 observations** from various water sources, this project seeks to predict **water potability** using 9 measurable variables that reflect the chemical, physical, and microbiological characteristics of water.

---

### Variable Description

| Variable           | Description                                                                 | Recommended Range / Limit       |
|--------------------|------------------------------------------------------------------------------|----------------------------------|
| `ph`               | Measures the acid-base balance of water. Ideal range is 6.5 to 8.5.         | 6.5 – 8.5 (WHO)                  |
| `Hardness`         | Concentration of calcium and magnesium salts (hardness).                   | —                                |
| `Solids`           | Total Dissolved Solids (TDS). Indicates mineralization level.              | < 500 mg/L (ideal), max. 1000    |
| `Chloramines`      | Common disinfectant agent used in potable water.                           | ≤ 4 mg/L                         |
| `Sulfate`          | Naturally occurring substance found in various environments.               | 3 to 30 mg/L (normal), up to 1000|
| `Conductivity`     | Related to the amount of dissolved ions.                                   | ≤ 400 μS/cm                      |
| `Organic_carbon`   | Represents natural or synthetic organic matter present in the water.       | < 4 mg/L                         |
| `Trihalomethanes`  | Byproducts of chlorine treatment.                                          | ≤ 80 ppm                         |
| `Turbidity`        | Opacity caused by suspended particles.                                     | ≤ 5 NTU                          |
| `Potability`       | **Target variable**. Indicates if the water is potable (1) or not (0).     | —                                |

---

### Problem Nature

- **Type:** Binary Classification (`0 = Not Potable`, `1 = Potable`)
- **Target Variable:** `Potability`
- **Predictor Variables:** 9 continuous variables related to water quality
- **Potential Challenge:** Class imbalance

---

### Practical Applications

- Automation of water treatment plants
- Real-time monitoring via sensors
- Alert systems for public managers and municipalities
- Decision support in contexts of water crises or environmental disasters

---

# Part 2) Data Understanding

### 2.1) Data Source

The data used in this project was obtained from the [Dataset (Water Quality)](https://www.kaggle.com/datasets/adityakadiwal/water-potability/data) on Kaggle.
The dataset used in this project is provided in the file `water_potability.csv`, with an approximate size of 525 KB, containing **3,276 records** and **10 columns**, each representing a physicochemical variable or the water potability label.

This dataset simulates samples from various water sources and aims to represent diverse water quality scenarios, based on parameters defined by regulatory agencies such as the **WHO (World Health Organization)** and the **EPA (United States Environmental Protection Agency)**.

---

### Column Description

| #  | Column             | Unit        | Description                                                                                 |
|----|--------------------|-------------|---------------------------------------------------------------------------------------------|
| 1  | `ph`               | —           | Measure of the acidity or alkalinity of water (scale from 0 to 14).                        |
| 2  | `Hardness`         | mg/L        | Water's ability to precipitate soap, related to the presence of calcium and magnesium.     |
| 3  | `Solids`           | ppm         | Total dissolved solids. High concentration affects water taste and color.                  |
| 4  | `Chloramines`      | ppm         | Concentration of chloramines, common disinfectants in public water systems.                |
| 5  | `Sulfate`          | mg/L        | Amount of dissolved sulfate, naturally present in soils and rocks.                         |
| 6  | `Conductivity`     | µS/cm       | Electrical conductivity of water, related to the amount of dissolved ions.                 |
| 7  | `Organic_carbon`   | ppm         | Amount of organic carbon, from natural or synthetic organic matter.                        |
| 8  | `Trihalomethanes`  | µg/L        | Byproducts of water chlorination, potentially toxic at high concentrations.                |
| 9  | `Turbidity`        | NTU         | Degree of water cloudiness caused by suspended particles.                                  |
| 10 | `Potability`       | Binary      | **Target variable**. Indicates whether the water is potable (`1`) or not potable (`0`).    |

---

### Notes on Data Collection

- The dataset does not include geographic or temporal identifiers, indicating that the data was either **anonymized or simulated** for academic or benchmarking purposes.
- Variable units are standardized according to technical specifications:
  - **ppm** (parts per million)
  - **mg/L** (milligrams per liter)
  - **µg/L** (micrograms per liter)
  - **µS/cm** (microsiemens per centimeter)
  - **NTU** (Nephelometric Turbidity Unit)
- Missing values (`NaN`) are present in some variables and will be handled during preprocessing.
- The target variable (`Potability`) is **binary**, where:
  - `1` → potable water
  - `0` → non-potable water

---

### Identified Potential Challenges

- **Missing values**: Some variables contain missing data, which requires imputation.
- **Class imbalance**: The distribution between potable and non-potable classes may be uneven, affecting model performance.

---

# Part 2.2) Exploratory Data Analysis (EDA)

## 2.2.1) Dataset Overview

![Dataset Overview](assets/images/crisp_dm/2.2.1%20-%20Visão%20geral%20do%20dataset.png)

- The dataset contains **3,276 rows** and **10 columns**.
- Each row represents a **water sample** with physicochemical measurements and the corresponding **potability label** (`0` or `1`).

---

### Initial Observations

- **Missing values**: We can already observe `NaN` values in some columns such as `ph` and `Sulfate`, indicating the need for missing data handling during preprocessing.
- **Data scale**: Some variables have **values with different orders of magnitude**:
  - `Solids`, `Conductivity`, `Sulfate` → very high values
  - `Turbidity`, `ph`, `Organic_carbon` → lower values
  - This **emphasizes the importance of scaling/normalization** before modeling.
- **Target variable (`Potability`)**: All 5 displayed samples have a value of `0`, suggesting that the sample might be **imbalanced** — which will be further investigated in the target distribution analysis.

### Partial Conclusion of the EDA Substage

The dataset overview reveals that the data is **well-structured**, but presents **common real-world challenges**, such as missing values, heterogeneous scales, and potential imbalance. These issues will be addressed in the upcoming stages of the predictive modeling pipeline.

## 2.2.2) Checking Data Types and Missing Values

![Dataset Overview](assets/images/crisp_dm/2.2.10%20-%20KDE%20plots%20(densidade)%20separados%20por%20classe.png)

### Data Structure

- The dataset has **3,276 rows** and **10 columns**.
- All predictor variables are of type `float64`.
- The target variable (`Potability`) is of type `int64`, with binary values (0 or 1).


---

### Missing Values Analysis

| Column            | Missing Values | Percentage (%)             |
|-------------------|----------------|-----------------------------|
| `ph`              | 491            | 14.99% (~15%)               |
| `Sulfate`         | 781            | 23.85% (high)               |
| `Trihalomethanes` | 162            | 4.94% (relatively low)      |
| Other columns     | 0              | —                           |

### Observations:

- **Three columns** contain missing values: `ph`, `Sulfate`, and `Trihalomethanes`.
- Missing data is **concentrated in physicochemical attributes**, possibly due to sensor failures or unperformed measurements.
- Columns such as `Hardness`, `Solids`, `Chloramines`, `Conductivity`, `Organic_carbon`, `Turbidity`, and `Potability` are complete.

---

### Implications for Preprocessing

| Column            | Suggested Imputation Strategy       |
|-------------------|--------------------------------------|
| `ph`              | Impute using the **median**          |
| `Sulfate`         | Impute using the **median**          |
| `Trihalomethanes` | Impute using the **median**          |

> 💡 Since the data is continuous and the percentage of missing values does not exceed 25%, **adding values (imputation) is preferable to dropping rows**.

---

### Insights from the EDA Substage

The missing values analysis shows that the dataset is **mostly complete**, but requires special attention to three columns with missing data. This issue will be addressed in the **data preprocessing stage**, ensuring dataset consistency before modeling.

---

## 2.2.3) Missing Values Visualization

![Dataset Overview](assets/images/crisp_dm/2.2.3%20-%20Visualização%20de%20valores%20ausentes.png)

The image above, generated using the function `missingno.matrix(df)`, provides a **graphical visualization of missing data patterns** in the dataset.

---

### Visual Interpretation

- Columns with **white lines** represent **missing values**.
- Columns with **solid black fill** contain no missing values.
- Three columns have missing data:
  - `ph` (column 0)
  - `Sulfate` (column 4)
  - `Trihalomethanes` (column 8)

---

### Confirmation with Numerical Data

| Column            | Missing Values | % of Total (3,276) |
|-------------------|----------------|--------------------|
| `ph`              | 491            | 14.99%             |
| `Sulfate`         | 781            | 23.85%             |
| `Trihalomethanes` | 162            | 4.94%              |
| Other columns     | 0              | 0%                 |

---

### Key Insights

- **No apparent visual correlation** between missing values across variables: each sample seems to have isolated gaps (not clustered).
- Columns `Hardness`, `Solids`, `Chloramines`, `Conductivity`, `Organic_carbon`, `Turbidity`, and `Potability` are **complete** (100% of values present).
- The missing data is **randomly distributed** across rows, which **suggests MCAR (Missing Completely At Random)** — meaning that the missingness is not dependent on observed data.

---

### 🛠️ Recommended Handling Strategies

> Removing entire rows is not recommended, as it would result in the loss of up to **23.85%** of the dataset, which would harm model learning.

---

### Insights from the EDA Substage

The visualization confirms the previous diagnosis: the dataset contains **missing values located in three specific columns**.
Since the missing data is sparse and relatively low in two variables, and moderate in `Sulfate`, **median imputation** will be applied during preprocessing to preserve data volume and integrity.

---

## 2.2.4) Descriptive Statistics

![Dataset Overview](assets/images/crisp_dm/2.2.4%20-%20Estatísticas%20Descritivas.png)

The table above summarizes the main statistics of central tendency, dispersion, and range for each continuous variable in the dataset.

---

### Insights from the EDA Substage

The descriptive statistics confirm the **need to handle** **missing values**.
Understanding the distribution and limits of variables also helps guide decisions on **feature engineering** and attribute selection in the modeling pipeline.

---

## 2.2.5) Target Variable Distribution

![Dataset Overview](assets/images/crisp_dm/2.2.5%20-%20Distribuição%20da%20variável%20alvo.png)

The target variable `Potability` indicates whether the water is **potable (1)** or **not potable (0)**.

---

### Graph Observations

- The distribution is **asymmetric**:
  - Class `0` (Not Potable): approximately **2,000 samples**
  - Class `1` (Potable): approximately **1,200 samples**

#### Approximate Proportions:
- Class 0 (Not Potable): ~61%
- Class 1 (Potable): ~39%


---

### Implications for Modeling

| Impact                         | Consequence                                                      |
|--------------------------------|------------------------------------------------------------------|
| Imbalanced classes             | Models tend to favor the majority class                         |
| Accuracy can be misleading     | May appear high even with poor performance on the minority class|
| F1-score and AUC more relevant | Metrics like F1, Recall, and ROC AUC should be prioritized       |

---

### Recommended Strategies

1. **Balancing with SMOTE (Synthetic Minority Over-sampling Technique)**
   - Generates synthetic samples of the minority class
   - Preserves the full dataset and improves generalization
   - Ideal before training the model

2. **Additional alternatives (if needed):**
   - Use **Class Weights** in models like `LogisticRegression`, `RandomForestClassifier`, and `XGBoost`

---

### Insights from the EDA Substage

The visualization confirms the **need to handle class imbalance**.
To ensure that the model learns fairly from both classes, the use of **SMOTE (Synthetic Minority Over-sampling Technique)** will be essential in the upcoming preprocessing and modeling stages.

---

## 2.2.6) Percentage Proportion of the Target Class

![Dataset Overview](assets/images/crisp_dm/2.2.6%20-%20Proporção%20percentual%20da%20classe%20alvo.png)

The `Potability` variable represents the model's **target class**, indicating whether a water sample is:
- `0`: **Not Potable**
- `1`: **Potable**

---

### Percentage Distribution

| Class         | Description     | Proportion (%) |
|---------------|------------------|----------------|
| `0`           | Not Potable      | 60.99%         |
| `1`           | Potable          | 39.01%         |


---

### Interpretation

- There is a **moderate imbalance** between the classes.
- The majority class (`0`, not potable) accounts for approximately **61%** of the samples, while the minority class (`1`, potable) represents about **39%**.
- Although not an extreme imbalance, it **can negatively affect model performance**, especially in recall and F1-score for the minority class (`1` – potable water).

---

### Recommended Actions

| Technique                          | Application                                          |
|-----------------------------------|------------------------------------------------------|
| **SMOTE**                         | Synthetically increase the minority class            |

---

### Insights from the EDA Substage

The analysis confirms the class imbalance, with a predominance of non-potable samples.
The use of **class rebalancing techniques** is recommended to avoid prediction bias and ensure a fair and robust model for detecting **potable water**, which is the class of greatest social and public health interest.

---

## 2.2.7) Histograms to Understand Variable Distribution

![Dataset Overview](assets/images/crisp_dm/2.2.7%20-%20Histogramas%20para%20entender%20a%20distribuição%20das%20variáveis.png)

The histograms provide a clear view of the **statistical distribution of continuous variables**.
This step is essential to guide decisions on normalization, transformation, and model selection.

---

### General Observations

- Most variables show an **approximately normal or symmetric distribution**.
- The **absence of significant skewness** indicates that many algorithms, such as Logistic Regression, KNN, and Random Forest, should perform well without additional transformations.
- Variables do not appear to have many extreme outliers, reducing the need for aggressive treatments.

---

### Individual Analysis

| Variable           | Observation                                                  |
|--------------------|--------------------------------------------------------------|
| `ph`               | Slightly symmetric distribution centered around 7            |
| `Hardness`         | Symmetric and well-behaved distribution                      |
| `Solids`           | Symmetric with a slight right tail (mild skew)               |
| `Chloramines`      | Slightly left-skewed, but still acceptable                   |
| `Sulfate`          | Approximates normal, with mild concentration to the right    |
| `Conductivity`     | Slight right skew, no major anomalies                        |
| `Organic_carbon`   | Slightly skewed, centered around 14                          |
| `Trihalomethanes`  | Reasonably symmetric distribution                            |
| `Turbidity`        | Slight concentration between 3 and 4, similar to normal shape|

---

### Insights from the EDA Substage

The variable distributions are suitable for direct use in Machine Learning models.
With **simple standardization**, the data will be ready for algorithms that assume normality.
This analysis reinforces that the dataset is **statistically stable and well-behaved**, with minimal need for complex transformations.

---

## 2.2.8) Boxplots to Detect Outliers

![Dataset Overview](assets/images/crisp_dm/2.2.8%20-%20Boxplots%20para%20detectar%20outliers.png)

In this step, boxplots were used to **compare the distribution of continuous variables** across the target variable `Potability` (0 = Not Potable, 1 = Potable) and to **identify outliers**.

---

### Observations by Variable

| Variable           | Outliers? | Difference Between Classes? | Observations                                                                 |
|--------------------|-----------|------------------------------|------------------------------------------------------------------------------|
| `ph`               | Yes       | Slight                       | Outliers on both sides; potable samples tend to have slightly higher pH.    |
| `Hardness`         | Yes       | Very slight                  | Similar distributions; some high outliers.                                  |
| `Solids`           | Yes       | Virtually none               | Very high outliers; similar distribution between classes.                   |
| `Chloramines`      | Yes       | Slight                       | Potable samples show slightly higher average values.                        |
| `Sulfate`          | Yes       | Slight                       | Potable water tends to have a lower mean and greater spread.                |
| `Conductivity`     | Yes       | Slight                       | Slight increase in the median for potable samples.                          |
| `Organic_carbon`   | Yes       | None                         | Nearly identical distributions.                                             |
| `Trihalomethanes`  | Yes       | None                         | Outliers in both classes; no apparent difference.                           |
| `Turbidity`        | Yes       | Slight                       | Slight median increase in potable samples.                                  |

---

### About the Outliers

- All variables present **visible outliers**.
- Most outliers are **above the upper limit (Q3 + 1.5 * IQR)**.
- The outliers are not extreme enough to compromise modeling, but it is worth considering:
  - **Keeping the outliers**, if plausible (especially for environmental variables).
  - **Robust transformations**, such as `RobustScaler`, if using sensitive models.

---

### Insights from the EDA Substage

The boxplot analysis shows that the dataset contains **outliers in all variables**, but **without severe impact on class separation**.
Differences between classes are **subtle**, meaning the model will need to **combine multiple variables** to achieve good performance — reinforcing the value of **non-linear models** such as **Random Forest** or **XGBoost**.

---

## 2.2.9) Correlation Map Between Variables

![Dataset Overview](assets/images/crisp_dm/2.2.9%20-%20Mapa%20de%20correlação%20entre%20variáveis.png)

The heatmap shown displays **Pearson correlation coefficients** between all variables in the dataset, including the target variable `Potability`.

---

### General Observations

- Most correlations are centered around **0**, indicating that variables are **weakly correlated** with one another.
- This is advantageous for tree-based models (like Random Forest and XGBoost), which are not sensitive to multicollinearity.

---

### Correlation with the Target Variable (`Potability`)

| Variable            | Correlation with `Potability` |
|---------------------|-------------------------------|
| `Solids`            | **+0.03**                     |
| `Chloramines`       | +0.02                         |
| `Trihalomethanes`   | +0.01                         |
| `Hardness`          | -0.01                         |
| `Sulfate`           | -0.02                         |
| `Conductivity`      | -0.01                         |
| `Organic_carbon`    | -0.03                         |
| `Turbidity`         | +0.01                         |
| `ph`                | ≈ 0.00                        |

**Notes:**
- No variable shows strong correlation with the target. This suggests:
  - The **relationship with potability is likely non-linear**;
  - Modeling should consider **combinations and interactions** between variables to achieve good predictive performance.

---

### Correlation Between Predictor Variables

| Variable Pair            | Correlation | Observation                      |
|--------------------------|-------------|----------------------------------|
| `Sulfate` & `Solids`     | **-0.17**   | Mild negative correlation        |
| `ph` & `Solids`          | -0.09       | Weak negative correlation        |
| `ph` & `Hardness`        | +0.08       | Weak positive correlation        |
| Other pairs              | ~0.00 to ±0.05 | Negligible correlation         |

**Notes:**
There is no evidence of multicollinearity, and all variables can be kept in the model without the need for removal due to redundancy.

---

### Implications for Modeling

| Strategy                 | Justification                                          |
|--------------------------|--------------------------------------------------------|
| **Non-linear models**    | Data suggests low linearity with the target variable   |
| **Feature engineering**  | Interactions can improve model performance             |
| **No strong collinearity** | All variables can be used as input                  |

---

### Insights from the EDA Substage

The correlation map shows that the dataset is **statistically stable**, with no problematic collinearity, but also **no variables strongly correlated with water potability**.
This reinforces the importance of using **non-linear and robust models**, as well as combining variables during feature engineering.

---

## 2.2.10) KDE Plots (Density) by Class

![Dataset Overview](assets/images/crisp_dm/2.2.10%20-%20KDE%20plots%20(densidade)%20separados%20por%20classe.png)

In this step, **Kernel Density Estimation (KDE)** plots were used to **visually compare the distribution of continuous variables** between the two classes of the target variable `Potability`:
- **Potable (`1`)** – blue line
- **Not Potable (`0`)** – orange line

---

### Variable-by-Variable Analysis

| Variable           | Difference Between Classes? | Relevant Observations                                                          |
|--------------------|-----------------------------|----------------------------------------------------------------------------------|
| `ph`               | Slight                      | Potable water tends to have a pH closer to 7. Slight visible deviation.         |
| `Hardness`         | Very slight                 | Almost overlapping distributions.                                               |
| `Solids`           | None                        | Nearly identical curves.                                                        |
| `Chloramines`      | Slight                      | Potable water shows a slightly right-shifted distribution.                      |
| `Sulfate`          | Slight                      | Potable water values are slightly more spread.                                  |
| `Conductivity`     | Slight                      | Potable class leans slightly to the right (higher average conductivity).        |
| `Organic_carbon`   | Very slight                 | Potable class distribution is more concentrated around the mean.                |
| `Trihalomethanes`  | None                        | Distributions are nearly identical.                                             |
| `Turbidity`        | Very slight                 | Potable water slightly more concentrated between 3.5 and 4.5 NTU.               |

---

### General Interpretation

- The variables **individually do not provide strong class separability**.
- However, small differences combined across multiple variables may help a non-linear model to **identify effective decision boundaries**.
- **Similar distributions** reinforce that this is a **non-trivial problem**, requiring algorithms capable of capturing complex patterns.

---

### Modeling Implications

| Strategy                           | Justification                                                                  |
|------------------------------------|---------------------------------------------------------------------------------|
| **Ensemble-based models**          | Random Forest or XGBoost can capture interactions between variables             |
| **Feature engineering**            | Creating or crossing variables may reveal hidden patterns                       |
| **Feature selection techniques**   | Evaluate combinations with higher discriminative power                          |
| **Use of PCA (optional)**          | May assist in dimensionality reduction and visualization of potential clusters  |

---

### Insights da subetapa do EDA

Os KDE plots confirmam que as variáveis **não são fortemente discriminatórias de forma isolada**, mas **podem ser valiosas quando combinadas**. A modelagem deve explorar **relações multivariadas** e aplicar algoritmos capazes de **captar interações não lineares**.

---

### Insights from the EDA Substage

The KDE plots confirm that the variables **are not strongly discriminatory in isolation**, but **can be valuable when combined**.
Modeling should explore **multivariate relationships** and apply algorithms capable of **capturing non-linear interactions**.

---

# Part 3) Data Preparation

### 3.1) Handling Missing Values

The first step in data preparation involved identifying and handling missing values in the dataset.
The presence of NaN values can negatively impact machine learning model performance and distort statistical analyses and metrics.
An initial check for missing values per column was performed using the command `df.isnull().sum()`.

To address this issue, **median imputation** was applied to each numerical column using the method `df.fillna(df.median(), inplace=True)`.
This approach is robust against outliers and helps preserve the overall data distribution.
After imputation, it was verified that no missing values remained in the dataset.

### 3.2) Splitting the Data into Training and Testing Sets

With the dataset now complete, the data was split into independent variables (X) and the target variable (y), where the target is the `Potability` column, indicating whether the water is potable (1) or not (0).

The `train_test_split` function from the sklearn library was then used to divide the data into training (80%) and testing (20%) sets.
The parameter `stratify=y` was used to preserve the original class proportions (potable vs. non-potable) in both sets, ensuring a representative split.
Additionally, a seed (`random_state=42`) was set for reproducibility.

### 3.3) Applying SMOTE

Due to the imbalance in the target variable — that is, an unequal distribution between classes — the **SMOTE (Synthetic Minority Over-sampling Technique)** method was applied to generate synthetic samples of the minority class in the training set.

Using SMOTE allows for training more robust models, minimizing bias toward the majority class and improving performance on imbalance-sensitive metrics such as **recall** and **F1-score**.
SMOTE was applied only to the training data (`X_train`, `y_train`) to avoid data leakage and preserve the integrity of the test evaluation.

---

## 4.1) Rationale for Model Testing: Random Forest and XGBoost with Optuna Optimization

---

### Why Random Forest and XGBoost?

### Random Forest Classifier

- A **robust model** based on bagging (bootstrap + decision trees).
- Ideal for data with:
  - Outliers (as seen in the boxplots)
  - Weak correlations between predictors and the target (as seen in the heatmap)
  - Poorly discriminative class distributions (as seen in the KDE plots)
- Performs well even without aggressive normalization.
- **Low risk of overfitting** when properly tuned (number of trees, depth, etc.).

### XGBoost Classifier

- A gradient boosting model that is **highly efficient and accurate**.
- Capable of capturing complex patterns and **non-linear interactions between variables**.
- Works well on **tabular data with imbalanced classes** (as in this project).
- Native support for missing value handling and L1/L2 regularization.
- Often outperforms other tree-based models in structured data benchmarks.

---

### Why Use **Optuna**?

- **Optuna** is a modern hyperparameter optimization library using **intelligent Bayesian search**.
- Unlike exhaustive search (GridSearch) or random search (RandomSearch), Optuna:
  - Reduces computational time.
  - Focuses on the **most promising regions** of the search space.
  - Works well even with limited computational resources.

- For this project, the complexity of tuning hyperparameters for Random Forest and XGBoost makes **Optuna essential to achieve the best possible performance**.

---

### Selected Metric: Accuracy

- **Accuracy** is a useful initial metric for evaluating models in binary classification problems.
- Justifications:
  - The class imbalance is **moderate** (≈ 61% vs 39%), not severe.
  - The metric is **simple to interpret and compare**.
  - It served as a baseline to **compare raw performance between models using the best hyperparameters**.

---

### Observations:

The combined choice of **Random Forest and XGBoost** models, both optimized with **Optuna** and evaluated using **accuracy**, is justified by the problem context:
- Continuous data with low direct correlation to the target variable;
- Subtle differences between class distributions;
- Need for generalization with strong predictive capacity;
- Efficient and automated hyperparameter search using Optuna.

This approach balances **performance, robustness, and interpretability**, making it highly suitable for the **water potability prediction** challenge.

---

### 4.2) Hyperparameter Optimization with Optuna

To ensure the best possible performance of each algorithm, the Optuna library was used for efficient hyperparameter search. Each algorithm had its own objective function defined, with return values based on accuracy over the test set:

* Random Forest: search over `n_estimators`, `max_depth`, `min_samples_split`;

* XGBoost: search over `n_estimators`, `max_depth`, `learning_rate`;

Each study was optimized for 100 iterations (`n_trials=100`), and the best sets of hyperparameters were selected for final model training.

---

# Part 5) Model Evaluation

### 5.1) Model Evaluation

![Dataset Overview](assets/images/crisp_dm/5.1%20-%20Avaliação%20dos%20modelos.png)

After optimization, the Random Forest and XGBoost models were retrained using the best parameters found. Both were evaluated using the following metrics:

* Accuracy
* Precision, Recall, and F1-Score per class
* Weighted and macro averages for overall comparison

| Model          | Accuracy | Precision (Class 1) | Recall (Class 1) | F1-Score (Class 1) |
|----------------|----------|----------------------|-------------------|---------------------|
| Random Forest  | **0.67** | 0.59                 | 0.52              | 0.55                |
| XGBoost        | 0.66     | 0.57                 | 0.54              | 0.56                |

It is observed that the Random Forest model achieved higher overall accuracy (0.67) and better precision when classifying samples as potable.
Although XGBoost achieved a slightly better recall for class 1, Random Forest strikes a better balance between precision and recall, resulting in a competitive F1-Score.

---

### 5.2) Best Model Selection

Based on performance comparison, the **Random Forest model optimized with Optuna** was chosen as the final model for this project.
Despite the close results, its greater ability to generalize to the minority class makes it more suitable for the project’s goal: to identify potable water samples with greater confidence.
