##default by risk score
select 
default_risk_score,
count(*) as total_accounts,
round(avg(default_flag),4) as default_rate
from uci_credit
group by default_risk_score
order by default_risk_score