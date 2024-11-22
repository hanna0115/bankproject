from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from .serializers import BankProductListSerializer, BankProductSerializer, UserProductSerializer
from .models import BankProducts, UserProduct

from django.db.models import Count
from django.utils import timezone

import pandas as pd
import random
from datetime import datetime, timedelta

User = get_user_model()

# Create your views here.
# 예금상품 전체 리스트 조회 : 우대 금리 기준 내림차순
@api_view(['GET'])
def deposits(request):
    if request.method == 'GET':
        deposits = BankProducts.objects.filter(category=0).order_by('-prime_interest_rate')
        serializer = BankProductListSerializer(deposits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# 예금상품 상세 리스트 조회
@api_view(['GET'])
def deposit_detail(request, product_pk):
    if request.method == 'GET':
        deposit = get_object_or_404(BankProducts, pk=product_pk, category=0)
        serializer = BankProductSerializer(deposit)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# 적금상품 전체 리스트 조회 : 우대 금리 기준 내림차순
@api_view(['GET'])
def savings(request):
    if request.method == 'GET':
        savings = BankProducts.objects.filter(category=1).order_by('-prime_interest_rate')
        serializer = BankProductListSerializer(savings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# 적금상품 상세 리스트 조회
@api_view(['GET'])
def savings_detail(request, product_pk):
    if request.method == 'GET':
        saving = get_object_or_404(BankProducts, pk=product_pk, category=1)
        serializer = BankProductSerializer(saving)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# 필터링한 예금상품 : 은행, 기간 기준 필터링 / 우대 금리 기준 내림차순
@api_view(['GET'])
def filtered_deposits(request):
    if request.method == 'GET':
        deposits = BankProducts.objects.filter(category=0)
        vue_company_code = request.query_params.get('company_code', None)
        vue_join_period = request.query_params.get('join_period', None)

        if vue_join_period and vue_company_code:
            filtered_deposits = deposits.filter(company_code=vue_company_code, join_period__contains=vue_join_period).order_by('-prime_interest_rate')
            serializer = BankProductListSerializer(filtered_deposits, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif vue_join_period:
            filtered_deposits = deposits.filter(join_period__contains=vue_join_period).order_by('-prime_interest_rate')
            serializer = BankProductListSerializer(filtered_deposits, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # 문자열 contain으로 확인(vue에서 개월 수 문자열로 넘겨줘야 함)
        elif vue_company_code:
            filtered_deposits = deposits.filter(company_code=vue_company_code).order_by('-prime_interest_rate')
            serializer = BankProductListSerializer(filtered_deposits, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            filtered_deposits = deposits.filter().order_by('-prime_interest_rate')
            serializer = BankProductListSerializer(filtered_deposits, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# 필터링한 적금상품 : 은행, 기간 기준 필터링 / 우대 금리 기준 내림차순
@api_view(['GET'])
def filtered_savings(request):
    if request.method == 'GET':
        deposits = BankProducts.objects.filter(category=1)
        vue_company_code = request.query_params.get('company_code', None)
        vue_join_period = request.query_params.get('join_period', None)

        if vue_join_period and vue_company_code:
            filtered_deposits = deposits.filter(company_code=vue_company_code, join_period__contains=vue_join_period).order_by('-prime_interest_rate')
            serializer = BankProductListSerializer(filtered_deposits, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif vue_join_period:
            filtered_deposits = deposits.filter(join_period__contains=vue_join_period).order_by('-prime_interest_rate')
            serializer = BankProductListSerializer(filtered_deposits, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # 문자열 contain으로 확인(vue에서 개월 수 문자열로 넘겨줘야 함)
        elif vue_company_code:
            filtered_deposits = deposits.filter(company_code=vue_company_code).order_by('-prime_interest_rate')
            serializer = BankProductListSerializer(filtered_deposits, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            filtered_deposits = deposits.filter().order_by('-prime_interest_rate')
            serializer = BankProductListSerializer(filtered_deposits, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)



# 회원 정보 기반 추천 예금
# 1. 로그인 안 한 상태 : 목표 카테고리 랜덤으로 선택해서 리턴, 최고 금리 순
# 2. 로그인 한 상태 : 나이 대, 고객 목표, 기간, 금액이 동일한 사람들이 많이 가입한 상품 필터링, 최고 금리 순

# 생각해보니까, 로그인한 사람도 자기 목표 말고 목표 값을 선택해서 조회할 수 있을텐데 그 로직도 짜야할 듯.

def get_top_products(bank_products):
    """예금(카테고리 0)과 적금(카테고리 1)을 각각 5개씩 반환하는 함수"""
    print('여기냐=========================')
    deposit_products = bank_products.filter(product__category=0)[:5]  # 예금 상품 5개
    savings_products = bank_products.filter(product__category=1)[:5]  # 적금 상품 5개
    return {
        'deposit_products': deposit_products,
        'savings_products': savings_products,
    }

def recommendation(user=None, purpose=None):
    if user:
        birth_date = user.birth_date
        saving_purpose = user.saving_purpose
        saving_period = user.saving_period
        asset = user.asset
        saving_amount = user.saving_amount

        age_range_start = birth_date - timedelta(days=365*5)
        age_range_end = birth_date + timedelta(days=365*5)

        #!!!! 버튼으로 누른 목적에 맞는 상품 추천 : 이거는 vue에서 넘겨줬을때 어떻게 들어오는지 확인 필요!!!!!!
        if purpose:
            filtered_users = BankProducts.objects.none()
            for pur in map(str.strip, purpose.split(',')):
                __filtered_users = User.objects.filter(
                    birth_date__range=(age_range_start, age_range_end),
                    saving_period=saving_period,
                    saving_purpose__contains=pur
                )
                filtered_users = filtered_users | __filtered_users

        # 회원 가입할 때 입력한 목적에 맞는 상품 추천
        else:
            filtered_users = BankProducts.objects.none()
            for pur in map(str.strip, saving_purpose.split(',')):
                __filtered_users = User.objects.filter(
                    birth_date__range=(age_range_start, age_range_end),
                    saving_period=saving_period,
                    saving_purpose__contains=pur
                )
                filtered_users = filtered_users | __filtered_users

        deposit_filtered_users = filtered_users.filter(
            asset__range=(asset - 2000, asset + 2000)
        )

        savings_filtered_users = filtered_users.filter(
            saving_amount__range=(saving_amount - 50, saving_amount + 50)
        )

        deposit_products = UserProduct.objects.filter(
            user__in=deposit_filtered_users,
            product__category=0  # BankProducts의 category 필드 참조
        ).values('product').annotate(user_count=Count('user')
        ).order_by('-user_count', '-product__interest_rate')[:5]

        savings_products = UserProduct.objects.filter(
            user__in=savings_filtered_users,
            product__category=1  # BankProducts의 category 필드 참조
        ).values('product').annotate(user_count=Count('user')
        ).order_by('-user_count', '-product__interest_rate')[:5]

        return {
            'deposit_products': deposit_products,
            'savings_products': savings_products,
        }

    else:
        if purpose:
            filtered_users = User.objects.filter(saving_purpose__contains=purpose)

            bank_products = UserProduct.objects.filter(
                user__in=filtered_users
            ).values('product').annotate(user_count=Count('user')
            ).order_by('-user_count', '-product__interest_rate')

            return get_top_products(bank_products)

        else:
            # 유저 목록에서 가장 많이 가입한 상품들
            bank_products = UserProduct.objects.values('product').annotate(
                user_count=Count('user')
            ).order_by('-user_count', '-product__interest_rate')

            return get_top_products(bank_products)


import json

@api_view(['GET'])
def products_recommend(request):
    purpose = request.query_params.get('saving_purpose', None)

    # JSON 문자열을 파싱하여 리스트로 변환
    if purpose is not None:
        try:
            purpose = json.loads(purpose)  # JSON 문자열을 리스트로 변환
        except json.JSONDecodeError:
            purpose = None

    if request.user.is_authenticated:
        recommended_products = recommendation(user=request.user, purpose=purpose)
    else:
        recommended_products = recommendation(purpose=purpose)

    # 함수로 return한 queryset에서 예금, 적금의 pk만 뽑아서 리스트에 저장.
    recommended_deposits_pk = [user_product['product'] for user_product in recommended_products['deposit_products']]
    recommended_savings_pk = [user_product['product'] for user_product in recommended_products['savings_products']]
    
    # 순서대로 pk와 bankproduct를 비교해서 데이터 생성
    recommended_deposits_product_list = []
    for pk in recommended_deposits_pk:
        recommended_deposits_product = BankProducts.objects.get(pk=pk)
        recommended_deposits_product_list.append(recommended_deposits_product)

    recommended_savings_product_list = []
    for pk in recommended_savings_pk:
        recommended_savings_product = BankProducts.objects.get(pk=pk)
        recommended_savings_product_list.append(recommended_savings_product)

    # 넘겨줌
    response_data = {
        'deposit_products': BankProductSerializer(recommended_deposits_product_list, many=True).data,
        'savings_products': BankProductSerializer(recommended_savings_product_list, many=True).data
    }

    return Response(response_data, status=status.HTTP_200_OK)

# ---------------------------------------------------------------------------------------------------

# user_pk와 product_pk를 난수로 만들어둔 엑셀 파일 (10000개)
products_joined_data = pd.read_csv('bank_products/data/products_joined.csv')

# 가입일자 생성을 위한 날짜 (2021년 ~ 현재)
start_date = datetime(2024, 7, 1)
end_date = datetime(2024, 11, 25)

def create_user_products(asset, product):
    # join date
    random_days = random.randint(0, (end_date - start_date).days)
    join_date = start_date + timedelta(days=random_days)

    # join_period
    if product.join_period == 'no_limit':
        join_period_list = [6, 12, 24, 36]
    else:
        join_period_list = list(map(str.strip, product.join_period.split(',')))
        print(join_period_list)

        # '36+'값 제거
        join_period_list = [int(elem) for elem in join_period_list if elem.isdigit()]
        # 1, 3 ,9 값 제거
        join_period_list = [period for period in join_period_list if period in [6, 12, 24, 36]]

    if not join_period_list:
        join_period_list = [36]

    join_period = random.choice(join_period_list)

    # expiration_date
    expiration_date = join_date + timedelta(days=join_period*30)

    # monthly_amount
    join_amount_min = product.join_amount_min
    join_amount_max = product.join_amount_max
    # 예금이면서
    if not product.category:
        # max의 제한이 없는 경우
        if not join_amount_max:
            # user의 asset을 최대값으로 설정
            join_amount_max = asset
        # max의 제한이 있는 경우
        else:
            # user의 asset과 max 값 중 min값을 최대값을 설정
            join_amount_max = min(join_amount_max, asset)
    # 적금이면서 max의 제한이 없는 경우
    elif not join_amount_max:
        join_amount_max = 200

    join_amount_min = max(join_amount_min, 5)
    join_amount_max = max(join_amount_max, 5)
    join_amount_min, join_amount_max = sorted([join_amount_min, join_amount_max])
    monthly_amount = random.randint(join_amount_min, join_amount_max)

    # interest_rate
    interest_rate_min = product.interest_rate
    interest_rate_max = product.prime_interest_rate
    interest_rate = round(random.uniform(interest_rate_min, interest_rate_max), 2)

    return join_date, expiration_date, join_period, monthly_amount, interest_rate


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def products_joined(request, user_pk):

    # 자신의 예적금만 연동 및 조회 가능
    user = get_object_or_404(User, pk=user_pk)
    if request.user == user:

        # 연동된 예적금 조회
        if request.method == 'GET':
            userproducts = UserProduct.objects.filter(user=user_pk)
            serializer = UserProductSerializer(userproducts, many=True)
            return Response(serializer.data)
        
        # 예적금 연동하기
        if request.method == 'POST':
            before_len = len(UserProduct.objects.filter(user=user_pk))

            # 연동하기 버튼을 누른 user가 가입한 상품 리스트
            joined_products = products_joined_data[products_joined_data['user_pk'] == user_pk].product_pk.unique().tolist()[:5]

            if not joined_products:
                return Response({'detail': '가입된 예적금이 없습니다.'}, status=status.HTTP_200_OK)

            # BankProducts 모델에서 pk 기반으로 상품 객체 조회
            bank_products = BankProducts.objects.filter(pk__in=joined_products)            

            # user가 가입한 상품을 하나씩 UserProduct DB에 저장
            for product in bank_products:
                data = create_user_products(user.asset, product)

                _ = UserProduct.objects.get_or_create(user=user, product=product,
                                                defaults={'join_date':data[0], 'expiration_date':data[1],
                                                            'join_period':data[2], 'monthly_amount':data[3],
                                                            'interest_rate':data[4]})
        
            after_len = len(UserProduct.objects.filter(user=user_pk))

            userproducts = UserProduct.objects.filter(user=user_pk)
            serializer = UserProductSerializer(userproducts, many=True)
            if before_len == after_len:
                return Response({'detail': '이미 모든 예적금이 연동되어 있습니다.', 'data':serializer.data}, status=status.HTTP_200_OK)
            
            return Response({'detail': f'{user.name}님의 예적금이 연동되었습니다.', 'data':serializer.data
                             }, status=status.HTTP_201_CREATED)
        
    return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)