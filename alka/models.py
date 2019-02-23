from django.db import models

# Create your models here.
from django.utils import timezone
#import zipcodes

class CustomerInfo(models.Model):
    name = models.CharField(max_length = 25)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)
    # need to input delivery address and deposit info FK (note: maybe don't need to input FKs bc of django's reverse relationship)
    # del_add

    def __str__(self):
        return self.name

    #message = models.CharField(max_length=300)
    #log_date = models.DateTimeField("date logged")

    #def __str__(self):
        #"""Returns a string representation of a message."""
        #date = timezone.localtime(self.log_date)
        #return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class DeliveryAddress(models.Model):

    #zip_object = zipcodes.filter_by(city = 'LOS ANGELES')

    customer = models.ForeignKey('CustomerInfo', on_delete = models.CASCADE, related_name = 'DelCustID')
    street = models.CharField(blank = True, max_length = 35)
    city = models.CharField(blank = True, max_length = 15) # change this to a selection with the cities from a list
    zip_code = models.CharField(blank = True, max_length = 5) # have this autofill after the city is selected


# try to get the cost of the bottle in the array so that I can fill in the deposit amount
class DepositInfo(models.Model):

    bottle_type_choices = (
            (0, '3 gallon plastic'),
            (1, '3 gallon plastic w spout'),
            (2, '3 gallon glass'),
            (3, '5 gallon plastic'),
            (4, '5 gallon plastic w spout'),
            (5, '5 gallon glass'),
            (6, '5 gallon glass w spout'),
        )

    customer = models.ForeignKey('CustomerInfo', on_delete = models.CASCADE, related_name = 'DepCustID')
    quantity = models.IntegerField()
    bottle_type = models.IntegerField(
        choices = bottle_type_choices,
        default = bottle_type_choices[0],
    )
    deposit = models.DecimalField(max_digits = 5, decimal_places = 2, blank = True)





#https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
# OBJECTS
# bt = bottle type
def bottle_cost(bt):
    cost = [12.99, 13.99, 14.99, 15.99, 16.99, 17.99, 18.99]
    return(cost[bt])

#zipcodes 1.0.5 package (pip install zipcodes)
#from pprint import pprint
#import zipcodes

#for x in zipcodes:
    #print(x.zip_code)

# 2/18/19: input list of LA cities and affliated zip codes use
# need to get the cities and zipcode of surrounding area: 
# zip_object = zipcodes.filter_by(city = 'ECHO VILLAGE')
# zip_object.append(zipcodes.filter_by(city = 'LOS ANGELES'))
# zip_object[32]['zip_code']
# zip_code = [[]]
# for x in zip_object:
#    zip_code.append(x['zip_code'])

# zip_object[0]