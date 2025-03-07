from django import forms
from .models import Musician
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  


#add musician a click korle ei form a niye asbe
class Musicianform(forms.ModelForm):
    class Meta:
        model= Musician
        fields= '__all__'

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'required'}))
    class Meta:
        model=User
        fields= ['username','first_name', 'last_name', 'email']


 