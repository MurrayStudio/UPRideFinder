from django.shortcuts import render

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ride
from .forms import RideCreateForm

# Create your views here.


class RideDetailView(LoginRequiredMixin, DetailView):
    model = Ride
    slug_field = 'id'
    slug_url_kwarg = 'id'
    context_object_name = 'ride'


class RideListView(LoginRequiredMixin, ListView):
    model = Ride
    slug_field = 'id'
    slug_url_kwarg = 'id'
    context_object_name = 'ride_list'


class RideCreateView(LoginRequiredMixin, CreateView):
    model = Ride
    form_class = RideCreateForm
    success_url = reverse_lazy('rides:list')

    def form_valid(self, form):
        """Set the driver to the user submitting this form."""
        form.instance.driver = self.request.user
        return super(RideCreateView, self).form_valid(form)
