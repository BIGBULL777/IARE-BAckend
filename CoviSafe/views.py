from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from IARE.seralizers import *
from django.http import HttpResponse
# from django.contrib.auth import authnticate,login,logout

# Create your views here.


def home_api(APIView):
    def get(self,request):
        hospi = hospital.objects.all()
        serializer = hospitalSerializer(hospi,many = True)
        return HttpResponse(serializer.data,{})
