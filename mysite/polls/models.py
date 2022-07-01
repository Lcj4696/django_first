from django.db import models

# Create your models here.
class List(models.Model):
    name=models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    bench = models.IntegerField()
    dead = models.IntegerField()
    squart = models.IntegerField()
    weight = models.IntegerField()