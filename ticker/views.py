from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Eth
from .serializers import EthSerializer

from django.core.files.storage import default_storage
from django.utils.crypto import get_random_string

# Create your views here.
@csrf_exempt
def EthApi(request, id=-1):
    if request.method=='GET':
        eth=Eth.objects.all()
        eth_s=EthSerializer(eth,many=True)
        print("ETH")
        return  JsonResponse(eth_s.data, safe=False)
    if request.method=='POST':
        eth_data=JSONParser().parse(request)
        eth_s=EthSerializer(data=eth_data)
        if eth_s.is_valid():
            eth_s.save()
            return JsonResponse("ADDED",safe=False)
        return JsonResponse(eth_s.errors, safe=False)
