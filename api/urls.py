from django.urls import path
from .views import DetailAPI

urlpatterns = [
    path('api', DetailAPI.as_view()),
]