# Generated by Django 4.2.5 on 2023-12-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_banner_options_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddressbook',
            name='address',
            field=models.TextField(),
        ),
    ]
