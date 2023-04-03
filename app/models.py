from django.db import models

# Create your models here.

class Country(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)

class City(models.Model):
    cid=models.OneToOneField(Country,on_delete=models.CASCADE)
    cityname=models.CharField(max_length=100)
    cityid=models.IntegerField()