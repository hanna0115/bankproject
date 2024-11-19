from django.db import models
from django.conf import settings
from bank_products.models import UserProduct


# Create your models here.
class PiggyBank(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    user_product = models.ForeignKey(UserProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    weight = models.FloatField(default=0.0)
    cheerup_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

