from pyexpat import model
from statistics import mode
from django.db import models

class Fraud(models.Model):
    msisdn = models.CharField(max_length=12)
    fraud_description = models.TextField()
    still_ongoing = models.BooleanField()

    def __str__(self):
        return self.msisdn
        

class QueryLog(models.Model):
    username = models.EmailField()
    msisdn = models.CharField(max_length=12)
    query_date = models.DateTimeField("date queried")

    def __str__(self):
        return self.username

