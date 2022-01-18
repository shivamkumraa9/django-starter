from rest_framework import serializers
from accounts.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6)
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'password']
