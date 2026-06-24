## high default risk accounts
select * from uci_credit where default_risk_score >= 2 ;

select count(*) from bank_churn;
select count(*) from uci_credit