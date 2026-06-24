# ---------------------------------------------------
# Default Prediction Model (Logistic Regression)
# ---------------------------------------------------

import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, RocCurveDisplay, confusion_matrix
import seaborn as sns

# Paths
CREDIT_FILE = r"D:\python project files\credit card churn and deliquency\data\default_credit_card_clients\cleaned\default of credit card clients.csv"
MODEL_FILE  = r"D:\python project files\credit card churn and deliquency\data\default_credit_card_clients\model\credit_model.csv"
MODEL_FOLDER = os.path.dirname(MODEL_FILE)
os.makedirs(MODEL_FOLDER, exist_ok=True)

def credit_model():
    # -----------------------------
    # Load cleaned credit data
    # -----------------------------
    df_uci = pd.read_csv(CREDIT_FILE)

    # -----------------------------
    # Features & Target
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
    target_default = "default_flag"

    # -----------------------------
    # Train-Test Split
    # -----------------------------
    X = df_uci[features_default]
    y = df_uci[target_default]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # -----------------------------
    # Feature Scaling
    # -----------------------------
    scaler_default = StandardScaler()
    X_train_scaled = scaler_default.fit_transform(X_train)
    X_test_scaled  = scaler_default.transform(X_test)

    # -----------------------------
    # Train Logistic Regression
    # -----------------------------
    model_default = LogisticRegression(max_iter=1000)
    model_default.fit(X_train_scaled, y_train)

    # -----------------------------
    # Model Evaluation
    # -----------------------------
    y_pred = model_default.predict(X_test_scaled)
    y_prob = model_default.predict_proba(X_test_scaled)[:, 1]

    print("ROC-AUC:", roc_auc_score(y_test, y_prob))

    # Save ROC curve as PNG
    plt.figure()
    RocCurveDisplay.from_estimator(model_default, X_test_scaled, y_test)
    plt.title("ROC Curve - Default Model")
    plt.savefig(os.path.join(MODEL_FOLDER, "roc_curve_default.png"))
    plt.close()

    # Save confusion matrix as PNG
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix - Default Model")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.savefig(os.path.join(MODEL_FOLDER, "confusion_matrix_default.png"))
    plt.close()

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

    # -----------------------------
    # Save results
    # -----------------------------
    df_uci.to_csv(MODEL_FILE, index=False)
    print("✅ Default model results saved:", MODEL_FILE)

    return df_uci

# -----------------------------
# Runner
# -----------------------------
if __name__ == "__main__":
    credit_model()
