from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

import stripe

from accounts.models import User
from payments.models import Plan

stripe.api_key = settings.STRIPE_SECRET_KEY

@receiver(pre_save, sender=User)
def attach_subscription(sender, instance, *args, **kwargs):
    plan = Plan.objects.get(name='free')
    instance.stripe_cus_id = stripe.Customer.create()['id']
    instance.plan = plan

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
