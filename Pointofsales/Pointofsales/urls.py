"""
URL configuration for Pointofsales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from orderapp.views import order_list_view
#from Traditionalapp.views import customer_list_view
#from Digitalapp.views import product_list_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',order_list_view),
    #path('',customer_list_view),
    #path('',product_list_view),
    # ✅ now '/' will load product page
    path('product/', include('Digitalapp.urls')),
    path('customer/', include('Traditionalapp.urls')),
    path('order/', include('orderapp.urls')),

    # path('order/', include('orderapp.urls'))  # if you create later
]
