import pandas as pd
import requests


def read_csv(file_path):
    """
    Read data from a CSV file.
    """
    return pd.read_csv(file_path)


def read_json(file_path):
    """
    Read data from a JSON file.
    """
    return pd.read_json(file_path)


def read_api(url):
    """
    Read JSON data from an API.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return pd.DataFrame(response.json())


def load_data(source, source_type="csv"):
    """
    Load data based on the source type.
    """

    if source_type == "csv":
        return read_csv(source)

    elif source_type == "json":
        return read_json(source)

    elif source_type == "api":
        return read_api(source)

    else:
        raise ValueError(f"Unsupported source type: {source_type}")