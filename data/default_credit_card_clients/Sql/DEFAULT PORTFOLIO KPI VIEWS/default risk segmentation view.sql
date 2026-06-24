##default risk segmentation view
create view default_risk_summary as 
select
default_risk_score,
count(*) as total_customers,
round(avg(default_flag),4) as default_rate
from uci_credit
group by default_risk_score

select * from default_risk_summary
select * from uci_credit where delinquency_bucket = '3+M Late'
describe default_risk_summary