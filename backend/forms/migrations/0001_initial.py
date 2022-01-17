# Generated by Django 3.1.7 on 2022-01-17 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('redirect_url', models.CharField(blank=True, max_length=80, null=True)),
                ('white_listed_domains', models.CharField(blank=True, max_length=100, null=True)),
                ('recaptcha_enabled', models.BooleanField(default=False)),
                ('notification_enabled', models.BooleanField(default=False)),
                ('notification_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content', models.JSONField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.form')),
            ],
        ),
    ]