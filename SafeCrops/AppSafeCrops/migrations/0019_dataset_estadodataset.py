# Generated by Django 4.2.3 on 2023-08-24 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSafeCrops', '0018_remove_dataset_estadodataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='estadoDataset',
            field=models.BooleanField(default=True, verbose_name='Estado del dataset'),
        ),
    ]
