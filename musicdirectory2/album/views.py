from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator #login required er kaj er jnno
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from . import models
from . import forms 

@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(CreateView):
    model=models.Album
    form_class= forms.Albumform
    template_name= 'add_album.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.mucisian= self.request.user
        return super().form_valid(form)


 
class EditAlbumView(UpdateView):
        model=models.Album
        form_class= forms.Albumform
        template_name= 'add_album.html'
        pk_url_kwarg='id'
        success_url = reverse_lazy('homepage')
 
class DeleteAlbumView(DeleteView):
     model=models.Album
     template_name= 'delete.html'
     success_url = reverse_lazy('homepage')
     pk_url_kwarg='id'


    
    
         
        