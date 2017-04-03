from datetime import datetime

from django.shortcuts import render, redirect

from django.http import JsonResponse, HttpResponseForbidden

from django.forms.models import model_to_dict

from django.core.exceptions import PermissionDenied

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ride, RideRequest
from .forms import RideCreateForm, RideRequestCreateForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

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
    # List 10 items per page.
    # See https://docs.djangoproject.com/en/1.10/topics/pagination/
    paginate_by = 10

    def get_queryset(self):
        """Sort the rides by creation date or by departure date
        depending on the 'order_by' URL param. By default, sort
        rides by those created soonest."""
        order_by = self.request.GET.get('order_by')
        future_rides = Ride.objects.filter(when__gte=datetime.today())
        if order_by != "departure_date":
            return future_rides.order_by('-created_date')
        return future_rides.order_by('when')


class RideJSONView(LoginRequiredMixin, DetailView, ):
    model = Ride
    slug_field = 'id'
    slug_url_kwarg = 'id'
    context_object_name = 'ride'

    def render_to_response(self, context, **response_kwargs):
        ride = Ride.objects.get(id=self.kwargs.get('id'))
        return JsonResponse(model_to_dict(ride, fields=['dest_name', 'origin_name']))
        # return JsonResponse({'dest_name': ride.dest_name, 'origin_name':
        # ride.origin_name})


class RideCreateView(LoginRequiredMixin, CreateView):
    model = Ride
    form_class = RideCreateForm
    success_url = reverse_lazy('rides:list')

    def form_valid(self, form):
        """Set the driver to the user submitting this form."""
        form.instance.driver = self.request.user
        return super(RideCreateView, self).form_valid(form)


class RideRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse_lazy(
            'rides:detail', kwargs={'id': self.request.ride.id})


class RideDrivingView(LoginRequiredMixin, ListView):
    """View that lists only the rides the current user is the driver for."""
    model = Ride

    def get_queryset(self):
        return Ride.objects.filter(
            driver__exact=self.request.user).order_by('-created_date')


class RideRequestCreateView(LoginRequiredMixin, CreateView):
    model = RideRequest
    form_class = RideRequestCreateForm
    # ride = Ride.objects.get(id=self.kwargs.get('ride_id'))

    def get_ride(self):
        return Ride.objects.get(id=self.kwargs.get('ride_id'))

    # def dispatch(self, request, *args, **kwargs):
    #     if self.get_ride().driver == self.request.user or self.get_ride().riderequest_set:
    #         # TODO: Implement error messages
    # return redirect(reverse_lazy('rides:detail', kwargs={'id':
    # self.kwargs.get('ride_id')}))

    def form_valid(self, form):
        # print(self.kwargs.get('ride_id'))
        form.instance.ride = Ride.objects.get(id=self.kwargs.get('ride_id'))
        form.instance.requester = self.request.user
        form.send_email()
        return super(RideRequestCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('rides:detail', kwargs={'id': self.kwargs.get('ride_id')})

    # def send_email(self, request):
    #     if request.method == 'GET':
    #         form = ContactForm()
    #     else:
    #         form = ContactForm(request.POST)
    #         if self.form_valid(form):
    #             subject = request.POST.get('subject', 'Request for a ride')
    #             message = request.POST.get('message', 'Test Message')
    #             from_email = request.POST.get('from_email', 'murrays17@up.edu')
    #             try:
    #                 send_mail(subject, message, from_email, ['admin@example.com'])
    #             except BadHeaderError:
    #                 return HttpResponse('Invalid header found.')
    #             return HttpResponseRedirect('detail')
    #         else:
    #             return render(request, "/rides/home.html")


class RideRideRequestListView(LoginRequiredMixin, ListView):
    model = RideRequest
    slug_field = 'ride_id'
    slug_url_kwarg = 'ride_id'
    context_object_name = 'request_list'
    template_name = 'rides/ride_requests.html'
    # List 10 items per page.
    # See https://docs.djangoproject.com/en/1.10/topics/pagination/
    paginate_by = 10

    def get_queryset(self):
        ride = Ride.objects.get(id=self.kwargs.get('ride_id'))
        # Only a ride's driver can view a ride's requests
        if ride.driver != self.request.user:
            raise PermissionDenied
        return ride.riderequest_set.all()
