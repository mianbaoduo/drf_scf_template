from django.urls import path
from djangodemo.views import index


urlpatterns = [
    path('', index),
]
