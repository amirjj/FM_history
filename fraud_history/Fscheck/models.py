from pyexpat import model
from statistics import mode
from django.db import models

class Fraud(models):
    msisdn = models.CharField(max_length=12)
    fraud_description = models.CharField(max_length=5000)
    still_ongoing = models.BooleanField()


class QueryLog(models):
    usernamme = models.EmailField()
    msisdn = models.CharField(max_length=12)
