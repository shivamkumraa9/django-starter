from rest_framework import permissions
from forms.models import Form

class HasWebhookPermissions(permissions.BasePermission):
    """
    Check if user's current plan has access of webhook action
    """

    def has_permission(self, request, view):
        return request.user.plan.allow_webhooks


class HasEmailPermissions(permissions.BasePermission):
    """
    Check if user's current plan has access of email action
    """

    def has_permission(self, request, view):
        return request.user.plan.allow_email
