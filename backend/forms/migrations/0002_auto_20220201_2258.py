# Generated by Django 3.1.7 on 2022-02-01 17:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='redirect_url',
            field=models.CharField(blank=True, max_length=80, null=True, validators=[django.core.validators.URLValidator]),
        ),
    ]
