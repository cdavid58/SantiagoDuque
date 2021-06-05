# Generated by Django 2.2.3 on 2021-05-22 23:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0022_comentariosubcategoria_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='respuestasComentariosSubcategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('fecha', models.CharField(default=datetime.date(2021, 5, 22), max_length=10)),
                ('like', models.CharField(max_length=20)),
                ('comentario', models.TextField()),
                ('csc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a.comentarioSubCategoria')),
            ],
        ),
    ]
