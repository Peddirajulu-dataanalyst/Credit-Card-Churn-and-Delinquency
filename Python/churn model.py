# ---------------------------------------------------
# Churn Prediction Model (Logistic Regression)
# ---------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score


def train_churn_model(df_churn):

    # -----------------------------
    # Features
    # -----------------------------
    features = [
        "Customer_Age",
        "Months_on_book",
        "Total_Relationship_Count",
        "Months_Inactive_12_mon",
        "Contacts_Count_12_mon",
        "credit_limit",
        "Total_Revolving_Bal",
        "total_spend",
        "transaction_count",
        "Total_Amt_Chng_Q4_Q1",
        "Total_Ct_Chng_Q4_Q1",
        "utilization_ratio"
    ]

    # Target
    target = "churn_flag"

    # -----------------------------
    # Train-Test Split
    # -----------------------------
    X = df_churn[features]
    y = df_churn[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,
        random_state=42
    )

    # -----------------------------
    # Feature Scaling
    # -----------------------------
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # -----------------------------
    # Train Logistic Regression
    # -----------------------------
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_scaled, y_train)

    # -----------------------------
    # Model Evaluation
    # -----------------------------
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]

    print(classification_report(y_test, y_pred))
    print("ROC-AUC:", roc_auc_score(y_test, y_prob))

    # -----------------------------
    # Predict churn probability
    # -----------------------------
    X_all = df_churn[features]
    X_all_scaled = scaler.transform(X_all)

    df_churn["churn_probability"] = model.predict_proba(X_all_scaled)[:, 1]

    # -----------------------------
    # Risk segmentation
    # -----------------------------
    df_churn["churn_risk_band"] = pd.cut(
        df_churn["churn_probability"],
        bins=[0, 0.3, 0.6, 1],
        labels=["Low Risk", "Medium Risk", "High Risk"]
    )

    return df_churn


# -----------------------------
# Example run
# -----------------------------
if __name__ == "__main__":
    print("Churn model module ready.")