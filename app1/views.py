from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string(request):
    return HttpResponse("string of app1")
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')