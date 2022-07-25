from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, renderers
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly
from .serializers import prestationSerializer1, PrestationSerializer, UserSerializer, PrestationSerializer2, prestationSerializer5

from .models import Client, Employe, Prestation, NewUser
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

def home(request):
    client = Client.objects.all()
    employe = Employe.objects.all()
    prestation = Prestation.objects.all()
    context={'clients':client, 'employes':employe, 'prestations':prestation}
    return render(request,'acceuil.html',context)


def prestation(request):
    prestation = Prestation.objects.all()
    context ={'prestations':prestation}
    return render(request,'prestations/prestations.html',context)


@api_view(['GET'])
def prestationOverview(request):
    api_url = {
        'List':'prestationAPI-list/',
        'Detail View':'prestationAPI-detail/<str:pk>/',
        'Create': 'addPrestation/',
        'Update':'updatePrestation/<str:pk>/',
        'Delete': 'deletePrestation/<str:pk>/',
    }
    return Response(api_url)
