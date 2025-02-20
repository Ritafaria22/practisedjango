from django.shortcuts import render,redirect
from . import models
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import Student
# Create your views here.
def home(request):
    student = models.Student.objects.all()#home page a backend er data show kora
    return render(request,"home.html", {'data' : student})

def deletestudent(request,roll):
    std=models.Student.objects.get(pk=roll).delete()
    return redirect("homepage")

def download_file(request, id):
    obj = get_object_or_404(Student, id=id)
    return FileResponse(obj.file_field.open(), as_attachment=True)


 







