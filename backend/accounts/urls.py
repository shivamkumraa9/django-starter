from django.urls import path
from accounts import views

urlpatterns = [
    path("login/", views.Login.as_view()),
    path("register/", views.Register.as_view()),
    path("change-password/", views.ChangePassword.as_view()),
    path('password-reset/', views.PasswordReset.as_view()),
    path('password-reset/<uidb64>/<token>',
         views.PasswordResetConfirm.as_view(), name='password-reset-confirm'),
]
