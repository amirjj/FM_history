from Fscheck.models import Fraud
i = 0
with open("scripts/pan.csv", "r") as f:
    for line in f:
        lc = line.strip().split(",")
        Fraud(msisdn=lc[0], fraud_description=lc[1], still_ongoing=True).save()
        
