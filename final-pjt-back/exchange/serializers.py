from rest_framework import serializers
from .models import Exchange

# 메인페이지 돼지저금통 조회
class ExchangeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Exchange
		fields = '__all__'
