from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
]
