import uuid
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def url_validator(value):
    validate = URLValidator()
    validate(value.strip())

def validate_wl(value):
    validate = URLValidator()
    all_domains = value.split(",")
    for domain in all_domains:
        validate(domain.strip())

class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    redirect_url = models.CharField(max_length=80, blank=True, null=True,
                                    validators=[url_validator])
    white_listed_domains = models.CharField(max_length=100, blank=True,
                                            null=True,
                                            validators=[validate_wl])
    recaptcha_enabled = models.BooleanField(default=False)
    notification_enabled = models.BooleanField(default=False)
    notification_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Submission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    content = models.JSONField()

    def __str__(self):
        return self.form.name
