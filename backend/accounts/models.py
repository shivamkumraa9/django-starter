from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=False, blank=True,
                                null=True)
    email = models.EmailField(unique=True)
    stripe_cus_id = models.CharField(max_length=50)
    stripe_sub_id = models.CharField(max_length=50, blank=True, null=True)
    plan = models.ForeignKey('payments.Plan', on_delete=models.SET_NULL,
                                      blank=True, null=True)
    is_cancelled = models.BooleanField(default=False)
    next_billing = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
