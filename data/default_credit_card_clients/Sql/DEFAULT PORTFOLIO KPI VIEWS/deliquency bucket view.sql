##delinquency_bucket
create view delinquency_bucket as 
select 
delinquency_bucket,
round(avg(default_flag),4) as default_rate
from uci_credit
group by delinquency_bucket
