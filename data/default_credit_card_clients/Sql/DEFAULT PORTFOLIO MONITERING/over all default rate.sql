##over all default rate
select 
count(*) as total_accounts,
sum(default_flag) as default_accounts,
round(avg(default_flag),4) as default_rate
from uci_credit