from django.urls import path
from app1.views import *
app_name = 'app1'

urlpatterns = [
    path('string/', string, name='string'),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
]