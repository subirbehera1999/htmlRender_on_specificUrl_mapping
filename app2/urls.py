from django.urls import path
from app2.views import *
app_name = 'app2'

urlpatterns = [
    path('string/',string, name='string'),
    path('index/',index,name='index'),
    path('home/',home,name='home'),
]