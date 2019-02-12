from django import forms
from alka.models import CustomerInfo, DeliveryAddress #, DepositInfo

# blog: https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
# django documentation:
# html template: https://docs.djangoproject.com/en/2.1/topics/forms/
# forms from models: https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/
#                     https://stackoverflow.com/questions/28054991/combining-two-forms-in-one-django-view
# formsets: https://docs.djangoproject.com/en/1.7/topics/forms/formsets/
# model field ref: https://docs.djangoproject.com/en/2.1/ref/models/fields/

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ("name", "phone", "email",)   # NOTE: the trailing comma is required
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = DeliveryAddress
        fields = ("street", "city", "zip_code",)   # NOTE: the trailing comma is required
        labels = {
            'zip_code': 'Zip Code'
        }
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
        }

#class DepositInfoForm(forms.ModelForm): # change this into a formset
#    class Meta:
#        model = DepositInfo
#        fields = ("bottle_type", "quantity", "deposit",)   # NOTE: the trailing comma is required