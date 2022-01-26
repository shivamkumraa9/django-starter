# Generated by Django 3.1.7 on 2022-01-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_auto_20220120_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='webhook',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='keyvalue',
            name='type',
            field=models.CharField(choices=[['H', 'Header Name/Value'], ['S', 'Static Key/Value']], max_length=2),
        ),
    ]
