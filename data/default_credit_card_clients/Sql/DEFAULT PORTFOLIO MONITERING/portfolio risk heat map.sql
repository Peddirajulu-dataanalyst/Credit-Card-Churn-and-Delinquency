select 
delinquency_bucket,
case when utilization_ratio < 0.3 then 'low'
     when utilization_ratio < 0.7 then 'medium'
     else 'high'
     end as util_band,
count(*) as total_accounts,
round(avg(default_flag),4) as default_rate
from uci_credit
group by delinquency_bucket,util_band
order by delinquency_bucket,util_band
