from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect
from alka.forms import CustomerInfoForm, DeliveryAddressForm #, DepositInfoForm
from alka.models import CustomerInfo, DeliveryAddress #, DepositInfo
from django.views.generic import ListView
from django.forms.formsets import formset_factory

class homeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = DeliveryAddress

    def get_context_data(self, **kwargs):
        context = super(homeListView, self).get_context_data(**kwargs)
        return context

def input(request):

    if request.method == "POST":
        info_form = CustomerInfoForm(request.POST)
        address_form = DeliveryAddressForm(request.POST)
        if info_form.is_valid() and address_form.is_valid():
            # 2 model ref: https://stackoverflow.com/questions/28054991/combining-two-forms-in-one-django-view
            #info = info_form.save(commit=False) # commit=False tells Django: "Don't send this to database yet.
            address = address_form.save(commit=False) 
            info = info_form.save()
            address.customer = info
            address.save()
            return redirect("home")
    else:
        info_form = CustomerInfoForm()
        address_form = DeliveryAddressForm()

        return render(request, "alka/input.html", {"in_form": info_form, "add_form": address_form})

