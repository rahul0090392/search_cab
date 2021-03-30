from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from restapi import views

urlpatterns = [
    path(
        "v1/driver/register/",
        views.DriverRegisterAPI.as_view(),
        name="driver_register_manage",
    ),
    path(
        "v1/driver/<int:driver_id>/sendLocation/",
        views.DriverUpdateLocationAPI.as_view(),
        name="driver_location_update",
    ),
    path(
        "v1/passenger/available_cabs/",
        views.GetNearByDrivers.as_view(),
        name="driver_nearby",
    ),
]


urlpatterns = format_suffix_patterns(urlpatterns)
