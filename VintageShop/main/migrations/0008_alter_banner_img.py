# Generated by Django 4.2.5 on 2023-11-20 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_banner_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(max_length=200, upload_to='banner_imgs'),
        ),
    ]
