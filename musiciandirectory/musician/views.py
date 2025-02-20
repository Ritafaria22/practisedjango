from django.shortcuts import render,redirect
from . import forms 
from . import models
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.Musicianform(request.POST)#user data pass korse
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    else:
        musician_form = forms.Musicianform()
    return render(request, 'add_musician.html', {'form' : musician_form})


def edit_musician(request,id):
    musician = models.Musician.objects.get(pk=id)
    musician_form = forms.Musicianform(instance=musician)#edit a click korle age theke dea input thakbe jeta theke edit korte chai.
    if request.method == 'POST':
        musician_form = forms.Musicianform(request.POST, instance=musician)#user data pass korse
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
 
    return render(request, 'add_musician.html', {'form' : musician_form})