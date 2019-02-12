from django.db import models

# Create your models here.
from django.utils import timezone

class CustomerInfo(models.Model):
    name = models.CharField(max_length = 25)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)

class DeliveryAddress(models.Model):
   customer = models.ForeignKey('CustomerInfo', on_delete = models.CASCADE)
   street = models.CharField(blank = True, max_length = 35)
   city = models.CharField(blank = True, max_length = 15) # change this to a selection with the cities from a list
   zip_code = models.CharField(blank = True, max_length = 5) # have this autofill after the city is selected


