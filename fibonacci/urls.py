from django.urls import path
from .views import Fibonacci

urlpatterns = [
    path('fibonacci', Fibonacci.as_view(), name='fibonacci'),
]