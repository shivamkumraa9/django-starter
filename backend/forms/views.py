from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)

from forms.models import Form, Submission
from forms.serializers import FormSerializer, SubmissionSerializer

class CreateFormView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FormSerializer

    def get_queryset(self):
        return Form.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FormView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def get_object(self):
        return get_object_or_404(Form, user=self.request.user,
                                 pk=self.kwargs.get('pk'))


class SubmitView(APIView):
    pass


class GetSubmissions(APIView):
    pass
