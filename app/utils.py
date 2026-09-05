import pandas as pd
from pandas import DataFrame


def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame"""

    data = pd.read_csv(file_path)
    return data


def clean_data(data: DataFrame):
    """
    Checks and handles discrepancies in the data
    """

    # Drop completely empty rows
    new_data = data.dropna(how="all")

    # Remove duplicate rows
    deduplicated_data = new_data.drop_duplicates()

    return deduplicated_data