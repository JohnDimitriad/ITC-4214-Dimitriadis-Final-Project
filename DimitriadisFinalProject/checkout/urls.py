from django.contrib import admin
from django.urls import path
from checkout import views

app_name = 'checkout'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
]
