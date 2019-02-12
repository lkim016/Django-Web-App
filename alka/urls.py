from django.urls import path
from alka import views
from alka.models import CustomerInfo

home_list_view = views.homeListView.as_view(
    queryset = CustomerInfo.objects.order_by("name")[:5],  # :5 limits the results to the five most recent
    context_object_name = "info_list",
    template_name="alka/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("input/", views.input, name="input"),
]