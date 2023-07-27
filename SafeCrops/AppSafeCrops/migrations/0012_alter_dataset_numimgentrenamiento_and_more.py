# Generated by Django 4.2.3 on 2023-07-26 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSafeCrops', '0011_alter_administrador_imagen_alter_experto_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='numImgEntrenamiento',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de imágenes de entrenamiento'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='numImgTotal',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de imágenes totales'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='numImgValidacion',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de imágenes de validación'),
        ),
    ]
