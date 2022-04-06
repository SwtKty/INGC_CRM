from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from prestations.serializers import PrestationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import prestationSerializer3, prestationSerializer1, prestationSerializer2

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
    serializer = prestationSerializer2(instance=prestations,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def DeletePrestation(request, pk):
    prestations = Prestation.objects.get(id=pk)
    prestations.delete()
    return Response("Prestation succesfully delete!")


@api_view(['GET', 'PUT', ])
def prestations_list(request):
    if request.method == 'GET':
        prestations = Prestation.objects.all()
        serializer = PrestationSerializer(prestations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = PrestationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def prestations_detail(request, pk):
    try:
        prestations = Prestation.objects.get(pk=pk)
    except Prestation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PrestationSerializer(prestations)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PrestationSerializer(prestations, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        prestations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

