# Generated by Django 2.2.3 on 2021-05-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentariosubcategoria',
            name='comentario',
            field=models.TextField(default=''),
        ),
    ]
