from django import forms
from alka.models import CustomerInfo, DeliveryAddress #, DepositInfo

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        #fields = '__all__'  # NOTE: the trailing comma is required
        exclude = ("id",)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = DeliveryAddress
        #fields = '__all__'
        exclude = ("customer",)   # NOTE: the trailing comma is required
        labels = {
            'zip_code': 'Zip Code'
        }
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
