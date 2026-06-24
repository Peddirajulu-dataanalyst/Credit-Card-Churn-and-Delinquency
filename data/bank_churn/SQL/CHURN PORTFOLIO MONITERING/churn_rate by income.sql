select 	
Income_category,
count(*) as total_customers,
round(avg(churn_flag),4) as churn_rate
from bank_churn
group by Income_Category
order by churn_rate DESC