# Generated by Django 4.2.3 on 2023-08-24 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSafeCrops', '0020_alter_dataset_estadodataset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='estadoDataset',
        ),
    ]
