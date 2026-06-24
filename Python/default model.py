# ---------------------------------------------------
# Default Prediction Model (Logistic Regression)
# ---------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


def train_default_model(df_uci):

    # -----------------------------
    # Features
    # -----------------------------
    features_default = [
        "LIMIT_BAL",
        "AGE",
        "PAY_0",
        "PAY_2",
        "PAY_3",
        "PAY_4",
        "PAY_5",
        "PAY_6",
        "BILL_AMT1",
        "PAY_AMT1",
        "utilization_ratio",
        "max_dpd",
        "payment_gap"
    ]

    # Target
    target_default = "default_flag"

    # -----------------------------
    # Train-Test Split
    # -----------------------------
    X = df_uci[features_default]
    y = df_uci[target_default]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,
        random_state=42
    )

    # -----------------------------
    # Feature Scaling
    # -----------------------------
    scaler_default = StandardScaler()

    X_train_scaled = scaler_default.fit_transform(X_train)
    X_test_scaled = scaler_default.transform(X_test)

    # -----------------------------
    # Train Logistic Regression
    # -----------------------------
    model_default = LogisticRegression(max_iter=1000)
    model_default.fit(X_train_scaled, y_train)

    # -----------------------------
    # Model Evaluation
    # -----------------------------
    y_prob = model_default.predict_proba(X_test_scaled)[:, 1]

    print("ROC-AUC:", roc_auc_score(y_test, y_prob))

    # -----------------------------
    # Feature Importance
    # -----------------------------
    coefficients = pd.DataFrame({
        "Feature": features_default,
        "Coefficient": model_default.coef_[0]
    }).sort_values(by="Coefficient", ascending=False)

    print(coefficients)

    # -----------------------------
    # Predict default probability
    # -----------------------------
    X_all_default = df_uci[features_default]
    X_all_default_scaled = scaler_default.transform(X_all_default)

    df_uci["default_probability"] = model_default.predict_proba(
        X_all_default_scaled
    )[:, 1]

    # -----------------------------
    # Risk segmentation
    # -----------------------------
    df_uci["default_risk_band"] = pd.cut(
        df_uci["default_probability"],
        bins=[0, 0.3, 0.6, 1],
        labels=["Low Risk", "Medium Risk", "High Risk"]
    )

    return df_uci


# -----------------------------
# Example run
# -----------------------------
if __name__ == "__main__":
    print("Default model module ready.")