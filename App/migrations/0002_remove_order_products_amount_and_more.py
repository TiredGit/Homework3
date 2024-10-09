# Generated by Django 5.1.1 on 2024-10-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.PositiveIntegerField(null=True, unique=True, verbose_name='Номер заказа'),
        ),
        migrations.AlterField(
            model_name='product',
            name='order',
            field=models.ManyToManyField(related_name='products', through='App.OrderProduct', to='App.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
    ]