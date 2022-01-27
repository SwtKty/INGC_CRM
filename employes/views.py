from django.shortcuts import render
from django.http import HttpResponse
from employes.models import Employe

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import employeSerializer

# Create your views here.

def homeEmploye(request):
   employe = Employe.objects.all()
   context = {'employes':employe}
   return render(request,'employes/employes.html',context)
