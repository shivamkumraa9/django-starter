from django.contrib import admin
from actions.models import EmailAction, Webhook, KeyValue

admin.site.register([EmailAction, Webhook, KeyValue])
