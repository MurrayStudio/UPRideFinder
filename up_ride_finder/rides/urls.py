from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^(?P<id>[\d+]+)/$',
        view=views.RideDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^$',
        view=views.RideListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^create/$',
        view=views.RideCreateView.as_view(),
        name='create'
    ),
]
