-- =====================================================
-- Database Schema
-- Project: Credit Card Churn & Default Risk Analysis
-- Database: MySQL
-- =====================================================

-----------------------------------------------------------------------------------

-- Table: bank_churn
-- Description: Customer credit card churn dataset

-----------------------------------------------------------------------------------

CREATE TABLE bank_churn (
Customer_id INT NOT NULL,
churn_flag TINYINT NOT NULL,
Customer_Age INT DEFAULT NULL,
Gender VARCHAR(10) DEFAULT NULL,
Dependent_count INT DEFAULT NULL,
Education_Level VARCHAR(50) DEFAULT NULL,
Marital_Status VARCHAR(20) DEFAULT NULL,
Income_Category VARCHAR(30) DEFAULT NULL,
Card_Category VARCHAR(30) DEFAULT NULL,
Months_on_book INT DEFAULT NULL,
Total_Relationship_Count INT DEFAULT NULL,
Months_Inactive_12_mon INT DEFAULT NULL,
Contacts_Count_12_mon INT DEFAULT NULL,
credit_limit DECIMAL(12,2) DEFAULT NULL,
Total_Revolving_Bal DECIMAL(12,2) DEFAULT NULL,
Avg_Open_To_Buy DECIMAL(12,2) DEFAULT NULL,
Total_Amt_Chng_Q4_Q1 DECIMAL(10,4) DEFAULT NULL,
total_spend DECIMAL(12,2) DEFAULT NULL,
transaction_count INT DEFAULT NULL,
Total_Ct_Chng_Q4_Q1 DECIMAL(10,4) DEFAULT NULL,
utilization_ratio DECIMAL(10,4) DEFAULT NULL,
high_utilization TINYINT DEFAULT NULL,
spend_drop_flag TINYINT DEFAULT NULL,
inactive_flag TINYINT DEFAULT NULL,
high_inactive_flag TINYINT DEFAULT NULL,
spend_decline_flag TINYINT DEFAULT NULL,
util_band VARCHAR(20) DEFAULT NULL,
risk_score DECIMAL(10,4) DEFAULT NULL,
churn_probability FLOAT DEFAULT NULL,
churn_risk_band VARCHAR(20) DEFAULT NULL,
PRIMARY KEY (Customer_id)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

---------------------------------------------------------------------------------------------------------

-- Table: uci_credit
-- Description: Credit card default prediction dataset

---------------------------------------------------------------------------------------------------------

CREATE TABLE uci_credit (
ID INT NOT NULL,
LIMIT_BAL DECIMAL(12,2) DEFAULT NULL,
SEX TINYINT DEFAULT NULL,
EDUCATION TINYINT DEFAULT NULL,
MARRIAGE TINYINT DEFAULT NULL,
AGE INT DEFAULT NULL,
PAY_0 INT DEFAULT NULL,
PAY_2 INT DEFAULT NULL,
PAY_3 INT DEFAULT NULL,
PAY_4 INT DEFAULT NULL,
PAY_5 INT DEFAULT NULL,
PAY_6 INT DEFAULT NULL,
BILL_AMT1 DECIMAL(14,2) DEFAULT NULL,
BILL_AMT2 DECIMAL(14,2) DEFAULT NULL,
BILL_AMT3 DECIMAL(14,2) DEFAULT NULL,
BILL_AMT4 DECIMAL(14,2) DEFAULT NULL,
BILL_AMT5 DECIMAL(14,2) DEFAULT NULL,
BILL_AMT6 DECIMAL(14,2) DEFAULT NULL,
PAY_AMT1 DECIMAL(14,2) DEFAULT NULL,
PAY_AMT2 DECIMAL(14,2) DEFAULT NULL,
PAY_AMT3 DECIMAL(14,2) DEFAULT NULL,
PAY_AMT4 DECIMAL(14,2) DEFAULT NULL,
PAY_AMT5 DECIMAL(14,2) DEFAULT NULL,
PAY_AMT6 DECIMAL(14,2) DEFAULT NULL,
default_payment_next_month TINYINT DEFAULT NULL,
max_dpd INT DEFAULT NULL,
delinquency_bucket VARCHAR(30) DEFAULT NULL,
default_flag TINYINT DEFAULT NULL,
utilization_ratio DECIMAL(10,4) DEFAULT NULL,
payment_gap DECIMAL(12,2) DEFAULT NULL,
high_util_flag TINYINT DEFAULT NULL,
payment_gap_flag TINYINT DEFAULT NULL,
default_risk_score DECIMAL(10,4) DEFAULT NULL,
default_probability FLOAT DEFAULT NULL,
default_risk_band VARCHAR(20) DEFAULT NULL,
PRIMARY KEY (ID)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;
