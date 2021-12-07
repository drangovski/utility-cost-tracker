from django.db import models
from .models import *
from django import forms

class setPriceCurrencyForm(forms.ModelForm):
	kwh_price = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Insert price'}))
	currency_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insert currency name'}))
	currency_abbr = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insert abbreviation or symbol'}))

	class Meta:
		model = Price
		fields = ("kwh_price", "currency_name", "currency_abbr" )

		def __init__(self, *args, **kwargs):
			super(setPriceCurrencyForm, self).__init__(*args, **kwargs)

