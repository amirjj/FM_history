from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Fraud, QueryLog
from datetime import datetime
# Create your views here.
def index(request):
    queries = QueryLog.objects.order_by('query_date')[:1000]
    if request.method == "POST":
        msisdn = request.POST['msisdn']
        QueryLog(username="test", msisdn=msisdn, query_date=datetime.now()).save()
        try:
            result = Fraud.objects.get(msisdn=msisdn)
        except Fraud.DoesNotExist:
            return render(request, 
                'fscheck/index.html', 
                {
                    'searched_msisdn': msisdn,
                    'queries' : queries, 
                    'result' : "No Fraud History."
                })
        return render(request, 
            'fscheck/index.html', 
            {
                'searched_msisdn': msisdn,
                'queries' : queries, 
                'result' : result.fraud_description
            })
    return render(request, 'fscheck/index.html', {
                                    'searched_msisdn': '9336661122',
                                    'queries' : queries,
                                    'result' : "Search Your MSISDN"})
