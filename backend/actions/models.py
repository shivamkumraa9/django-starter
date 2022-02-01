import re
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class Action(models.Model):
    form = models.ForeignKey("forms.Form", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


EMAIL_REGEX = r'({{.+?}})'

class EmailAction(Action):
    to = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def clean(self):
        try:
            validate_email(self.to)
        except:
            search = re.search(EMAIL_REGEX, self.to)
            if search is None:        
                raise ValidationError({'to': 'To has be a valid email or\
                                       submission field(eg: {{ email }})'})
            self.to = search.group(0)[2:-2].strip()
        return super().clean()
    
    def is_to_email(self):
        try:
            validate_email(self.to)
            return True
        except:
            return False


class Webhook(Action):
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)


class KeyValue(models.Model):
    TYPE_CHOICES = [
        ['H', 'Header Name/Value'],
        ['S', 'Static Key/Value']
    ]
    webhook = models.ForeignKey(Webhook, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)

    def __str__(self):
        return "{}:{}".format(self.webhook.name, self.type)
