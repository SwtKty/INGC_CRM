from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from .serializers import prestationSerializer3, prestationSerializer1, PrestationSerializer

from clients.models import Client
from employes.models import Employe
from prestations.models import Prestation


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


@api_view(['GET'])
def prestationList(request):
    prestations = Prestation.objects.all()
    serializer = prestationSerializer1(prestations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def prestationDetail(request, pk):
    prestations = Prestation.objects.get(id=pk)
    serializer = prestationSerializer1(prestations, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addPrestation(request):
    serializer = PrestationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def UpdatePrestation(request, pk):
    prestations = Prestation.objects.get(id=pk)
    serializer = PrestationSerializer(instance=prestations,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def DeletePrestation(request, pk):
    prestations = Prestation.objects.get(id=pk)
    prestations.delete()
    return Response("Prestation succesfully delete!")


class PrestationList(generics.ListCreateAPIView):
    queryset = Prestation.objects.all()
    serializer_class = PrestationSerializer


class PrestationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestation.objects.all()
    serializer_class = PrestationSerializer

