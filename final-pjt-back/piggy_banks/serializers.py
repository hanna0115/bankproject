from rest_framework import serializers
from .models import PiggyBank
from datetime import datetime
from django.utils.timezone import now

# 메인페이지 돼지저금통 조회
class PiggyListSerializer(serializers.ModelSerializer):
        
	class Meta:
		model = PiggyBank
		fields = ('user', 'name', 'cheerup_count')
		read_only_fields = ('user',)


# 내 돼지저금통 조회
class PiggyDetailSerializer(serializers.ModelSerializer):
    # d_day 계산 로직
    d_day = serializers.SerializerMethodField()

    def get_d_day(self, obj):
        if hasattr(obj, 'user_product') and obj.user_product and obj.user_product.expiration_date:
            return (obj.user_product.expiration_date - now().date()).days
        return None

    class Meta:
        model = PiggyBank
        fields = '__all__'
        read_only_fields = ('user', 'user_product')


# 돼지저금통 생성, 수정
class PiggySerializer(serializers.ModelSerializer):

	class Meta:
		model = PiggyBank
		fields = '__all__'
		read_only_fiels = ('user', 'user_product')


