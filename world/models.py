from django.contrib.gis.db import models


class BikeStation(models.Model):
    location = models.CharField(max_length=250)
    coordinates = models.PointField()
    type = models.CharField(max_length=50)
    security = models.CharField(max_length=50)
    no_stands = models.CharField(max_length=25)

    def __str__(self):
        return self.location
