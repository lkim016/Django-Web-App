# Generated by Django 2.1.4 on 2019-02-12 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alka', '0011_auto_20190212_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=35)),
                ('city', models.CharField(blank=True, max_length=15)),
                ('zip_code', models.CharField(blank=True, max_length=5)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alka.CustomerInfo')),
            ],
        ),
    ]
