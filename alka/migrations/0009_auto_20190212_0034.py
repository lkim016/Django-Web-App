# Generated by Django 2.1.5 on 2019-02-12 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alka', '0008_auto_20190211_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='depositinfo',
            name='customer_id',
        ),
        migrations.DeleteModel(
            name='DeliveryAddress',
        ),
        migrations.DeleteModel(
            name='DepositInfo',
        ),
    ]
