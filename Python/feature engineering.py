# ---------------------------------------------------
# Feature Engineering + Risk Segmentation
# ---------------------------------------------------

import pandas as pd


# -----------------------------
# Churn Feature Engineering
# -----------------------------
def churn_feature_engineering(df_churn):

    # Create inactivity risk flag
    df_churn["high_inactive_flag"] = df_churn["Months_Inactive_12_mon"] >= 3

    # Create spend decline flag
    df_churn["spend_decline_flag"] = df_churn["Total_Amt_Chng_Q4_Q1"] < 0.8

    # Create utilization band
    df_churn["util_band"] = pd.cut(
        df_churn["utilization_ratio"],
        bins=[0, 0.2, 0.5, 0.8, 1],
        labels=["Very Low", "Low", "Medium", "High"]
    )

    # Create simple churn risk score
    df_churn["risk_score"] = (
        df_churn["high_inactive_flag"].astype(int)
        + df_churn["spend_decline_flag"].astype(int)
    )

    return df_churn


# -----------------------------
# Default Risk Feature Engineering
# -----------------------------
def default_feature_engineering(df_uci):

    # Create high utilization flag
    df_uci["high_util_flag"] = df_uci["utilization_ratio"] > 0.8

    # Create payment stress flag
    df_uci["payment_gap_flag"] = df_uci["payment_gap"] > 0

    # Create default risk score
    df_uci["default_risk_score"] = (
        (df_uci["max_dpd"] >= 2).astype(int)
        + df_uci["high_util_flag"].astype(int)
        + df_uci["payment_gap_flag"].astype(int)
    )

    # Rename column for consistency
    df_uci.rename(
        columns={"default payment next month": "default_payment_next_month"},
        inplace=True
    )

    return df_uci


# -----------------------------
# Example run
# -----------------------------
if __name__ == "__main__":

    print("Feature engineering module ready.")