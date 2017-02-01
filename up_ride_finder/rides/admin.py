from django.contrib import admin

from .models import Ride
from .forms import RideForm
# Register your models here.


class RideAdmin(admin.ModelAdmin):
    form = RideForm

admin.site.register(Ride, RideAdmin)
