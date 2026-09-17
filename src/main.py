from config import load_config
from logger import setup_logger
from ingestion import load_data
from validation import validate_dataframe, generate_quality_report
from cleaning import clean_data
from transformation import transform_data


def main():

    # Load configuration
    config = load_config()

    # Setup logger
    logger = setup_logger(config["log_file"])

    logger.info("Pipeline started")

    try:

        # -------------------------------
        # 1. Load data
        # -------------------------------

        logger.info("Loading input data")

        df = load_data(
            config["input_file"],
            config["input_type"]
        )

        logger.info(
            f"Loaded {len(df)} rows and {len(df.columns)} columns"
        )

        # -------------------------------
        # 2. Validate data
        # -------------------------------

        logger.info("Validating dataset")

        validate_dataframe(df)

        logger.info("Validation successful")

        # -------------------------------
        # 3. Generate input quality report
        # -------------------------------

        before_report = generate_quality_report(df)

        logger.info(
            f"Input quality report: {before_report}"
        )

        # -------------------------------
        # 4. Clean data
        # -------------------------------

        logger.info("Cleaning data")

        before_rows = len(df)

        df = clean_data(df)

        after_rows = len(df)

        logger.info(
            f"Cleaning completed. "
            f"Rows before: {before_rows}, "
            f"Rows after: {after_rows}"
        )

        # -------------------------------
        # 5. Transform data
        # -------------------------------

        logger.info("Transforming data")

        df = transform_data(df)

        logger.info("Transformation completed")

        # -------------------------------
        # 6. Save output
        # -------------------------------

        df.to_csv(
            config["output_file"],
            index=False
        )

        logger.info(
            f"Output saved to {config['output_file']}"
        )

        # -------------------------------
        # 7. Final quality report
        # -------------------------------

        final_report = generate_quality_report(df)

        logger.info(
            f"Final quality report: {final_report}"
        )

        logger.info("Pipeline completed successfully")

        print("\nPipeline completed successfully!")
        print("-------------------------------")
        print(f"Input rows       : {before_rows}")
        print(f"Output rows      : {after_rows}")
        print(f"Output columns   : {len(df.columns)}")
        print(
            f"Output file      : {config['output_file']}"
        )
        print("-------------------------------")

    except Exception as error:

        logger.exception(
            f"Pipeline failed: {error}"
        )

        print(f"\nPipeline failed: {error}")


if __name__ == "__main__":
    main()