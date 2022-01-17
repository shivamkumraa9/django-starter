from django.db import models


class Action(models.Model):
    form = models.ForeignKey("forms.Form", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Email(Action):
    to = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    body = models.TextField()


class Webhook(Action):
    pass


class KeyValue(models.Model):
    TYPE_CHOICES = [
        ['A', 'Auth Username/Password'],
        ['H', 'Header Name/Value'],
        ['S', 'Static Key/Value']
    ]
    webhook = models.ForeignKey(Webhook, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)

    def __str__(self):
        return "{}:{}".format(self.webhook.name, self.type)

# r'({{.+?}})'
