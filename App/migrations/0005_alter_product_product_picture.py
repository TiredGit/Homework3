# Generated by Django 4.2.16 on 2024-10-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_product_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(blank=True, default='no_product.png', null=True, upload_to='profile_pictures'),
        ),
    ]