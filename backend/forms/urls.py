from django.urls import path
from forms import views

urlpatterns = [
    path("", views.CreateFormView.as_view()),
    path("<uuid:pk>/", views.FormView.as_view()),
    path("<uuid:pk>/submissions/", views.GetSubmissions.as_view()),
    path("submit/<uuid:pk>/", views.SubmitView.as_view()),
]
