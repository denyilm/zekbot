
from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^eth$',views.EthApi),
    url(r'^shib$',views.ShibApi),
    url(r'^ethsocket$',views.EthSocketApi),
    url(r'^ethsocket/([0-9]+)$',views.EthSocketApi),
    url(r'^shibsocket$',views.ShibSocketApi),
    url(r'^shibsocket/([0-9]+)$',views.ShibSocketApi),
    url(r'^tradeeth$',views.TradeEth),
    url(r'^tradeeth/([0-9]+)$',views.TradeEth),
    url(r'^tradeshib$',views.TradeShib),
    url(r'^tradeshib/([0-9]+)$',views.TradeShib)
]