from django.conf import settings
from django.db import models
from datetime import datetime
from django.conf.urls.static import static
from django.urls import reverse	


class Device(models.Model):
	name = models.CharField(max_length=150)
	device_id = models.CharField(max_length=150)
	status = models.BooleanField(default=False)
	watts = models.IntegerField(null=True)
	monitoring = models.BooleanField(default=False)
	powered_on = models.DateTimeField(blank=True, null=True)
	powered_off = models.DateTimeField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.name

class DeviceLog(models.Model):
	device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="device")
	powered_on = models.DateTimeField(blank=True, null=True)
	powered_off = models.DateTimeField(blank=True, null=True)
	consumption = models.FloatField(blank=True, null=True)
	cost = models.FloatField(blank=True, null=True)