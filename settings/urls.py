from django.urls import path

from . import views

urlpatterns = [
    path('settings/', views.settings, name="settings"),
]