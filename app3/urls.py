from django.urls import path
from app3.views import *
app_name = 'app3'

urlpatterns  = [
    path('string/',string,name='string'),
    path('index/',index,name='index'),
    path('home/',home,name='home'),
]