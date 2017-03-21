from django.contrib import admin

from .models import Ride, RideRequest
from .forms import RideAdminForm, RideRequestAdminForm
# Register your models here.


class RideAdmin(admin.ModelAdmin):
    form = RideAdminForm


class RideRequestAdmin(admin.ModelAdmin):
    form = RideRequestAdminForm

admin.site.register(Ride, RideAdmin)
admin.site.register(RideRequest, RideRequestAdmin)
