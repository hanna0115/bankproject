from django.db import models

# Create your models here.
class Exchange(models.Model):
    cur_unit = models.TextField()
    cur_nm = models.TextField()
    deal_bas_r = models.FloatField()
    date = models.DateField()