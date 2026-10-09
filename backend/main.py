import io
import sys
import os

import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Get project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add src folder to Python path
SRC_PATH = os.path.join(PROJECT_ROOT, "src")

if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

# Import pipeline modules
from ingestion import load_data
from validation import validate_dataframe, generate_quality_report
from cleaning import clean_data
from transformation import transform_data


app = FastAPI(
    title="Data Processing Pipeline API",
    description="API for processing CSV, JSON and API data.",
    version="1.0.0"
)


# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://data-processessing-pipeline.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class APIRequest(BaseModel):
    url: str


@app.get("/")
def root():
    return {
        "message": "Data Processing Pipeline API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


def process_dataframe(df):
    """
    Run the complete data processing pipeline.
    """

    # Validate input
    validate_dataframe(df)

    # Report before cleaning
    before_report = generate_quality_report(df)

    # Clean data
    cleaned_df = clean_data(df)

    # Transform data
    processed_df = transform_data(cleaned_df)

    # Report after processing
    after_report = generate_quality_report(processed_df)

    # Convert datetime values to JSON-friendly strings
    processed_df = processed_df.copy()

    for column in processed_df.columns:
        if pd.api.types.is_datetime64_any_dtype(processed_df[column]):
            processed_df[column] = processed_df[column].dt.strftime(
                "%Y-%m-%d"
            )

    # Replace NaN with None
    processed_df = processed_df.where(
        pd.notnull(processed_df),
        None
    )

    return {
        "columns": processed_df.columns.tolist(),
        "rows": processed_df.to_dict(orient="records"),
        "before_report": before_report,
        "after_report": after_report
    }


@app.post("/process/file")
async def process_file(file: UploadFile = File(...)):
    """
    Process an uploaded CSV or JSON file.
    """

    try:
        filename = file.filename or ""

        extension = os.path.splitext(filename)[1].lower()

        if extension not in [".csv", ".json"]:
            raise HTTPException(
                status_code=400,
                detail="Only CSV and JSON files are supported."
            )

        contents = await file.read()

        if not contents:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        # Read CSV
        if extension == ".csv":
            df = pd.read_csv(
                io.BytesIO(contents)
            )

        # Read JSON
        else:
            df = pd.read_json(
                io.BytesIO(contents)
            )

        # Process dataset
        result = process_dataframe(df)

        result["source"] = filename

        return result

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/process/api")
async def process_api(request: APIRequest):
    """
    Fetch and process data from an API endpoint.
    """

    try:
        url = request.url.strip()

        if not url.startswith(
            ("http://", "https://")
        ):
            raise HTTPException(
                status_code=400,
                detail="API URL must start with http:// or https://"
            )

        # Load API data
        df = load_data(
            url,
            "api"
        )

        # Process dataset
        result = process_dataframe(df)

        result["source"] = url

        return result

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )