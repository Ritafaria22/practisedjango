from django.shortcuts import render,redirect
from . import forms 
from . import models
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = forms.Albumform(request.POST)#user data pass korse
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    else:
        album_form = forms.Albumform()
    return render(request, 'add_album.html', {'form' : album_form})


def delete_album(request, id):
    musician = models.Album.objects.get(pk=id)
    musician.delete()
    return redirect('homepage')


 
def edit_album(request,id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.Albumform(instance=album)#edit a click korle age theke dea input thakbe jeta theke edit korte chai.
    if request.method == 'POST':
        album_form = forms.Albumform(request.POST, instance=album)#user data pass korse
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
 
    return render(request, 'add_album.html', {'form' : album_form})