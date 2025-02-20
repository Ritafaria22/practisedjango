from django import forms
from .models import Musician

#add musician a click korle ei form a niye asbe
class Musicianform(forms.ModelForm):
    class Meta:
        model= Musician
        fields= '__all__'
