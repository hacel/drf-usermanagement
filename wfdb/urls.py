from django.urls import path
from .views import URLList

urlpatterns = [
    path('', URLList.as_view()),
]
