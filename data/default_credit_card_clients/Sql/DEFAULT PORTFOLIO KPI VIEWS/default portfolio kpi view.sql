##default portfolio kpi view
create view default_portfolio_kpi as 
select 
count(*) as total_accounts,
sum(default_flag) as default_accounts,
round(avg(default_flag),4) as default_rate,
round(avg(utilization_ratio),4) as avg_utilization,
round(avg(max_dpd),2) as avg_max_dpd
from uci_credit

