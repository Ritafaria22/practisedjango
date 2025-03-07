from .forms import RegisterForm
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator #login required er kaj er jnno
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from . import models
from . import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash

@method_decorator(login_required, name='dispatch')
class AddMusicianCreateView(CreateView):
    model = models.Musician
    form_class = forms.Musicianform
    template_name = 'add_mucisian.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.musician= self.request.user
        return super().form_valid(form)
 
class EditMusicianView(UpdateView):
        model=models.Musician
        form_class= forms.Musicianform
        template_name= 'add_album.html'
        pk_url_kwarg='id'
        success_url = reverse_lazy('homepage')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            messages.success(request, "Signup successful!")
            return redirect('homepage')  # Ensure 'homepage' is correctly defined
        else:
            messages.error(request, "Signup failed. Please check your inputs.")
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


class UserLoginView(LoginView):
    template_name='login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')

    def form_valid(self,form):
         messages.success(self.request, 'logged in successful')
         return super().form_valid(form)
    
    def form_invalid(self,form):
         messages.success(self.request, 'logged in information is incorrect')
         return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Login'
        return context

 
def user_logout(request):
    logout(request)
    return redirect('userlogin')
