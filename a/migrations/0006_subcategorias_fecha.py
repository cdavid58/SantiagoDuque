# Generated by Django 2.2.3 on 2021-05-18 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0005_subcategorias_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategorias',
            name='fecha',
            field=models.CharField(default=datetime.date(2021, 5, 18), max_length=10),
        ),
    ]
