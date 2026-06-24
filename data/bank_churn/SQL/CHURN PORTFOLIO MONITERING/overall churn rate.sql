## overall portfolio churn rate 
select 
count(*) as total_customers,
sum(churn_flag) as churn_customers,
round(avg(churn_flag),4) as churn_rate
from bank_churn
