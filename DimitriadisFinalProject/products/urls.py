from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.product, name='product'),
    path('addproduct/', views.addproduct, name='addproduct'),
]