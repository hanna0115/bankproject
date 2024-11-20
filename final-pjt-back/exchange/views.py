from django.shortcuts import render
from django.conf import settings
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse 
from .serializers import ExchangeSerializer
from .models import Exchange
import schedule
import time
from datetime import date


def update_exchange():
    # 오늘 날짜의 데이터가 이미 존재하는지 확인
    if Exchange.objects.filter(date=date.today()).exists():
        print("Today's exchange rates already exist.")
        return None  # 이미 데이터가 있으면 API 호출하지 않음

    # 금융 상품 저장하기.
    API_KEY = settings.EXCHANGE_API_KEY
    URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': API_KEY,
        'data': 'AP01'
    }

    try:
        # SSL 검증 비활성화
        response = requests.get(URL, params=params, verify=False)
        products = response.json()

        for product in products:
            cur_unit = product.get('cur_unit')
            cur_nm = product.get('cur_nm')
            deal_bas_r = product.get('deal_bas_r')

            # 오늘 날짜의 동일한 통화 정보가 없을 때만 저장
            if not Exchange.objects.filter(cur_unit=cur_unit, date=date.today()).exists():
                save_data = {
                    'cur_unit': cur_unit,
                    'cur_nm': cur_nm,
                    'deal_bas_r': float(deal_bas_r.replace(',', '')),
                    'date': date.today()
                }

                serializer = ExchangeSerializer(data=save_data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

        print("Exchange rates updated successfully.")
        return Response(status=status.HTTP_200_OK)

    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 환율 정보 매일 12시에 정기적으로 받아오기 코드. 일단 서버 계속 켜져 있지 않으니까,
# 일단 get 요청시마다 오늘날짜 데이터 없으면 받아오기
# schedule.every().day.at("12:00").do(update_exchange)

# 환율정보 API로 받아오기
@api_view(['GET'])
def get_exchange(request):
   # 오늘 날짜의 데이터가 없으면 업데이트 시도
    update_exchange()

    # 오늘날짜 환율 리스트 보내주기.
    exchange = Exchange.objects.filter(date=date.today())
    serializer = ExchangeSerializer(exchange, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
