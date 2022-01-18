from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    stripe_id = models.CharField(max_length=50)
    max_submissions = models.IntegerField(default=100)
    allow_webhooks = models.BooleanField(default=True)
    allow_notification = models.BooleanField(default=True)
    allow_email = models.BooleanField(default=True)
    allow_recaptchs = models.BooleanField(default=True)
    allow_uploads = models.BooleanField(default=True)
    upload_limit = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Card(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=20)
    last_four = models.IntegerField()
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return '{} XXXX-XXXX-XXXX-{}'.format(self.brand_name, self.last_four)


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('S', 'Success'),
        ('F', 'Fail')
    ]
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, blank=True,
                             null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    message = models.CharField(max_length=100)

    def __str__(self):
        return "{}: {}".format(self.amount, self.status)
