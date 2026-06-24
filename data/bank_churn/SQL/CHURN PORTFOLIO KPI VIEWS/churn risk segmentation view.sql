##churn risk segmentation view
create view churn_risk_summary as 
select 
risk_score,
count(*) as total_customers,
round(avg(churn_flag),4) as churn_rate
from bank_churn
group by risk_score

select * from churn_risk_summary
select count(customer_id) from bank_churn
select * from uci_credit