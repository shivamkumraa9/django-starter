from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from accounts.serializers import RegisterUserSerializer
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
            return Response({"msg": "Registration success!"},
                            status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
