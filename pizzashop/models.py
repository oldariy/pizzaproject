from django.db import models


# Create your models here.
class Dish(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField(default=0)


