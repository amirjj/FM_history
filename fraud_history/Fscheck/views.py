from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Fraud, QueryLog
from datetime import datetime
# Create your views here.
def index(request):
    queries = QueryLog.objects.order_by('query_date')[:100]
    if request.method == "POST":
        msisdn = request.POST['msisdn']
        if msisdn.startswith("98"):
            msisdn = msisdn[2:]
        elif msisdn.startswith("0"):
            msisdn = msisdn[1:]
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


def error_404_view(request, exception):
       
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')