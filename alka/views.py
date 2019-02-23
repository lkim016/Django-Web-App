from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect
from alka.forms import CustomerInfoForm, DeliveryAddressForm, DepositInfoForm
from alka.models import CustomerInfo, DeliveryAddress, DepositInfo
from django.views.generic import ListView
from django.forms.formsets import formset_factory
from alka.functions import calculate

class homeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = CustomerInfo

    def get_context_data(self, **kwargs):
        context = super(homeListView, self).get_context_data(**kwargs)
        return context

# https://stackoverflow.com/questions/569468/django-multiple-models-in-one-template-using-forms
def input(request):
    info_form = CustomerInfoForm(request.POST or None)
    address_form = DeliveryAddressForm(request.POST or None)
    deposit_form = DepositInfoForm(request.POST or None)

    if request.method == "POST":
        if info_form.is_valid() and address_form.is_valid() and deposit_form.is_valid():
            # CustomerInfoForm instance
            info = info_form.save()
            address = address_form.save(commit=False) # commit=False tells Django: "Don't send this to database yet."
            deposit = deposit_form.save(commit=False)
            # DeliveryAddressForm instance
            address.customer = info
            address.save()
            # DepositInfoForm instance
            deposit.customer = info
            deposit.deposit = calculate(deposit.quantity, deposit.bottle_type)
            deposit.save()
            return redirect("home")
    else:
        return render(request, "alka/input.html", {"in_form": info_form, "add_form": address_form, "dep_form": deposit_form})



#def home(request):
    #info_form = CustomerInfoForm(request.POST or None)
    #address_form = DeliveryAddressForm(request.POST or None)
    #deposit_form = DepositInfoForm(request.POST or None)

    #if request.method == "POST":
        #if info_form.is_valid(): #and address_form.is_valid() and deposit_form.is_valid():
            #customer = info_form.save(commit=False) # commit=False tells Django: "Don't send this to database yet.
            #info.save()
            #return redirect("home")

            # need to check the input of the form to see if the form is put into an object so that I can combine the 3 form inputs on 'POST'
            #customer = info_form.cleaned_data['name']
            #return render(request, "alka/home.html", {"result": customer})
    #else:
        #return render(request, "alka/home.html", {"in_form": info_form, "add_form": address_form, "dep_form": deposit_form})