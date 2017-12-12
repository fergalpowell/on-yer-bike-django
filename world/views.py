from django.shortcuts import render

# Create your views here.
import csv
from django.template.loader import get_template
from django.contrib.gis.geos import fromstr
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import BikeStation
from .serializers import BikeStationSerializer


def load_map(request):
    csv_file = 'world/data/stations.csv'
    my_csv = csv.reader(open(csv_file))

    for line in my_csv:
        if line[1] != 'X':
            my_long_lat = str(line[1] + " " + line[2])
            _, created = BikeStation.objects.get_or_create(
                location=line[5],
                coordinates=fromstr('POINT(' + my_long_lat + ')'),
                type=line[0],
                security=line[10],
                no_stands=line[24]
            )
    t = get_template('map.html')
    html = t.render()
    return HttpResponse(html)


@csrf_exempt
def bike_station_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        bike_stations = BikeStation.objects.all()
        serializer = BikeStationSerializer(bike_stations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BikeStationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def bike_station_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        bike_station = BikeStation.objects.get(pk=pk)
    except BikeStation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BikeStationSerializer(bike_station)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BikeStationSerializer(bike_station, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bike_station.delete()
        return HttpResponse(status=204)
