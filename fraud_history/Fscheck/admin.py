from django.contrib import admin
from .models import Fraud, QueryLog

# Register your models here.

class FraudAdmin(admin.ModelAdmin):
    fields = ['msisdn', 'fraud_description', 'still_ongoing']
    list_display = ('msisdn', 'fraud_description', 'still_ongoing')

class QueryLogAdmin(admin.ModelAdmin):
    fields = ['username', 'msisdn', 'query_date']
    list_display = ('username', 'msisdn', 'query_date')


admin.site.register(Fraud, FraudAdmin)
admin.site.register(QueryLog, QueryLogAdmin)
