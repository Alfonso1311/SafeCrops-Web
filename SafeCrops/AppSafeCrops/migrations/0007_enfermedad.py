# Generated by Django 4.2.3 on 2023-07-25 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSafeCrops', '0006_alter_administrador_imagen_alter_experto_imagen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id_Enfermedad', models.AutoField(primary_key=True, serialize=False)),
                ('nombreEnfermedad', models.CharField(max_length=45, verbose_name='Nombre de la Enfermedad')),
                ('cultivoEnfermedad', models.CharField(max_length=45, verbose_name='Cultivo en el que se presenta la enfermedad')),
                ('descripcionEnfermedad', models.TextField(max_length=200, verbose_name='Descripción de la enfermedad')),
                ('curaEnfermedad', models.TextField(max_length=200, verbose_name='Cura de la enfermedad')),
            ],
        ),
    ]
