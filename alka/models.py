from django.db import models

# Create your models here.
from django.utils import timezone

class CustomerInfo(models.Model):
    name = models.CharField(max_length = 25)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)

    #message = models.CharField(max_length=300)
    #log_date = models.DateTimeField("date logged")

    #def __str__(self):
        #"""Returns a string representation of a message."""
        #date = timezone.localtime(self.log_date)
        #return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class DeliveryAddress(models.Model):
   customer = models.ForeignKey('CustomerInfo', on_delete = models.CASCADE)
   street = models.CharField(blank = True, max_length = 35)
   city = models.CharField(blank = True, max_length = 15) # change this to a selection with the cities from a list
   zip_code = models.CharField(blank = True, max_length = 5) # have this autofill after the city is selected

#class DepositInfo(models.Model):
#    bottle_type_choices = (
#        (1, '3 gallon plastic'),
#        (2, '3 gallon plastic w spout'),
#        (3, '3 gallon glass'),
#        (4, '5 gallon plastic'),
#        (5, '5 gallon plastic w spout'),
#        (6, '5 gallon glass'),
#        (7, '5 gallon glass w spout'),
#    )

#    customer_id = models.ForeignKey('CustomerInfo', on_delete = models.CASCADE)
#    quantity = models.IntegerField()
#    bottle_type = models.IntegerField(
#        choices = bottle_type_choices,
#        default = bottle_type_choices[0],
#    )
#    deposit = models.DecimalField(max_digits = 5, decimal_places = 2)

#zipcodes 1.0.5 package (pip install zipcodes)
#from pprint import pprint
#import zipcodes

#for x in zipcodes:
    #print(x.zip_code)

