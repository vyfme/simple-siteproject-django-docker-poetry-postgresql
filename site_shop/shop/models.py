from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    percent = models.IntegerField()
    in_stock = models.BooleanField()
    pub_date = models.DateTimeField()