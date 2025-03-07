from django import forms
from .models import Album

#add aalbum a click korle ei form a niye asbe
class Albumform(forms.ModelForm):
    class Meta:
        model= Album
        fields= '__all__'
