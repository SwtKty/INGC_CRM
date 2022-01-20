from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'acceuil.html')

def prestation(request):
    return render(request,'prestations/prestations.html')
