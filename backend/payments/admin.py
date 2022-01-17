from django.contrib import admin

from payments.models import Plan, Card, Transaction

admin.site.register([Plan, Card, Transaction])
