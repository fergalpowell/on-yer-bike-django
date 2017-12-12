from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView
from .models import BikeStation
from . import views

urlpatterns = [
    url(r'^$', views.load_map, name='BikeStation'),
    url(r'^data/$', GeoJSONLayerView.as_view(model=BikeStation, properties='location, coordinates, type,'
                                                                           ' security, no_stands'),
        name='data'),
    url(r'^stations/$', views.bike_station_list),
    url(r'^station/(?P<pk>[0-9]+)/$', views.bike_station_detail),
]