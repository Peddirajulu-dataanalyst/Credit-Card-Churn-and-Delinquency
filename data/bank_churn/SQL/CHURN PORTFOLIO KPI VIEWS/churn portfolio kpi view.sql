##churn protfolio kpi view
create view churn_portfolio_kpi as 
select 
count(*) as total_customers,
sum(churn_flag) as churn_customers,
round(avg(churn_flag),4) as churn_rate,
round(avg(utilization_ratio),4) as avg_utilization,
round(avg(Months_Inactive_12_mon),2) as avg_inactive_months
from bank_churn