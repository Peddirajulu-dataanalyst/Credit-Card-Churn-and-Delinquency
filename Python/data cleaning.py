# ---------------------------------------------------
# Data loading and cleaning for churn & credit default
# ---------------------------------------------------

import pandas as pd


# -----------------------------
# Load churn dataset
# -----------------------------
def load_churn_data(file_path):
    df_churn = pd.read_csv(file_path)
    return df_churn


# -----------------------------
# Clean churn dataset
# -----------------------------
def clean_churn_data(df_churn):

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

    return df_churn


# -----------------------------
# Load credit default dataset
# -----------------------------
def load_credit_data(file_path):
    df_uci = pd.read_csv(file_path)
    return df_uci


# -----------------------------
# Clean credit dataset
# -----------------------------
def clean_credit_data(df_uci):

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

    return df_uci


# -----------------------------
# Example run
# -----------------------------
if __name__ == "__main__":

    churn_file = "data/archive/BankChurners.csv"
    credit_file = "data/default_credit_card_clients/default_credit_card_clients.csv"

    df_churn = load_churn_data(churn_file)
    df_churn = clean_churn_data(df_churn)

    df_uci = load_credit_data(credit_file)
    df_uci = clean_credit_data(df_uci)

    print("Churn data shape:", df_churn.shape)
    print("Credit data shape:", df_uci.shape)