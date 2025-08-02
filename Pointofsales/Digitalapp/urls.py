from django.urls import path
from Digitalapp.views import product_list_view, edit, delete  # ✅ renamed import

urlpatterns = [
    path('', product_list_view, name='productlist'),  # ✅ lowercase name for clarity
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
]
