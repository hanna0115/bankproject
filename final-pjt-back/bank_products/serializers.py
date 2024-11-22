from rest_framework import serializers
from .models import BankProducts, UserProduct
from django.conf import settings
from django.utils.timezone import now


class BankProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankProducts
        fields = ('category', 'company_code', 'company_name', 'product_code', 'product_name', 'interest_rate', 'prime_interest_rate', 'product_link', 'join_way')


class BankProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankProducts
        fields = '__all__'


class UserProductSerializer(serializers.ModelSerializer):
    
    product = BankProductSerializer(read_only=True)
    d_day = serializers.SerializerMethodField()


    def get_d_day(self, obj):
        # expiration_date가 None이 아닌 경우 d-day 계산
        if obj.expiration_date:
            return (obj.expiration_date.date() - now().date()).days
        return None  # 만료일이 없으면 None 반환

    # 납입 기간(개월)
    remain_month = serializers.SerializerMethodField()

    def get_remain_month(self, obj):
        # expiration_date가 None이 아닌 경우 d-day 계산
        if obj.join_date:
            return int((now().date() - obj.join_date.date()).days/30)+1
        return None  # 만료일이 없으면 None 반환

    class Meta:
        model = UserProduct
        fields = '__all__'
