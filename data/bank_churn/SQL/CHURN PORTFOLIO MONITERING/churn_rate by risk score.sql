##churn rate by risk score
select 
risk_score,
count(*) as total_customers,
round(avg(churn_flag),4) as churn_rate
from bank_churn
group by risk_score
order by risk_score