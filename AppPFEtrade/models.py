from django.db import models

# Create your models here.



class Buyer(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    ticker = models.CharField(max_length=5)
    precio = models.FloatField(max_length=4)

class Seller(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    ticker = models.CharField(max_length=5)
    precio = models.FloatField()

class Market(models.Model):
    
    position = models.CharField(max_length=30)
    ticker = models.CharField(max_length=5)
    price = models.FloatField(max_length=1000000)
