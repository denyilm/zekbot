from os import kill, system
import subprocess
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from subprocess import Popen, run,PIPE
import sys

from .models import Eth, Shib
from .serializers import EthSerializer, ShibSerializer

from django.core.files.storage import default_storage
from django.utils.crypto import get_random_string

# Create your views here.
@csrf_exempt
def EthApi(request, id=-1):
    if request.method=='GET':
        eth=Eth.objects.all().order_by('id')
        eth_s=EthSerializer(eth,many=True)
        return  JsonResponse(eth_s.data, safe=False)
    if request.method=='POST':
        eth_data=JSONParser().parse(request)
        eth_s=EthSerializer(data=eth_data)
        if eth_s.is_valid():
            eth_s.save()
            return JsonResponse("ADDED",safe=False)
        return JsonResponse(eth_s.errors, safe=False)
    if request.method=='DELETE':
        Eth.objects.all().delete()
        return JsonResponse('DELETED',safe=False)

@csrf_exempt
def ShibApi(request, id=-1):
    if request.method=='GET':
        shib=Shib.objects.all()
        shib_s=ShibSerializer(shib,many=True)
        return  JsonResponse(shib_s.data, safe=False)
    if request.method=='POST':
        shib_data=JSONParser().parse(request)
        shib_s=ShibSerializer(data=shib_data)
        if shib_s.is_valid():
            shib_s.save()
            return JsonResponse("ADDED",safe=False)
        return JsonResponse(shib_s.errors, safe=False)
    if request.method=='DELETE':
        Shib.objects.all().delete()
        return JsonResponse('DELETED',safe=False)

@csrf_exempt
def EthSocketApi(request, id=-1):
    if request.method=='GET':
        p=run([sys.executable, "/usr/src/app/ticker/eth.py"],stdout=PIPE,stderr=PIPE)
        if(id==-1):
            return JsonResponse("STARTED", safe=False)
        else:
            p.kill()
            print(p)
            return JsonResponse("STOPPED", safe=False)

@csrf_exempt
def ShibSocketApi(request, id=-1):
    if request.method=='GET':
        p=run([sys.executable, "/usr/src/app/ticker/shib.py"],stdout=PIPE,stderr=PIPE)
        if(id==-1):
            return JsonResponse("STARTED", safe=False)
        else:
            p.kill()
            print(p)
            return JsonResponse("STOPPED", safe=False)