from rest_framework import permissions
from forms.models import Form
from django.http import Http404

class OnlyOwnerCanAccessForm(permissions.BasePermission):
    """
    Check if user can access the form or not
    """

    def has_permission(self, request, view):
        form_id = view.kwargs['form_id']

        if form_id:
            try:
                request.form_obj = Form.objects.get(id=form_id,
                                                    user=request.user)
                return True
            except Form.DoesNotExist:
                pass
        raise Http404
