# Generated by Django 3.1.7 on 2022-02-01 17:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20220201_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='redirect_url',
            field=models.CharField(default='', max_length=80, validators=[django.core.validators.URLValidator]),
            preserve_default=False,
        ),
    ]
