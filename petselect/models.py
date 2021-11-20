from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50) #Campo de carácteres de hasta solo 50 chars
    hair = models.CharField(max_length=10) 
    size = models.CharField(max_length=10)