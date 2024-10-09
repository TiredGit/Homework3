from django.contrib import admin
from App import models
from .models import OrderProduct

# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'profile_picture')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'status', 'created_at', 'updated_at',
                    'calculate_products_amount', 'calculate_total_price')
    inlines = [OrderProductInline]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price')


@admin.register(models.OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product')


@admin.register(models.ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'house_number', 'room_number')


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
