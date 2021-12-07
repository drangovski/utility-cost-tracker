from django.urls import path

from . import views

urlpatterns = [
    path('devices/', views.devices, name="devices"),
    path('power/<device_id>', views.power_device, name="power_device"),
    path('monitor/<device_id>', views.monitor_device, name="monitor_device"),
]