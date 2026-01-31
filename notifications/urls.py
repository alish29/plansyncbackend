from django.urls import path
from .views import my_notifications

urlpatterns = [
    path("my/", my_notifications),
]
