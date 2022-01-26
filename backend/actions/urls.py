from django.urls import path

from actions import views

urlpatterns = [
    path("<uuid:pk>/", views.GetActionsView.as_view()),
    
    path("<uuid:pk>/email/", views.CreateEmailActionView.as_view()),
    path("email/<int:pk>/", views.EmailActionView.as_view()),

    path("<uuid:pk>/webhook/", views.CreateWebhookView.as_view()),
    path("webhook/<int:pk>/", views.WebhookView.as_view()),

    path("<int:pk>/key-value/", views.CreateKeyValueView.as_view()),
    path("key-value/<int:pk>/", views.KeyValueView.as_view()),
]
