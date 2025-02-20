from django.db import models

# Create your models here.
class Musician(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    instrumenttype=models.CharField(max_length=40)
    
    def __str__(self):
        return self.firstname