# Generated by Django 2.2.3 on 2021-05-18 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0009_subcategorias_visto'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategorias',
            name='comentarios',
            field=models.CharField(default=0, max_length=10000),
        ),
    ]