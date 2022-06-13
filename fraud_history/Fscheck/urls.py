from argparse import Namespace
from django.urls import URLPattern
from . import views
from django.urls import path
from django.conf.urls import handler404


urlpatterns = [
    path('', views.index, name='index'),
]

handler404 = 'Fscheck.views.error_404_view'
