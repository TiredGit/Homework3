from django.db import models


# Create your models here.
# online store
class User(models.Model):
    username = models.CharField(verbose_name='Логин', max_length=255, unique=True)
    email = models.EmailField(verbose_name='Электронная почта пользователя', unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=255)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    name = models.CharField(verbose_name='Имя пользователя', max_length=255)
    surname = models.CharField(verbose_name='Фамилия пользователя', max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    receive_notifications = models.BooleanField(default=True)
    user = models.OneToOneField(User, verbose_name='Пользователь',
                                related_name='profile', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Order(models.Model):
    status_choices = [
        ('new', 'New'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]
    order_number = models.PositiveIntegerField(verbose_name='Номер заказа', unique=True, null=True)
    status = models.CharField(verbose_name='Статус заказа', max_length=255, choices=status_choices, default='new')
    created_at = models.DateTimeField(verbose_name='Дата создания заказа', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения статуса заказа', auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='orders', on_delete=models.CASCADE)
    shipping_address = models.ForeignKey('ShippingAddress', verbose_name='Адрес доставки',
                                         on_delete=models.SET_NULL, blank=True,
                                         null=True, related_name='orders')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.order_number} - {self.created_at}'

    def calculate_products_amount(self):
        return len(self.order_products.all())

    calculate_products_amount.short_description = 'Количество товаров'

    def calculate_total_price(self):
        return sum(order_product.product.price for order_product in self.order_products.all())

    calculate_total_price.short_description = 'Общая цена'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ продукта (промежуточное)'
        verbose_name_plural = 'Заказы продуктов (промежуточные)'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.order} - {self.product}'


class Product(models.Model):
    product_name = models.CharField(verbose_name='Название продукта', max_length=255)
    price = models.FloatField(verbose_name='Цена продукта')
    description = models.TextField(verbose_name='Описание товара', max_length=255, blank=True)
    order = models.ManyToManyField(Order, through='OrderProduct', verbose_name='Заказ',
                                   related_name='products')
    category = models.ForeignKey('ProductCategory', verbose_name='Категория', related_name='products',
                                 blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['product_name']

    def __str__(self):
        return f'{self.product_name} - {self.price}'

    def discount(self):
        return f'{self.product_name} - {self.price*0.5}'


class ShippingAddress(models.Model):
    city = models.CharField(verbose_name='Город', max_length=255)
    street = models.CharField(verbose_name='Улица', max_length=255)
    house_number = models.CharField(verbose_name='Номер дома', max_length=255)
    room_number = models.CharField(verbose_name='Номер квартиры', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'

    def __str__(self):
        return f'{self.city}, {self.street}, {self.house_number}'


class ProductCategory(models.Model):
    category_name = models.CharField(verbose_name='Имя категории', max_length=255)
    category_description = models.TextField(verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'
        ordering = ['category_name']

    def __str__(self):
        return f'{self.category_name}'
