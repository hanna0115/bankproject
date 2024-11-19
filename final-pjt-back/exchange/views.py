from django.shortcuts import render
from django.conf import settings
import requests
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse 
from .serializers import ExchangeSerializer
from .models import Exchange
import schedule
import time
from datetime import datetime


def update_exchange():
    # 금융 상품 저장하기.
    API_KEY =settings.EXCHANGE_API_KEY

    URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey' : API_KEY,
        'data' : 'AP01'
    }

    products = requests.get(URL, params=params).json()

    for product in products:
        if not Exchange.objects.filter(cur_unit=cur_unit).exists():
            cur_unit = product.get('cur_unit')
            cur_nm = product.get('cur_nm')
            deal_bas_r = product.get('deal_bas_r')

            save_data = {
                'cur_unit':cur_unit,
                'cur_nm':cur_nm,
                'deal_bas_r':deal_bas_r,
                'date':datetime.today()
            }
        
            serializer = ExchangeSerializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

schedule.every().day.at("12:00").do(update_exchange)

# 환율정보 API로 받아오기
def get_exchange(request):
    # 금융 상품 리스트 보내주기.
    exchange = Exchange.objects.filter(date=datetime.today())
    serializer = ExchangeSerializer(exchange, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
