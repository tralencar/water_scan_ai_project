# data_pipeline.py
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split


class DataPipeline:
    """
    Class responsible for loading and cleaning raw data.

    Methods:
        - load_and_clean_data: Reads a CSV file, handles missing values, and returns a cleaned DataFrame.
    """

    def __init__(self, file_path: str):
        """
        Initializes the class with the path to the CSV file.

        Args:
            file_path (str): Full path to the CSV dataset.
        """
        self.file_path = file_path

    def load_and_clean_data(self) -> pd.DataFrame:
        """
        Loads data from the CSV file, prints missing values before and after cleaning,
        replaces missing values with the median of each column, and returns the cleaned DataFrame.

        Returns:
            pd.DataFrame: Cleaned DataFrame ready for preprocessing.
        """
        df = pd.read_csv(self.file_path)
        print('Missing values before treatment:\n', df.isnull().sum())
        df.fillna(df.median(), inplace=True)
        print('Missing values after treatment:\n', df.isnull().sum())
        return df


class DataPreprocessor:
    """
    Class responsible for preprocessing data for machine learning.

    Main functions:
        - split_data: Splits the dataset into training and testing sets.
        - apply_smote: Applies the SMOTE oversampling technique to the training set.
    """

    def __init__(self, df: pd.DataFrame, target: str):
        """
        Initializes the class with the DataFrame and the name of the target column.

        Args:
            df (pd.DataFrame): Cleaned dataset.
            target (str): Name of the column representing the target variable (e.g., 'Potability').
        """
        self.df = df
        self.target = target

    def split_data(self, test_size=0.2, random_state=42):
        """
        Splits the data into training and testing sets while maintaining the target variable proportion.

        Args:
            test_size (float): Proportion of the dataset to include in the test split.
            random_state (int): Seed for reproducibility.

        Returns:
            Tuple: X_train, X_test, y_train, y_test
        """
        X = self.df.drop(columns=[self.target])
        y = self.df[self.target]
        return train_test_split(
            X, y, test_size=test_size, stratify=y, random_state=random_state
        )

    def apply_smote(self, X_train, y_train):
        """
        Applies the SMOTE oversampling technique to balance the classes in the training set.

        Args:
            X_train (DataFrame): Training set features.
            y_train (Series): Training set target variable.

        Returns:
            Tuple: X_train_balanced, y_train_balanced
        """
        over_sampler = SMOTE(random_state=42)
        return over_sampler.fit_resample(X_train, y_train)
