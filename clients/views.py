from django.shortcuts import render
from django.http import HttpResponse
from clients.models import Client


# Create your views here.

def homeClient(request):
    client = Client.objects.all()
    context = {'clients':client}
    return render(request,'clients/clients.html',context)
