# Generated by Django 2.2.3 on 2019-07-08 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0004_pedido_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='productor',
            name='photo',
            field=models.ImageField(blank=True, upload_to='productor_img'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='photo',
            field=models.ImageField(blank=True, upload_to='productor_img'),
        ),
    ]
