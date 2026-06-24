# ---------------------------------------------------
# Data loading and cleaning for churn & credit default
# ---------------------------------------------------

import pandas as pd
import numpy as np
import os

# Paths
CHURN_RAW   = r"D:\python project files\credit card churn and deliquency\data\bank_churn\raw\BankChurners.csv"
CREDIT_RAW  = r"D:\python project files\credit card churn and deliquency\data\default_credit_card_clients\raw\default_credit_card_clients.csv"

CHURN_CLEAN = r"D:\python project files\credit card churn and deliquency\data\bank_churn\cleaned\BankChurners.csv"
CREDIT_CLEAN= r"D:\python project files\credit card churn and deliquency\data\default_credit_card_clients\cleaned\default_credit_card_clients.csv"

# Ensure cleaned folder exists
CLEAN_FOLDER = os.path.dirname(CHURN_CLEAN)
os.makedirs(CLEAN_FOLDER, exist_ok=True)

# -----------------------------
# Clean churn dataset
# -----------------------------
def clean_churn_data(file_path):
    df_churn = pd.read_csv(file_path)

    # Rename columns
    df_churn = df_churn.rename(columns={
        "CLIENTNUM": "Customer_id",
        "Attrition_Flag": "churn_flag",
        "Credit_Limit": "credit_limit",
        "Avg_Utilization_Ratio": "utilization_ratio",
        "Total_Trans_Amt": "total_spend",
        "Total_Trans_Ct": "transaction_count"
    })

    # Convert churn flag to numeric
    df_churn["churn_flag"] = df_churn["churn_flag"].map({
        "Existing Customer": 0,
        "Attrited Customer": 1
    })

    # Behavioral metrics
    df_churn["high_utilization"] = df_churn["utilization_ratio"] > 0.8
    df_churn["spend_drop_flag"] = df_churn["Total_Amt_Chng_Q4_Q1"] < 0.8
    df_churn["inactive_flag"] = df_churn["Months_Inactive_12_mon"] > 3

    # Add time simulation (portfolio monitoring)
    df_churn["report_month"] = np.random.choice(
        ["Jan","Feb","Mar","Apr","May","Jun"],
        size=len(df_churn)
    )

    # Extra cleaning checks
    df_churn = df_churn.drop_duplicates()
    df_churn = df_churn.dropna(subset=["Customer_id","credit_limit","utilization_ratio"])
    df_churn["utilization_ratio"] = df_churn["utilization_ratio"].clip(lower=0, upper=1)

    return df_churn

# -----------------------------
# Clean credit dataset
# -----------------------------
def clean_credit_data(file_path):
    df_uci = pd.read_csv(file_path)

    # Maximum Days Past Due
    df_uci["max_dpd"] = df_uci[
        ["PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6"]
    ].max(axis=1)

    # Delinquency bucket
    df_uci["delinquency_bucket"] = pd.cut(
        df_uci["max_dpd"],
        bins=[-2, 0, 1, 2, 10],
        labels=["Current", "1M Late", "2M Late", "3+M Late"]
    )

    # Default flag
    df_uci["default_flag"] = df_uci["default payment next month"]

    # Utilization proxy
    df_uci["utilization_ratio"] = df_uci["BILL_AMT1"] / df_uci["LIMIT_BAL"]

    # Add time simulation (portfolio monitoring)
    df_uci["report_month"] = np.random.choice(
        ["Jan","Feb","Mar","Apr","May","Jun"],
        size=len(df_uci)
    )

    # Extra cleaning checks
    df_uci = df_uci.drop_duplicates()
    df_uci = df_uci.dropna(subset=["LIMIT_BAL","BILL_AMT1"])
    df_uci["utilization_ratio"] = df_uci["utilization_ratio"].clip(lower=0)

    return df_uci

# -----------------------------
# Main pipeline
# -----------------------------
def clean_data():
    # Churn
    df_churn = clean_churn_data(CHURN_RAW)
    df_churn.to_csv(CHURN_CLEAN, index=False)
    print("✅ Cleaned churn dataset saved:", CHURN_CLEAN)

    # Credit default
    df_uci = clean_credit_data(CREDIT_RAW)
    df_uci.to_csv(CREDIT_CLEAN, index=False)
    print("✅ Cleaned credit dataset saved:", CREDIT_CLEAN)

    print("🎯 Pipeline finished successfully.")

# Runner
if __name__ == "__main__":
    clean_data()
