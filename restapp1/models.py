from django.db import models

class student(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    address= models.CharField(max_length=100)
