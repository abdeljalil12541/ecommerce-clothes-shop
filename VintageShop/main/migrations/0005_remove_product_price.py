# Generated by Django 4.2.7 on 2023-11-19 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_banner_productattribute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
