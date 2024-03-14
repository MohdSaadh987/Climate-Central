from django.urls import path

from . import views
from django.contrib import admin

from django.conf import settings

urlpatterns = [
    path("", views.registration_view, name="registration"),
    path('registration_success/', views.registration_success, name='registration_success'),
]