from rest_framework import serializers

from actions.models import EmailAction, Webhook, KeyValue

class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailAction
        exclude = ('form', )


class KeyValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyValue
        exclude = ('webhook', )


class WebhookSerializer(serializers.ModelSerializer):
    headers = serializers.SerializerMethodField()
    static = serializers.SerializerMethodField()

    class Meta:
        model = Webhook
        exclude = ('form', )
    
    def get_headers(self, obj):
        headers = KeyValue.objects.filter(webhook=obj, type='H')
        return KeyValueSerializer(headers, many=True).data
    
    def get_static(self, obj):
        static = KeyValue.objects.filter(webhook=obj, type='S')
        return KeyValueSerializer(static, many=True).data
    