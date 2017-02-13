from django.contrib import admin

from .models import Ride
from .forms import RideAdminForm
# Register your models here.


class RideAdmin(admin.ModelAdmin):
    form = RideAdminForm

admin.site.register(Ride, RideAdmin)
