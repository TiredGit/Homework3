from rest_framework import serializers
from App import models

class UserSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    class Meta:
        model = models.User
        fields = '__all__'

    def get_picture(self, obj):
        if models.UserProfile.objects.filter(user=obj).exists() and obj.profile.profile_picture:
            return obj.profile.profile_picture.url
        else:
            return None


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(required=False, allow_null=True)
    class Meta:
        model = models.UserProfile
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = '__all__'

class ShippingAddressSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()
    class Meta:
        model = models.ShippingAddress
        fields = '__all__'

    def get_orders(self, obj):
        orders = models.Order.objects.filter(shipping_address=obj)
        return OrderSerializer(orders, many=True).data


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = models.Order
        fields = '__all__'

    def get_products(self, obj):
        order_products = models.OrderProduct.objects.filter(order=obj)
        products = [order_product.product for order_product in order_products]
        return ProductSerializer(products, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    category_id = serializers.IntegerField(required=False, allow_null=True)
    class Meta:
        model = models.Product
        fields = '__all__'

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = models.OrderProduct
        fields = '__all__'
