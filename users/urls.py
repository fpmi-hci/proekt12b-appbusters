from django.urls import path, include
from . import views

urlpatterns = [
    path('api/users/', views.UserCreate.as_view(), name='account-create'),
]