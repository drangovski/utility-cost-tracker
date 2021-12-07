from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, date
from devices.models import *
from .models import *
from .forms import *

# Settings
def settings(request):

	price = Price.objects.last()

	form = setPriceCurrencyForm(instance=price)
	if request.method == 'POST':

		form = setPriceCurrencyForm(request.POST, instance=price)
		
		if form.is_valid():
			form.save()
		
			return redirect('settings')


	context = {
		'form': form,
	}


	return render(request, 'settings.html', context)


