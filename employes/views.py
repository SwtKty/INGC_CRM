from django.shortcuts import render
from django.http import HttpResponse
from employes.models import Employe

# Create your views here.

def homeEmploye(request):
   employe = Employe.objects.all()
   context = {'employes':employe}
   return render(request,'employes/employes.html',context)
