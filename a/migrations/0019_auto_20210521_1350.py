# Generated by Django 2.2.3 on 2021-05-21 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0018_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariosubcategoria',
            name='fecha',
            field=models.CharField(default=datetime.date(2021, 5, 21), max_length=10),
        ),
        migrations.AlterField(
            model_name='subcategorias',
            name='fecha',
            field=models.CharField(default=datetime.date(2021, 5, 21), max_length=10),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imgPerfil',
            field=models.ImageField(default='https://d500.epimg.net/cincodias/imagenes/2016/07/04/lifestyle/1467646262_522853_1467646344_noticia_normal.jpg', upload_to='Perifl'),
        ),
    ]