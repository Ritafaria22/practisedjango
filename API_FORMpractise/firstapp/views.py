from django.shortcuts import render,redirect
from . forms import contactform
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
 
def djangoform(request):
    if request.method == 'POST':
        form = contactform(request.POST, request.FILES)
        if form.is_valid():
          print(form.cleaned_data)
            
    else:
        form = contactform()
    return render(request, 'djangoform.html', {'form': form})


   
        
       