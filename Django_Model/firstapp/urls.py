from django.urls import path

from . import views 
 
urlpatterns = [
    path('', views.home, name="homepage"),
    path('delete/<int:roll>', views.deletestudent, name="deletestudent"),
    #path('upload/', upload_file, name='upload_file'),
    path('download/<int:id>/', views.download_file, name='download_file'),
]
