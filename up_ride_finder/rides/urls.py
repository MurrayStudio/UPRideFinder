from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^(?P<id>[\d+]+)/$',
        view=views.RideDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<id>[\d+]+)/json$',
        view=views.RideJSONView.as_view(),
        name='json'
    ),
    url(
        regex=r'^$',
        view=views.RideListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.RideRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^create/$',
        view=views.RideCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^mine/$',
        view=views.RideDrivingView.as_view(),
        name='driving'
    ),
    url(
        regex=r'^(?P<ride_id>[\d+]+)/request/$',
        view=views.RideRequestCreateView.as_view(),
        name='request'
    ),
    url(
        regex=r'^(?P<ride_id>[\d+]+)/requests/$',
        view=views.RideRideRequestListView.as_view(),
        name='requests'
    ),
    
]
