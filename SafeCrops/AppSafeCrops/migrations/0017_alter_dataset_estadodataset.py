# Generated by Django 4.2.3 on 2023-08-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSafeCrops', '0016_dataset_estadodataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='estadoDataset',
            field=models.BooleanField(default=True, verbose_name='Estado del dataset'),
        ),
    ]
