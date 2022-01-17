from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
import stripe

from accounts.models import CustomUser
from payments.models import Plan

stripe.api_key = settings.STRIPE_SECRET_KEY

@receiver(pre_save, sender=CustomUser)
def attach_subscription(sender, instance, *args, **kwargs):
    plan = Plan.objects.get(name='free')
    instance.stripe_cus_id = stripe.Customer.create()['id']
    instance.plan = plan
