select 
delinquency_bucket,
count(*) as total_accounts,
sum(default_flag) as default_accounts,
round(sum(default_flag)*1.0/count(*),4) as default_rate
from uci_credit
group by delinquency_bucket	
order by delinquency_bucket