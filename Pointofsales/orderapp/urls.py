from django.urls import path
from .views import order_list_view, edit_order, delete_order

urlpatterns = [
    path('', order_list_view, name='orderlist'),
    path('edit/<int:id>/', edit_order, name='edit_order'),
    path('delete/<int:id>/', delete_order, name='delete_order'),
]
