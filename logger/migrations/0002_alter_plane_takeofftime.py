# Generated by Django 3.2.9 on 2022-05-08 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plane',
            name='takeofftime',
            field=models.TimeField(),
        ),
    ]
