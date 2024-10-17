"""
URL configuration for models project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from App import views
from models import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products_list/', views.ProductsList.as_view(), name='products_list'),
    path('products/<int:pk>/', views.ProductsDetail.as_view(), name='product_details'),
    path('products/<int:pk>/update/', views.ProductsUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductsDelete.as_view(), name='product_delete'),
    path('products/create/', views.ProductsCreate.as_view(), name='product_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
