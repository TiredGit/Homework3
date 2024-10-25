from django.contrib import admin
from django.urls import path

from App import views
from models import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register('users', views.UserAPI, basename='users')
router.register('products', views.ProductAPI, basename='products')
router.register('profiles', views.UserProfileAPI, basename='profiles')
router.register('categories', views.CategoryAPI, basename='categories')
router.register('addresses', views.ShippingAddressAPI, basename='addresses')
router.register('orders', views.OrderAPI, basename='orders')
router.register('order_product', views.OrderProductAPI, basename='order_product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('products_list/', views.ProductsList.as_view(), name='products_list'),
    path('products/<int:pk>/', views.ProductsDetail.as_view(), name='product_details'),
    path('products/<int:pk>/update/', views.ProductsUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductsDelete.as_view(), name='product_delete'),
    path('products/create/', views.ProductsCreate.as_view(), name='product_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls
