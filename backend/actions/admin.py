from django.contrib import admin
from actions.models import Email, Webhook, KeyValue

admin.site.register([Email, Webhook, KeyValue])
