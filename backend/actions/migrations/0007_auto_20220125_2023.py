# Generated by Django 3.1.7 on 2022-01-25 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0006_auto_20220123_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[['H', 'Header Name/Value'], ['S', 'Static Key/Value']], max_length=2)),
                ('webhook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actions.webhook')),
            ],
        ),
        migrations.RemoveField(
            model_name='webhookstatic',
            name='webhook',
        ),
        migrations.DeleteModel(
            name='WebhookHeader',
        ),
        migrations.DeleteModel(
            name='WebhookStatic',
        ),
    ]
