from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeEmploye(request):
    return render(request,'employes/employes.html')
