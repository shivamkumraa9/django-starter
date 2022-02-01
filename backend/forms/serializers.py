from rest_framework import serializers
from forms.models import Form, Submission

class FormSerializer(serializers.ModelSerializer):

    def validate_recaptcha_enabled(self, value):
        plan = self.context['request'].user.plan
        if not plan.allow_recaptchs:
            raise serializers.ValidationError("Upgrade to enable this")
        return value

    def validate_notification_enabled(self, value):
        plan = self.context['request'].user.plan
        if not plan.allow_notification:
            raise serializers.ValidationError("Upgrade to enable this")
        return value

    class Meta:
        model = Form
        exclude = ('user', )


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
