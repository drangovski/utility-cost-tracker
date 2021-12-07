from django.db import models
from .models import *
from django import forms

class setWattsForm(forms.Form):
	watts = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Insert device Watts'}))


