from django.db import models
from django.conf import settings

# Create your models here.
class BankProducts(models.Model):
    category = models.IntegerField()
    company_code = models.TextField()
    company_name = models.TextField()
    product_code = models.TextField()
    product_name = models.TextField()
    interest_rate = models.FloatField()
    prime_interest_rate = models.FloatField()
    product_link = models.TextField()
    join_period = models.TextField()
    join_period_text = models.TextField()
    join_amount_min = models.IntegerField()
    # null값 : 최대 금액 제한 없음
    join_amount_max = models.IntegerField(null=True, blank=True)
    join_amount_text = models.TextField()
    join_way = models.TextField(null=True, blank=True)
    join_member = models.TextField()
    prime_conditions = models.TextField(null=True, blank=True)
    interest_payment = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)



class UserProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(BankProducts, on_delete=models.CASCADE)
    # 21년부터 지금까지 랜덤
    join_date = models.DateTimeField()
    # join_date에서 += join_period
    expiration_date = models.DateTimeField()
    # 리스트 중에서 하나 선택
    join_period = models.IntegerField()
    # 최고, 최저 사이 랜덤, 1만원 단위로
    monthly_amount = models.IntegerField()
    # 더미데이터 : 최저~우대금리 사이 값 선택 0.1%씩 차이
    interest_rate = models.FloatField()