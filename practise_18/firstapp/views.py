from django.shortcuts import render,redirect
from . import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth  import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#Create your views here.
 

def home(request):
    return render(request, 'home.html')
def signup(request):
    if request.method == 'POST':
        signup_form= forms.SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account created successfully !!')
            return redirect('signup')
        
    else:
        sign_form = forms.SignupForm()
    return render(request, 'signup.html', {'form' : sign_form, 'type':'Register'})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form= AuthenticationForm(request, request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user= authenticate(username=user_name, password=user_pass)#check korbe user er data ache kina j login korte chai
                if user is not None:
                    messages.success(request, 'Logged in successfully !!')
                    login(request,user) #user login korlo
                    return redirect('profile')
            
            else:
                messages.warning(request, ' Log in information is incorrect !!!')
                return redirect('signup')    
        else:
            form= AuthenticationForm()# empty form dibe
            return render(request, 'signup.html', {'form': form, 'type':'Login' })

def user_logout(request) :
    logout(request)
    return redirect('login')

@login_required            
def profile(request):
    return render(request, 'profile.html')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            form = PasswordChangeForm(user=request.user, data = request.POST)#data er modde user er shb data pass korlam
            if form.is_valid():
                form.save()
                messages.success(request, 'password updated successfully !!')
                update_session_auth_hash(request, form.cleaned_data['user'])
                return redirect('profile')
        else:
            form= PasswordChangeForm(user=request.user)
        return render(request, 'pass_change.html', {'form':form})
    
    else:
        return redirect('login')


def pass_change2(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            form = SetPasswordForm(user=request.user, data = request.POST)#data er modde user er shb data pass korlam
            if form.is_valid():
                form.save()
                messages.success(request, 'password updated successfully !!')
                update_session_auth_hash(request, form.cleaned_data['user'])
                return redirect('profile')
        else:
            form= SetPasswordForm(user=request.user)
        return render(request, 'pass_change.html', {'form':form})
    else:
        return redirect('login')






   