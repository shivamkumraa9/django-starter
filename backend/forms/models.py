import uuid
from django.db import models


class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    redirect_url = models.CharField(max_length=80, blank=True, null=True)
    white_listed_domains = models.CharField(max_length=100, blank=True,
                                            null=True)
    recaptcha_enabled = models.BooleanField(default=False)
    notification_enabled = models.BooleanField(default=False)
    notification_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.id


class Submission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    content = models.JSONField()

    def __str__(self):
        return self.form.id
