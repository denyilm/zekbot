from os import kill, system
from django.shortcuts import render
import time, base64, hmac, hashlib, requests, json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from subprocess import Popen, run,PIPE
import pandas as pd
import sys

from .models import Eth, Shib
from .serializers import EthSerializer, ShibSerializer

from django.core.files.storage import default_storage
from django.utils.crypto import get_random_string


apiKey='3c9e6309-db16-43f8-b355-29067d6e2fed'
apiSecret='Q0XnMt/SGpwBIuleyPy8fG0VFY3PXiP5'
apiSecret = base64.b64decode(apiSecret)

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
        shib=Shib.objects.all().order_by('id')
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

@csrf_exempt
def TradeEth(request, id=-1):
    while True:
        data=Eth.objects.all().order_by('-id')[:300].values("price")
        data_reverse=reversed(data)
        data_reverse_s=EthSerializer(data_reverse, many=True)
        df=pd.DataFrame(list(data_reverse))
        cumret=(df.pct_change()+1).cumprod()-1
        print("CUMRET: ", cumret)
        if(id==1):
            return JsonResponse(data_reverse_s.data, safe=False)

@csrf_exempt
def TradeShib(request, id=-1):
    # Start with false, which means you have money not coin
    position=False
    while True:
        data=Shib.objects.all().order_by('-id')[:600].values("price")
        data_reverse=reversed(data)
        data_reverse_s=ShibSerializer(data_reverse, many=True)
        df=pd.DataFrame(list(data_reverse))
        cumret=(df.pct_change()+1).cumprod()-1
        threshold=cumret.values[cumret.last_valid_index()][0]
        print("CUMRET: ", 100*threshold)
        balance=getBalance()
        latestPrice=df.values[df.last_valid_index()][0]
        if 100*threshold>0.05 and not position:
            print('BUY', latestPrice)
            balance=getBalance()
            money=format(balance['para'],".0f")
            openOrder("buy", latestPrice,float(money)-1, "SHIB_TRY")
            Shib.objects.all().delete()
            position=True
        if position:
            data=Shib.objects.all().order_by('-id')[:600].values("price")
            data_reverse=reversed(data)
            data_reverse_s=ShibSerializer(data_reverse, many=True)
            df=pd.DataFrame(list(data_reverse))
            cumret=(df.pct_change()+1).cumprod()-1
            threshold=cumret.values[cumret.last_valid_index()][0]
            latestPrice=df.values[df.last_valid_index()][0]
            if 100*threshold>0.15:
                print('SELL', latestPrice)
                balance=getBalance()
                shib=format(balance['shib'],".0f")
                print('SHIB', shib)
                openOrder("sell", latestPrice, float(shib)-10, "SHIB_TRY")
                Shib.objects.all().delete()
                position=False
            if 100*threshold<-1:
                print('SELL', latestPrice)
                balance=getBalance()
                shib=format(balance['shib'],".0f")
                print('SHIB', shib)
                openOrder("sell", latestPrice, float(shib)-10, "SHIB_TRY")
                Shib.objects.all().delete()
                position=False
        time.sleep(1)
        ##
        if(id==1):
            return JsonResponse(data_reverse_s.data, safe=False)

# asd
def openOrder(orderType, price, quantity, pair):
    base = "https://api.btcturk.com"
    method = "/api/v1/order"
    uri = base+method
    stamp = str(int(time.time())*1000)
    data = "{}{}".format(apiKey, stamp).encode("utf-8")
    signature = hmac.new(apiSecret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {"X-PCK": apiKey, "X-Stamp": stamp, "X-Signature": signature, "Content-Type" : "application/json"}
    params={"quantity": quantity, "price": price, "stopPrice": 0, "newOrderClientId":"BtcTurk Python API Test", "orderMethod":"market", "orderType":orderType, "pairSymbol":"SHIB_TRY"}
    result = requests.post(url=uri, headers=headers, json=params)
    result = result.json()
    print(json.dumps(result, indent=2))
    return result

# asd
def getBalance():
    base = "https://api.btcturk.com"
    method = "/api/v1/users/balances"
    uri = base+method
    stamp = str(int(time.time())*1000)
    data = "{}{}".format(apiKey, stamp).encode("utf-8")
    signature = hmac.new(apiSecret, data, hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {"X-PCK": apiKey, "X-Stamp": stamp, "X-Signature": signature, "Content-Type" : "application/json"}
    result = requests.get(url=uri, headers=headers)
    turkish = result.json()["data"][0]
    eth=result.json()["data"][40]
    shiba = result.json()["data"][34]
    return {"para" : float(turkish["balance"]), "shib": float(shiba["balance"]), "eth": float(eth["balance"])}