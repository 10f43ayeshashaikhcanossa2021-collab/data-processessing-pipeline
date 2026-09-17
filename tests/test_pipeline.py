import pandas as pd

from src.cleaning import clean_data
from src.transformation import transform_data


def test_missing_customer():

    df = pd.DataFrame({
        "order_id": [1],
        "customer_name": [None],
        "product": ["Laptop"],
        "quantity": [2],
        "price": [50000],
        "order_date": ["2026-01-01"],
        "city": ["Mumbai"]
    })

    result = clean_data(df)

    assert result.iloc[0]["customer_name"] == "Unknown"


def test_total_amount():

    df = pd.DataFrame({
        "quantity": [2],
        "price": [1000],
        "order_date": pd.to_datetime(
            ["2026-01-01"]
        )
    })

    result = transform_data(df)

    assert result.iloc[0]["total_amount"] == 2000