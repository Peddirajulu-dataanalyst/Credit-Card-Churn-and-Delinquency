select 
util_band,
count(*) as total_customers,
sum(churn_flag) as churn_customers,
round(sum(churn_flag)*1.0/count(*),4) as churn_rate
from bank_churn
group by util_band