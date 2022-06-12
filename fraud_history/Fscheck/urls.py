from argparse import Namespace
from django.urls import URLPattern
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
]
