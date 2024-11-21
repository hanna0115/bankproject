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
        # 문자열 contain으로 확인(vue에서 개월 수 문자열로 넘겨줘야 함)
        filtered_deposits = deposits.filter(company_code=vue_company_code, join_period__contains=vue_join_period).order_by('-prime_interest_rate')
        serializer = BankProductListSerializer(filtered_deposits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# 필터링한 적금상품 : 은행, 기간 기준 필터링 / 우대 금리 기준 내림차순
@api_view(['GET'])
def filtered_savings(request):
    if request.method == 'GET':
        savings = BankProducts.objects.filter(category=1)
        vue_company_code = request.query_params.get('company_code', None)
        vue_join_period = request.query_params.get('join_period', None)
        # 문자열 contain으로 확인(vue에서 개월 수 문자열로 넘겨줘야 함)
        filtered_savings = savings.filter(company_code=vue_company_code, join_period__contains=vue_join_period).order_by('-prime_interest_rate')
        serializer = BankProductListSerializer(filtered_savings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)



# 회원 정보 기반 추천 예금
# 1. 로그인 안 한 상태 : 목표 카테고리 랜덤으로 선택해서 리턴, 최고 금리 순
# 2. 로그인 한 상태 : 나이 대, 고객 목표, 기간, 금액이 동일한 사람들이 많이 가입한 상품 필터링, 최고 금리 순

# 생각해보니까, 로그인한 사람도 자기 목표 말고 목표 값을 선택해서 조회할 수 있을텐데 그 로직도 짜야할 듯.

def get_top_products(bank_products):
    """예금(카테고리 0)과 적금(카테고리 1)을 각각 5개씩 반환하는 함수"""
    deposit_products = bank_products.filter(category=0)[:5]  # 예금 상품 5개
    savings_products = bank_products.filter(category=1)[:5]  # 적금 상품 5개
    return {
        'deposit_products': deposit_products,
        'savings_products': savings_products,
    }

def recommendation(user=None, purpose=None):
    # 1. 로그인 한 상태면 정보 기반으로 추천
    if user:
        birth_date = user.birth_date
        saving_purpose = user.saving_purpose  # JSONField로 저장된 다중 선택 값
        saving_period = user.saving_period
        asset = user.asset  # 예금에 사용
        saving_amount = user.saving_amount  # 적금에 사용

        # 나이 범위 계산 (±5년)
        age_range_start = birth_date - timedelta(days=365*5)
        age_range_end = birth_date + timedelta(days=365*5)

        # 로그인한 사용자가 특정 purpose를 선택했는지 확인
        if purpose:
            # 사용자가 선택한 목적 기반으로 필터링
            filtered_users = User.objects.filter(
                saving_purpose__contains=purpose,
                saving_period=saving_period,
            )
        else:
            # 사용자의 정보 기반으로 필터링 (나이, 저축 기간, 저축 목표)
            filtered_users = User.objects.filter(
                birth_date__range=(age_range_start, age_range_end),
                saving_period=saving_period,
                saving_purpose__overlap=saving_purpose  # 다중 선택된 목적 중 하나라도 겹치는지 확인
            )

        # 예금용 필터링: 자산을 기준으로 필터링
        deposit_filtered_users = filtered_users.filter(
            asset__range=(asset - 200, asset + 200)
        )

        # 적금용 필터링: 저축 금액을 기준으로 필터링
        savings_filtered_users = filtered_users.filter(
            saving_amount__range=(saving_amount - 200, saving_amount + 200)
        )

        # 예금 상품 목록 가져오기 및 가입자 수 계산 (자산 기반)
        deposit_products = BankProducts.objects.filter(
            bank_product_users__in=deposit_filtered_users,
            category=0  # 예금 카테고리
        ).annotate(user_count=Count('bank_product_users')).distinct().order_by('-user_count', '-interest_rate')[:5]

        # 적금 상품 목록 가져오기 및 가입자 수 계산 (저축 금액 기반)
        savings_products = BankProducts.objects.filter(
            bank_product_users__in=savings_filtered_users,
            category=1  # 적금 카테고리
        ).annotate(user_count=Count('bank_product_users')).distinct().order_by('-user_count', '-interest_rate')[:5]

        return {
            'deposit_products': deposit_products,
            'savings_products': savings_products,
        }

    # 2. 로그인 안 한 상태면 목적 기반 추천
    else:
        if purpose:
            # 해당 목적을 가진 사용자들이 가장 많이 가입한 상품을 찾기 위해 필터링
            filtered_users = User.objects.filter(
                saving_purpose__contains=purpose
            )

            # 해당 사용자들이 많이 가입한 예적금 상품을 금리 기준으로 정렬
            bank_products = BankProducts.objects.filter(
                bank_product_users__in=filtered_users
            ).annotate(user_count=Count('bank_product_users')).order_by('-user_count', '-interest_rate')

            return get_top_products(bank_products)
        
        # 모든 사용자가 가장 많이 가입한 상품 기준 필터링 (목표가 없을 때)
        else:
            bank_products = BankProducts.objects.annotate(
                user_count=Count('bank_product_users')
            ).order_by('-user_count', '-interest_rate')

            return get_top_products(bank_products)




@api_view(['GET'])
def products_recommend(request):
    # GET 요청에서 saving_purpose 파라미터를 가져옴 (없으면 None)
    purpose = request.query_params.get('saving_purpose', None)

    # 1. 로그인 한 상태일 때
    if request.user.is_authenticated:
        # 사용자의 정보와 선택된 목적(없으면 None)을 함께 전달하여 추천
        recommended_products = recommendation(user=request.user, purpose=purpose)
    
    # 2. 로그인하지 않은 상태일 때
    else:
        # 비로그인 사용자는 purpose가 없으면 모든 사용자가 가장 많이 가입한 상품을 추천
        recommended_products = recommendation(purpose=purpose)

    # 3. 예금과 적금 상품을 각각 직렬화하여 반환
    response_data = {
        'deposit_products': BankProductListSerializer(recommended_products['deposit_products'], many=True).data,
        'savings_products': BankProductListSerializer(recommended_products['savings_products'], many=True).data,
    }

    return Response(response_data, status=status.HTTP_200_OK)



# user_pk와 product_pk를 난수로 만들어둔 엑셀 파일 (10000개)
products_joined_data = pd.read_csv('bank_products/data/products_joined.csv')

# 가입일자 생성을 위한 날짜 (2021년 ~ 현재)
start_date = datetime(2021, 1, 1)
end_date = datetime(2024, 11, 25)

def create_user_products(product):
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
        join_period_list = [period for period in join_period_list if period in [6, 12, 24, 36]]

    if not join_period_list:
        join_period_list = [36]

    join_period = random.choice(join_period_list)

    # expiration_date
    expiration_date = join_date + timedelta(days=join_period*30)

    # monthly_amount
    join_amount_min = product.join_amount_min
    join_amount_max = product.join_amount_max
    if not join_amount_max:
        join_amount_max = 200
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

        # if not joined_products:
        #     return Response({'detail': '가입된 예적금 상품이 없습니다.'}, status=status.HTTP_200_OK)

        # BankProducts 모델에서 pk 기반으로 상품 객체 조회
        bank_products = BankProducts.objects.filter(pk__in=joined_products)            
        user = get_object_or_404(User, pk=user_pk)


        # user가 가입한 상품을 하나씩 UserProduct DB에 저장
        for product in bank_products:
            data = create_user_products(product)

            _ = UserProduct.objects.get_or_create(user=user, product=product,
                                            defaults={'join_date':data[0], 'expiration_date':data[1],
                                                        'join_period':data[2], 'monthly_amount':data[3],
                                                        'interest_rate':data[4]})
    
        after_len = len(UserProduct.objects.filter(user=user_pk))

        if before_len == after_len:
            return Response({'detail': '이미 모든 상품이 연동되어 있습니다.'}, status=status.HTTP_200_OK)

        return Response({'detail': f'{user.email.split("@")[0]}님의 예적금이 연동되었습니다.'}, status=status.HTTP_201_CREATED)
    