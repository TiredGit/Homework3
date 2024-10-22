import factory
from random import choice
from factory.django import ImageField

from App import models
from App.models import Order


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')

    class Meta:
        model = models.User


class UserProfileFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    profile_picture = ImageField()
    receive_notifications = factory.Faker('boolean')
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = models.UserProfile


class ProductCategoryFactory(factory.django.DjangoModelFactory):
    category_name = factory.Faker('sentence')
    category_description = factory.Faker('text')

    class Meta:
        model = models.ProductCategory


class ShippingAddressFactory(factory.django.DjangoModelFactory):
    city = factory.Faker('city')
    street = factory.Faker('street_name')
    house_number = factory.Faker('random_int', min=1, max=1000)
    room_number = factory.Faker('random_int', min=1, max=1000)

    class Meta:
        model = models.ShippingAddress


class OrderFactory(factory.django.DjangoModelFactory):
    order_number = factory.Faker('random_int', min=1, max=10000)
    status = factory.LazyFunction(lambda: choice([x[0] for x in Order.status_choices]))
    created_at = factory.Faker('date_time')
    updated_at = factory.Faker('date_time')
    user = factory.SubFactory(UserFactory)
    shipping_address = factory.SubFactory(ShippingAddressFactory)

    class Meta:
        model = models.Order


class ProductFactory(factory.django.DjangoModelFactory):
    product_name = factory.Faker('sentence')
    price = factory.Faker('pyfloat', positive='True', min_value=1, max_value=1000000)
    description = factory.Faker('text')
    category = factory.SubFactory(ProductCategoryFactory)
    product_picture = ImageField()

    class Meta:
        model = models.Product


class OrderProductFactory(factory.django.DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    created_at = factory.Faker('date_time')

    class Meta:
        model = models.OrderProduct
