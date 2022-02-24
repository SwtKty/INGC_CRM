from django.shortcuts import render
from django.http import HttpResponse
from employes.models import Employe

from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import employeSerializer2, employeSerializer1, EmployeRegisterSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.generics import GenericAPIView
from employes.serializers import EmployeRegisterSerializer
from rest_framework import status


# Create your views here.


def homeEmploye(request):
    employe = Employe.objects.all()
    context = {'employes': employe}
    return render(request, 'employes/employes.html', context)


class LoginEmploye(GenericAPIView):
    serializer_class = EmployeRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def employeList(request):
    employes = Employe.objects.all()
    serializer = employeSerializer1(employes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def employeDetail(request, pk):
    employes = Employe.objects.get(id=pk)
    serializer = employeSerializer1(employes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addEmploye(request):
    serializer = employeSerializer2(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def UpdateEmploye(request, pk):
    employes = Employe.objects.get(id=pk)
    serializer = employeSerializer2(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteEmploye(request, pk):
    employes = Employe.objects.get(id=pk)
    employes.delete()
    return Response("Employe succesfully delete!")
