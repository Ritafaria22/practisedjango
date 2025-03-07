from django.urls import path
from . import views
urlpatterns = [
    path('signup/',  views.signup, name='signup'),
    path('userlogin/',  views.UserLoginView.as_view(), name='userlogin'),
    path('logout/',  views.user_logout, name='logout'),
    path('add/', views.AddMusicianCreateView.as_view() , name='add_musician'),
    path('edit/<int:id>/', views.EditMusicianView.as_view(), name='edit_musician'),
   
]
