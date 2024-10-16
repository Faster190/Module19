from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.IntegerField()


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=True)
    buyer = models.ManyToManyField(Buyer, related_name="Games")
