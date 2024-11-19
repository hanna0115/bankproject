from rest_framework import serializers
from .models import BankProducts, UserProduct
from django.conf import settings


class BankProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankProducts
        fields = ('category', 'company_code', 'company_name', 'product_code', 'product_name', 'interest_rate', 'prime_interest_rate', 'product_link', 'join_way')


class BankProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankProducts
        fields = '__all__'


class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = '__all__'