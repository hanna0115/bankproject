from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from bank_products.models import BankProducts

class CustomUserManager(BaseUserManager):
    """이메일을 식별자로 사용하는 커스텀 유저 매니저"""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수 항목입니다.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None  # username 필드 제거
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    birth_date = models.DateField()
    asset = models.IntegerField()
    saving_purpose = models.JSONField()  # 다중 선택을 위해 JSONField 사용
    saving_amount = models.IntegerField()
    saving_period = models.IntegerField()
    followings = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='followers'
    )

    objects = CustomUserManager()
    
    # 사용자 1명이 가입한 예적금 상품 / 역참조 : 예적금 상품에 가입한 사용자들
    user_bank_products = models.ManyToManyField(BankProducts, related_name="bank_product_users")

    USERNAME_FIELD = 'email'
    # 필수로 입력받을 필드 목록
    REQUIRED_FIELDS = ['name', 'birth_date', 'asset', 'saving_purpose', 'saving_amount', 'saving_period']

    def __str__(self):
        return self.email