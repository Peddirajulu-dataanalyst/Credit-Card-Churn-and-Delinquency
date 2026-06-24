##churn by inactiviy band
select 
Months_Inactive_12_Mon,
count(*) as total_customers,
round(avg(churn_flag),4) as churn_rate
from bank_churn
group by Months_Inactive_12_mon
order by Months_Inactive_12_mon