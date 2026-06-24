# ---------------------------------------------------
# Churn & Default EDA Pipeline
# ---------------------------------------------------

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Paths
CHURN_FILE = r"D:\python project files\credit card churn and deliquency\data\bank_churn\cleaned\BankChurners.csv"
CREDIT_FILE = r"D:\python project files\credit card churn and deliquency\data\default_credit_card_clients\cleaned\default of credit card clients.csv"

CHURN_EDA_FOLDER = r"D:\python project files\credit card churn and deliquency\data\bank_churn\eda"
CREDIT_EDA_FOLDER = r"D:\python project files\credit card churn and deliquency\data\default_credit_card_clients\eda"

# Ensure folders exist
os.makedirs(CHURN_EDA_FOLDER, exist_ok=True)
os.makedirs(CREDIT_EDA_FOLDER, exist_ok=True)

def run_eda():
    # -----------------------------
    # Load datasets
    # -----------------------------
    df_churn = pd.read_csv(CHURN_FILE)
    df_uci   = pd.read_csv(CREDIT_FILE)

    # -----------------------------
    # Churn EDA
    # -----------------------------
    print("Churn dataset shape:", df_churn.shape)
    print(df_churn.info())
    print(df_churn.describe())

    # Convert churn flag
    df_churn["churn_flag"] = df_churn["Attrition_Flag"].map({
        "Existing Customer": 0,
        "Attrited Customer": 1
    })
    print("Churn rate:", df_churn["churn_flag"].mean())

    # Spend vs churn
    plt.figure()
    sns.boxplot(x="churn_flag", y="total_spend", data=df_churn)
    plt.title("Spend vs Churn")
    plt.savefig(os.path.join(CHURN_EDA_FOLDER, "spend_vs_churn.png"))
    plt.close()

    # Utilization vs churn
    plt.figure()
    sns.boxplot(x="churn_flag", y="utilization_ratio", data=df_churn)
    plt.title("Utilization vs Churn")
    plt.savefig(os.path.join(CHURN_EDA_FOLDER, "utilization_vs_churn.png"))
    plt.close()

    # Inactivity vs churn
    plt.figure()
    sns.barplot(x="Months_Inactive_12_mon", y="churn_flag", data=df_churn)
    plt.title("Inactivity vs Churn")
    plt.savefig(os.path.join(CHURN_EDA_FOLDER, "inactivity_vs_churn.png"))
    plt.close()

    # Spend change signal
    plt.figure()
    sns.boxplot(x="churn_flag", y="Total_Amt_Chng_Q4_Q1", data=df_churn)
    plt.title("Spend Change vs Churn")
    plt.savefig(os.path.join(CHURN_EDA_FOLDER, "spend_change_vs_churn.png"))
    plt.close()

    # -----------------------------
    # Credit Default EDA
    # -----------------------------
    print("Credit dataset shape:", df_uci.shape)
    print(df_uci.info())
    print(df_uci.describe())

    print("Default rate:", df_uci["default payment next month"].mean())

    # DPD vs Default
    plt.figure()
    sns.barplot(x="max_dpd", y="default payment next month", data=df_uci)
    plt.title("DPD vs Default")
    plt.savefig(os.path.join(CREDIT_EDA_FOLDER, "dpd_vs_default.png"))
    plt.close()

    # Utilization vs Default
    plt.figure()
    sns.boxplot(x="default payment next month", y="utilization_ratio", data=df_uci)
    plt.title("Utilization vs Default")
    plt.savefig(os.path.join(CREDIT_EDA_FOLDER, "utilization_vs_default.png"))
    plt.close()

    # Payment gap vs Default
    df_uci["payment_gap"] = df_uci["BILL_AMT1"] - df_uci["PAY_AMT1"]
    plt.figure()
    sns.boxplot(x="default payment next month", y="payment_gap", data=df_uci)
    plt.title("Payment Gap vs Default")
    plt.savefig(os.path.join(CREDIT_EDA_FOLDER, "payment_gap_vs_default.png"))
    plt.close()

    print("✅ EDA completed. Plots saved in churn & credit EDA folders.")

# -----------------------------
# Runner
# -----------------------------
if __name__ == "__main__":
    run_eda()
