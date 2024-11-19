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



# 회원 정보 기반 추천 예금 : 알고리즘 내일 확정.
# 1. 로그인 안 한 상태 : 목표 카테고리 랜덤으로 선택해서 리턴, 최고 금리 순
# 2. 로그인 한 상태 : 나이 대, 고객 목표, 기간, 금액이 동일한 사람들이 많이 가입한 상품 필터링, 최고 금리 순
def recommendation(user=None, purpose=None):
    # 1. 로그인 한 상태면 정보 기반으로 추천 
    if user:
        birth_date = user.birth_date
        asset = user.asset # 예금에 써
        saving_purpose = user.saving_purpose.split(',').strip()
        saving_amount = user.saving_amount # 적금에 써
        saving_period = user.saving_period

        users = get_user_model().objects.all()

        # 1. user를 필터링해 -> 2. 그 유저가 가입한 많이 가입한 상품 목록을 받아. -> 3. 금리기준 내림차순 리턴
        # 목표를 어떻게 필터링 할지(다중 선택 가능해서 리스트로 전달해야 할 것 같음)
        # 1. user 필터링
        filtered_users = users.filter(birth_date__range=(birth_date-1825,birth_date+1825))\
            .filter(asset__range=(asset-200,asset+200))\
            .filter(saving_period=saving_period)
        
        # .filter() # 목표 어떻게 필터링해야함 \
        # 2. 가입한 상품목록 -> 금리 기준 내림차순
        
        # 예금, 적금 필터링, 5개 씩 리턴

    # 2. 로그인 안 한 사람
    else:
        filtered_users = users.filter(saving_purpose__contains=purpose)
    
    return filtered_users['user_bank_products']
        
        
    pass




@api_view(['GET'])
def products_recommend(request):
    if request.user.is_authenticated:
        recommended_products = recommendation(request.user)
    else:
        purpose = request.query_params.get('saving_purpose', None)
        recommended_products = recommendation(purpose)
    serializer = BankProductListSerializer(recommended_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




# 사용자 가입 예적금 상품 불러오기 : 가입한 예적금 상품 연동하기 누르면 DB에 추가되도록하고, 조회 값 return
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def products_joined(request, user_pk):
    # 가입일 기준으로 오름차순(D-date 가까운 순)
    userproducts = UserProduct.objects.filter(user_pk=user_pk).order_by('join_date')
    serializer = UserProductSerializer(userproducts, many=True)
    return Response(serializer.data)
