from django.contrib.auth import authenticate, login
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from accounts.serializers import (
    RegisterUserSerializer, PasswordResetSerializer, PasswordSerializer,
    ChangePasswordSerializer, ProfileSerializer
)
from accounts.models import User

class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            token = Token.objects.get(user=user)
            return Response({"token": token.key})
        else:
            return Response({"msg": "Invalid Email/Password"},
                            status=status.HTTP_400_BAD_REQUEST)


class Register(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "ok"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfileSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "ok"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data,
                                              user=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class PasswordReset(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.send_email()
            return Response({"msg": "ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirm(APIView):
    def post(self, request, uidb64, token):
        user = self.get_user(uidb64)
        is_valid = default_token_generator.check_token(user, token)

        if user and is_valid:
            serializer = PasswordSerializer(data=request.data, user=user)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "ok"}, status=status.HTTP_200_OK)
            else:
                return Response({"errors": serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"msg": "Invalid Token"},
                            status=status.HTTP_400_BAD_REQUEST)

    def get_user(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user
