from django.urls import path
from alka import views
from alka.models import CustomerInfo, DeliveryAddress, DepositInfo

home_list_view = views.homeListView.as_view(
    #.order_by("id")[:5],  # :5 limits the results to the five most recent
    # purpose: just show the customer's information and on-click then have the more specific information pull up like the address and deposit info
    queryset = CustomerInfo.objects.all().prefetch_related('DelCustID') | CustomerInfo.objects.all().prefetch_related('DepCustID'), # merge querysets
    context_object_name = "info_list",
    template_name="alka/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("input/", views.input, name="input"),
]

