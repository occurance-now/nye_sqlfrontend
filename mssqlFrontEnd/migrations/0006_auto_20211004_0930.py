# Generated by Django 3.0.10 on 2021-10-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mssqlFrontEnd', '0005_auto_20211004_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressure',
            name='PressureValue',
            field=models.IntegerField(),
        ),
    ]
