##default rate by dpd bucket
select 
delinquency_bucket,
count(*) as total_accounts,
round(avg(default_flag),4) as default_rate
from uci_credit
group by delinquency_bucket
order by delinquency_bucket