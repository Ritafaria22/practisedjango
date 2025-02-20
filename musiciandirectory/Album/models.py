from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    albumname= models.CharField(max_length=30)
    releasedate=models.DateField()
    Rating=models.IntegerField()
    musician=models.ForeignKey(Musician, on_delete=models.CASCADE)#one to many relationship

    def __str__(self):
        return f"{self.albumname}"