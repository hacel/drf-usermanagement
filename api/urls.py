from django.urls import include, path
from rest_framework.authtoken import views as token

from api import views


urlpatterns = [
    path("user/", views.UserList.as_view()),
    path("user/<int:pk>/", views.UserDetail.as_view()),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("token-auth/", token.obtain_auth_token),
]
