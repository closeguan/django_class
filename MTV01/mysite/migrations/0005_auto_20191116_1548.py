# Generated by Django 2.2.7 on 2019-11-16 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=15),
        ),
    ]
