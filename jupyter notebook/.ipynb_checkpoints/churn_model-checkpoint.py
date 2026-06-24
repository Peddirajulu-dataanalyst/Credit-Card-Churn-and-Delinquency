# ---------------------------------------------------
# Churn Prediction Model (Logistic Regression)
# ---------------------------------------------------

import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, RocCurveDisplay

# Paths
CHURN_FILE = r"D:\python project files\credit card churn and deliquency\data\bank_churn\cleaned\BankChurners.csv"
MODEL_FILE = r"D:\python project files\credit card churn and deliquency\data\bank_churn\model\BankChurners_model.csv"
MODEL_FOLDER = os.path.dirname(MODEL_FILE)
os.makedirs(MODEL_FOLDER, exist_ok=True)

def churn_model():
    # -----------------------------
    # Load cleaned churn data
    # -----------------------------
    df_churn = pd.read_csv(CHURN_FILE)

    # -----------------------------
    # Features & Target
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
    target = "churn_flag"

    # -----------------------------
    # Train-Test Split
    # -----------------------------
    X = df_churn[features]
    y = df_churn[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
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

    # Save ROC curve as PNG
    plt.figure()
    RocCurveDisplay.from_estimator(model, X_test_scaled, y_test)
    plt.title("ROC Curve - Churn Model")
    plt.savefig(os.path.join(MODEL_FOLDER, "roc_curve.png"))
    plt.close()

    # -----------------------------
    # Predict churn probability
    # -----------------------------
    X_all_scaled = scaler.transform(X)
    df_churn["churn_probability"] = model.predict_proba(X_all_scaled)[:, 1]

    # -----------------------------
    # Risk segmentation
    # -----------------------------
    df_churn["churn_risk_band"] = pd.cut(
        df_churn["churn_probability"],
        bins=[0, 0.3, 0.6, 1],
        labels=["Low Risk", "Medium Risk", "High Risk"]
    )

    # -----------------------------
    # Save results
    # -----------------------------
    df_churn.to_csv(MODEL_FILE, index=False)
    print("✅ Churn model results saved:", MODEL_FILE)

    return df_churn

# -----------------------------
# Runner
# -----------------------------
if __name__ == "__main__":
    churn_model()
