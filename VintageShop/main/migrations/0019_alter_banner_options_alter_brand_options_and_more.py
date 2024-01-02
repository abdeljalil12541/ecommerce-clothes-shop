# Generated by Django 4.2.5 on 2023-12-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_productreview_options_alter_whishlist_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': '01. Banners'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': '03. Brands'},
        ),
        migrations.AlterModelOptions(
            name='cartorder',
            options={'verbose_name_plural': '08. Orders'},
        ),
        migrations.AlterModelOptions(
            name='cartorderitems',
            options={'verbose_name_plural': '09. Order Items'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '02. Categories'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': '04. Colors'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '06. Products'},
        ),
        migrations.AlterModelOptions(
            name='productattribute',
            options={'verbose_name_plural': '07. ProductAttributes'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name_plural': '05. Sizes'},
        ),
        migrations.AddField(
            model_name='useraddressbook',
            name='mobile',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='useraddressbook',
            name='address',
            field=models.CharField(max_length=1500),
        ),
    ]
