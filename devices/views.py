from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, date
from .models import *
from settings.models import *

from django.db.models import Q

from .forms import *

# Import Logging
import logging

# Import connection configurayion (.env file) & import TuyaOpenAPI and Logger
from .env import ACCESS_ID, ACCESS_KEY, API_ENDPOINT
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

# Uncomment this if you want to Debug Tuya Cloud Functions
#TUYA_LOGGER.setLevel(logging.DEBUG)

# Connect to TuyaOpenAPI
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Refresh Devices
def refresh_devices(request):
	# Fetch all available Devices
	all_devices = openapi.get("/v1.2/iot-03/devices")
	all_devices = all_devices['result']['list']

	# Loop through all fetched devices and save/update them in the database
	for device in all_devices:
		device_id = device['id']
		name = device['name']

		# Check the Cloud state of the device
		dev = openapi.get('/v1.0/iot-03/devices/{}/status'.format(device_id))
		state = dev['result'][0]['value']

		obj, created = Device.objects.update_or_create(
			device_id=device_id, defaults={'name': name, 'status':state}
		)

def power_device(request, device_id):
	today = datetime.now()
	# Get a device
	device = get_object_or_404(Device, device_id=device_id)

	# Check if device is powered on/off
	if device.status:
		commands = {'commands': [{'code': 'switch_1', 'value': False}]}
		device.status = False
		device.save()

		# Update Powered Off time in Device model
		obj, created = Device.objects.update_or_create(
			device_id=device_id, defaults={'powered_off': today}
		)

		# Caluclate consumption
		started = device.powered_on
		ended = today

		# difference between the start and the end of an activity in seconds
		dur = ended - started
		duration = dur.total_seconds()

		# convert duration to hours
		hours = duration / 3600

		# calculate device kilowatts
		kilowatts = device.watts / 1000

		# calculate kilowatt-hours
		kwh = hours * kilowatts

		# caluclate the activity session cost
		price = Price.objects.last()
		kwh_price = price.kwh_price
		cost = kwh * kwh_price

		# Create DeviceLog entry with each active session of a device
		DeviceLog.objects.create(device_id=device.id, powered_on=device.powered_on, powered_off=today, consumption=kwh, cost=cost)

	else:
		commands = {'commands': [{'code': 'switch_1', 'value': True}]}
		device.status = True
		device.save()

		# Update Powered On time in Device model
		obj, created = Device.objects.update_or_create(
			device_id=device_id, defaults={'powered_on': today}
		)
		

	# Send the commands for powering on/off
	openapi.post('/v1.0/iot-03/devices/{}/commands'.format(device_id), commands)

	return redirect(request.META['HTTP_REFERER'])


def devices(request):
	refresh_devices(request)

	devices = Device.objects.all()

	form = setWattsForm()
	if request.method == 'POST':

		form = setWattsForm(request.POST)

		if form.is_valid():
			device_id = request.POST.get('device_id')
			watts = form.cleaned_data['watts']
			monitoring = True

			Device.objects.filter(device_id=device_id).update_or_create(device_id=device_id, defaults={'watts': watts, 'monitoring': monitoring})


			return redirect('devices')

		else:
			print('Not valid')


	context = {
		'devices': devices,
		'form': form
	}

	return render(request, 'devices.html', context)


def monitor_device(request, device_id):
	# Get a device
	device = get_object_or_404(Device, device_id=device_id)

	if device.monitoring:
		device.monitoring = False
		device.save()

	else:
		device.monitoring = True
		device.save()

	return redirect(request.META['HTTP_REFERER'])