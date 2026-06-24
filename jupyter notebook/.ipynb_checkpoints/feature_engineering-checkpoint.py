# ---------------------------------------------------
# Feature Engineering + Risk Segmentation
# ---------------------------------------------------

import pandas as pd
import numpy as np
import os

# Paths
CHURN_FILE   = r"D:\python project files\credit card churn and deliquency\data\bank_churn\cleaned\BankChurners.csv"
CREDIT_FILE  = r"D:\python project files\credit card churn and deliquency\data\default_credit_card_clients\cleaned\default of credit card clients.csv"

CHURN_PROCESSED_FOLDER  = r"D:\python project files\credit card churn and deliquency\data\bank_churn\processed"
CREDIT_PROCESSED_FOLDER = r"D:\python project files\credit card churn and deliquency\data\default_credit_card_clients\Processed"

# Ensure folders exist
os.makedirs(CHURN_PROCESSED_FOLDER, exist_ok=True)
os.makedirs(CREDIT_PROCESSED_FOLDER, exist_ok=True)

def run_feature_engineering():
    # -----------------------------
    # Load datasets
    # -----------------------------
    df_churn = pd.read_csv(CHURN_FILE)
    df_uci   = pd.read_csv(CREDIT_FILE)

    # -----------------------------
    # Churn Feature Engineering
    # -----------------------------
    # Inactivity risk flag
    df_churn["high_inactive_flag"] = df_churn["Months_Inactive_12_mon"] >= 3

    # Spend decline flag
    df_churn["spend_decline_flag"] = df_churn["Total_Amt_Chng_Q4_Q1"] < 0.8

    # Utilization band
    df_churn["util_band"] = pd.cut(
        df_churn["utilization_ratio"],
        bins=[0, 0.2, 0.5, 0.8, 1],
        labels=["Very Low", "Low", "Medium", "High"]
    )

    # Risk score (simple additive)
    df_churn["risk_score"] = (
        df_churn["high_inactive_flag"].astype(int) +
        df_churn["spend_decline_flag"].astype(int)
    )

    # -----------------------------
    # Credit Default Feature Engineering
    # -----------------------------
    # High utilization flag
    df_uci["high_util_flag"] = df_uci["utilization_ratio"] > 0.8

    # Payment stress flag
    df_uci["payment_gap_flag"] = df_uci["payment_gap"] > 0

    # Default risk score
    df_uci["default_risk_score"] = (
        (df_uci["max_dpd"] >= 2).astype(int) +
        df_uci["high_util_flag"].astype(int) +
        df_uci["payment_gap_flag"].astype(int)
    )

    # Rename target column for clarity
    df_uci.rename(columns={"default payment next month": "default_payment_next_month"}, inplace=True)

    # -----------------------------
    # Save processed files
    # -----------------------------
    churn_out = os.path.join(CHURN_PROCESSED_FOLDER, "BankChurners_processed.csv")
    credit_out = os.path.join(CREDIT_PROCESSED_FOLDER, "default_credit_card_clients_processed.csv")

    df_churn.to_csv(churn_out, index=False)
    df_uci.to_csv(credit_out, index=False)

    print("✅ Feature engineering completed.")
    print("Churn processed file saved:", churn_out)
    print("Credit processed file saved:", credit_out)

    return df_churn, df_uci

# -----------------------------
# Runner
# -----------------------------
if __name__ == "__main__":
    run_feature_engineering()
