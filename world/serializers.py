from rest_framework import serializers
from .models import BikeStation
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class BikeStationSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = BikeStation
        geo_field = "coordinates"
        fields = ('location', 'type', 'security', 'no_stands')
