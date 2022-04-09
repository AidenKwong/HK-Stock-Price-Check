from django.db import models


class Stock(models.Model):
    time = models.DateField()
    code = models.CharField(max_length=10)
    closed_price = models.FloatField()
    volume = models.IntegerField()
