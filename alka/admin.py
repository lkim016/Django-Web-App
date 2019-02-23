from django.contrib import admin

# Register your models here.
from .models import CustomerInfo, DeliveryAddress, DepositInfo

admin.site.register(CustomerInfo)
admin.site.register(DeliveryAddress)
admin.site.register(DepositInfo)