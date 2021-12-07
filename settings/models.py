from django.conf import settings
from django.db import models
from datetime import datetime
from django.conf.urls.static import static
from django.urls import reverse	


class Price(models.Model):
	kwh_price = models.FloatField()
	currency_name = models.CharField(max_length=150)
	currency_abbr = models.CharField(max_length=150)
	updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.currency_name