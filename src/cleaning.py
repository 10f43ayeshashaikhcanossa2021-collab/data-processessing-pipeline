import pandas as pd


def clean_data(df):
    """
    Perform generic data cleaning on any dataset.
    """

    df = df.copy()

    # --------------------------------
    # 1. Clean column names
    # --------------------------------

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # --------------------------------
    # 2. Remove completely empty rows
    # --------------------------------

    df = df.dropna(how="all")

    # --------------------------------
    # 3. Remove completely empty columns
    # --------------------------------

    df = df.dropna(axis=1, how="all")

    # --------------------------------
    # 4. Remove duplicate rows
    # --------------------------------

    df = df.drop_duplicates()

    # --------------------------------
    # 5. Clean text columns
    # --------------------------------

    text_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns

    for column in text_columns:

        df[column] = df[column].apply(
            lambda value:
            value.strip()
            if isinstance(value, str)
            else value
        )

    # --------------------------------
    # 6. Detect numeric columns
    # --------------------------------

    for column in df.columns:

        if df[column].dtype == "object":

            converted = pd.to_numeric(
                df[column],
                errors="coerce"
            )

            valid_ratio = converted.notna().mean()

            if valid_ratio >= 0.8:
                df[column] = converted

    # --------------------------------
    # 7. Detect date columns
    # --------------------------------

    for column in df.columns:

        if df[column].dtype == "object":

            converted = pd.to_datetime(
                df[column],
                errors="coerce"
            )

            valid_ratio = converted.notna().mean()

            if valid_ratio >= 0.8:
                df[column] = converted

    # --------------------------------
    # 8. Handle missing values
    # --------------------------------

    for column in df.columns:

        # Numeric columns
        if pd.api.types.is_numeric_dtype(df[column]):

            median_value = df[column].median()

            # Only fill if a valid median exists
            if pd.notna(median_value):

                df[column] = df[column].fillna(
                    median_value
                )

        # Date columns
        elif pd.api.types.is_datetime64_any_dtype(
            df[column]
        ):

            # Keep missing dates as missing
            continue

        # Text / categorical columns
        else:

            df[column] = df[column].fillna(
                "Unknown"
            )

    return df