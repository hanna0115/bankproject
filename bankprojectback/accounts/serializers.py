from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
import re
from django.conf import settings

User = get_user_model()


# 회원가입을 위한 커스텀 시리얼라이저
class CustomRegisterSerializer(RegisterSerializer):
    # username 필드 제거
    username = None
    # 기본 필드 외 추가 필드 정의
    # 커스텀 필드 추가
    name = serializers.CharField(required=True)
    birth_date = serializers.DateField(required=True)
    asset = serializers.IntegerField(required=True)
    saving_purpose = serializers.ListField(required=True)
    saving_amount = serializers.IntegerField(required=True)
    saving_period = serializers.IntegerField(required=True)

    def validate_password1(self, password):
        """비밀번호 유효성 검사"""
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            raise serializers.ValidationError(
                "비밀번호는 8자 이상이며, 영문 대소문자, 숫자, 특수문자를 포함해야 합니다."
            )
        return password

    # 이메일 형식 유효성 검사
    def validate_email(self, email):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise serializers.ValidationError("유효한 이메일 형식이 아닙니다.")
        return email

    # 자산 금액 유효성 검사: 10,000원 단위
    def validate_asset(self, amount):
        if amount % 10000 != 0:
            raise serializers.ValidationError("자산 금액은 10,000원 단위여야 합니다.")
        return amount
    
    # 저축 금액 유효성 검사: 10,000원 단위
    def validate_saving_amount(self, amount):
        """저축 금액 유효성 검사"""
        if amount % 10000 != 0:
            raise serializers.ValidationError("저축 금액은 10,000원 단위여야 합니다.")
        return amount

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'name': self.validated_data.get('name', ''),
            'birth_date': self.validated_data.get('birth_date', ''),
            'asset': self.validated_data.get('asset', ''),
            'saving_purpose': self.validated_data.get('saving_purpose', []),
            'saving_amount': self.validated_data.get('saving_amount', ''),
            'saving_period': self.validated_data.get('saving_period', '')
        })
        return data


# 사용자 정보 조회/수정을 위한 시리얼라이저
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('pk', 'email', 'name', 'birth_date', 'asset', 'saving_purpose', 

                 'saving_amount', 'saving_period')
        read_only_fields = ('pk','email', 'name', )  #  수정 불가