from django.contrib import admin
from forms.models import Form, Submission

admin.site.register([Form, Submission])
