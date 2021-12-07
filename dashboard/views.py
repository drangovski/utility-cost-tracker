from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, date
from devices.models import *
from settings.models import *

from django.db.models import Q, Sum

from devices.views import refresh_devices

# Dashboard
def dashboard(request):
	# Check the Cloud state of the devices
	refresh_devices(request)

	# Get all devices
	devices = Device.objects.filter(monitoring=True)

	# Devices count
	devices_count = devices.count()

	# Price per kWh
	price = Price.objects.last()

	# Get the Device Log
	device_log = DeviceLog.objects.all().order_by('-powered_off')

	# Sum total consumption in kWh
	total_kwh = DeviceLog.objects.aggregate(Sum('consumption'))['consumption__sum']

	# Sum total cost
	total_cost = DeviceLog.objects.aggregate(Sum('cost'))['cost__sum']

	context = {
		'devices': devices,
		'device_log': device_log,
		'devices_count': devices_count,
		'price': price,
		'total_kwh': total_kwh,
		'total_cost': total_cost
	}

	return render(request, 'dashboard.html', context)





