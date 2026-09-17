import pandas as pd


def validate_dataframe(df):
    """
    Perform generic validation on the input DataFrame.
    """

    if df is None:
        raise ValueError("Input data is None.")

    if df.empty:
        raise ValueError("Input dataset is empty.")

    if len(df.columns) == 0:
        raise ValueError("Dataset contains no columns.")

    return True


def generate_quality_report(df):
    """
    Generate a basic data quality report.
    """

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_values": int(df.isnull().sum().sum())
    }

    return report