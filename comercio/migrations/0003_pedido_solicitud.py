# Generated by Django 2.2.3 on 2019-07-07 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0002_auto_20190706_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('detalle', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('pyme', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
