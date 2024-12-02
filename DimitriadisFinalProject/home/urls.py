from django.contrib import admin
from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('home/', views.home, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
]