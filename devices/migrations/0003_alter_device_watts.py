# Generated by Django 3.2.9 on 2021-12-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_device_watts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='watts',
            field=models.IntegerField(null=True),
        ),
    ]