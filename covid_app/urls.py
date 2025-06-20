from django.urls import path
from . import views

urlpatterns = [
    path('', views.covid_report, name='covid_report'),
]
