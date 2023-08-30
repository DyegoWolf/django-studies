from django.urls import path
from core.views import index, contact

urlpatterns = [
    path('', index),
    path('contato/', contact)
]