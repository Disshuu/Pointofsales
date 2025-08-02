# Traditionalapp/urls.py
from django.urls import path
from .views import customer_list_view, edit_customer, delete_customer

urlpatterns = [
    path('', customer_list_view, name='customerlist'),
    path('edit/<int:id>/', edit_customer, name='edit_customer'),
    path('delete/<int:id>/', delete_customer, name='delete_customer'),
]
