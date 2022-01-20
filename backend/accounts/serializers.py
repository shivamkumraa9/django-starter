from rest_framework import serializers
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.conf import settings

from accounts.models import User
from accounts.send_mail import send as send_email

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


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def get_user(self):
        """
        This method returns the user associated with the email
        """
        email = self.validated_data['email']

        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
    
    def send_email(self):
        """
        Send the one time password reset link to the user 
        """
        user = self.get_user()
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            url = settings.PASSWORD_RESET_URL
            link = f"{url}/{uid}/{token}"

            subject = "Password Reset Email"
            body = """<h1>Reset Password link</h1>
                      <p>
                         Click this link to reset the password 
                         <a href="{}">{}</a>
                      </p>""".format(link, link)

            send_email(user.email, subject, body)


class PasswordSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(min_length=6)
    new_password2 = serializers.CharField(min_length=6)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def validate(self, data):
        """
        Check if password1 and password2 are same
        """
        password1 = data['new_password1']
        password2 = data['new_password2']
        if (password1 and password2) and (password1 == password2):
            return super().validate(data)
        errors = {"password1": "Passwords not matched",
                  "password2": "Passwords not matched"}
        raise serializers.ValidationError(errors)

    def save(self):
        """
        Set the new password to user
        """
        password = self.validated_data["new_password1"]
        self.user.set_password(password)
        self.user.save()
        return self.user


class ChangePasswordSerializer(PasswordSerializer):
    old_password = serializers.CharField(min_length=6)

    def validate(self, data):
        """
        Check if the old password is correct or not
        """
        old_password = data["old_password"]
        if not self.user.check_password(old_password):
            raise serializers.ValidationError({"old_password":
                                               "Invalid Password"})
        return super().validate(data)
