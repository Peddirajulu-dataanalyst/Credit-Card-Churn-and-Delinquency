# ---------------------------------------------------
# Master Pipeline Runner
# ---------------------------------------------------

import logging
import os

# Import functions from your modules
from Data_generation import generate_customers, generate_products, generate_orders, generate_returns
from Data_Cleaning import clean_data
from eda_analysis import run_eda
from feature_engineering import run_feature_engineering
from churn_model import churn_model
from credit_model import credit_model

# Configure logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("🚀 Pipeline Started")

    # -----------------------------
    # Data Generation
    # -----------------------------
    generate_customers()
    logging.info("Customers generated")

    generate_products()
    logging.info("Products generated")

    generate_orders()
    logging.info("Orders generated")

    generate_returns()
    logging.info("Returns generated")

    # -----------------------------
    # Data Cleaning
    # -----------------------------
    clean_data()
    logging.info("Data cleaning completed")

    # -----------------------------
    # Exploratory Data Analysis
    # -----------------------------
    run_eda()
    logging.info("EDA completed")

    # -----------------------------
    # Feature Engineering
    # -----------------------------
    run_feature_engineering()
    logging.info("Feature engineering completed")

    # -----------------------------
    # Churn Model
    # -----------------------------
    churn_model()
    logging.info("Churn model completed")

    # -----------------------------
    # Credit Default Model
    # -----------------------------
    credit_model()
    logging.info("Credit default model completed")

    logging.info("✅ Pipeline Finished Successfully")
    print("Project completed successfully")

# -----------------------------
# Runner
# -----------------------------
if __name__ == "__main__":
    main()
