from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, CreateAPIView
)

from actions.models import EmailAction, Webhook, KeyValue
from actions.serializers import (
    EmailSerializer, WebhookSerializer, KeyValueSerializer,
)
from forms.models import Form

class GetActionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Form, user=self.request.user,
                                 pk=self.kwargs.get('pk'))

    def get(self, request, pk):
        form = self.get_object()
        email_actions = EmailAction.objects.filter(form=form)
        webhooks = Webhook.objects.filter(form=form)
        response = {
            "emails": EmailSerializer(email_actions, many=True).data,
            "webhooks": WebhookSerializer(webhooks, many=True).data
        }
        return Response(response)


class CreateWebhookView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Form, user=self.request.user,
                                 pk=self.kwargs.get('pk'))

    def post(self, request, pk):
        form = self.get_object()
        headers = request.data.get("headers", [])
        static = request.data.get("static", [])

        w_s = WebhookSerializer(data=request.data)
        h_s = KeyValueSerializer(data=headers, many=True)
        s_s = KeyValueSerializer(data=static, many=True)

        for s in [w_s, h_s, s_s]:
            if not s.is_valid():
                return Response({"errors": s.errors},
                                status=status.HTTP_400_BAD_REQUEST)

        webhook = w_s.save(form=form)
        h_s.save(webhook=webhook)
        s_s.save(webhook=webhook)
        return Response({'id': webhook.pk})


class WebhookView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Webhook.objects.all()
    serializer_class = WebhookSerializer

    def get_object(self):
        return get_object_or_404(Webhook, form__user=self.request.user,
                                 pk=self.kwargs.get('pk'))


class CreateKeyValueView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = KeyValueSerializer

    def perform_create(self, serializer):
        w = get_object_or_404(Webhook, form__user=self.request.user,
                              pk=self.kwargs.get('pk'))
        serializer.save(webhook=w)


class KeyValueView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = KeyValue.objects.all()
    serializer_class = KeyValueSerializer

    def get_object(self):
        return get_object_or_404(
            KeyValue, webhook__form__user=self.request.user,
            pk=self.kwargs.get('pk')
        )


class CreateEmailActionView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmailSerializer

    def perform_create(self, serializer):
        form = get_object_or_404(Form, user=self.request.user,
                                 pk=self.kwargs.get('pk'))
        serializer.save(form=form)


class EmailActionView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = EmailAction.objects.all()
    serializer_class = EmailSerializer

    def get_object(self):
        return get_object_or_404(EmailAction, form__user=self.request.user,
                                 pk=self.kwargs.get('pk'))
