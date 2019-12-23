from django.db import models
class Cust(models.Model):
    name=models.CharField(max_length=35)
    no=models.IntegerField()
    age=models.IntegerField()
    city=models.CharField(max_length=35)

# Create your models here.
