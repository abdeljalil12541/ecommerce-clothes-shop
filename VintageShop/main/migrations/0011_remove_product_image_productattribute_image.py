# Generated by Django 4.2.5 on 2023-11-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_product_color_remove_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='productattribute',
            name='image',
            field=models.ImageField(null=True, upload_to='product_imgs/'),
        ),
    ]