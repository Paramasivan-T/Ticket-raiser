from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.loginUser, name='login'),
    path('signup/', views.createUser, name='signup'),
    path('logout/', views.logoutUser, name='logout'),

    
]
