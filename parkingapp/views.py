import io
import json
from pprint import pp
import sched, time
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.core import serializers as pintu
from django.http import JsonResponse

from .models import *
from .serializers import *
from rest_framework import viewsets
#
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import  Response


def getAllParkingSpots(request):
    spots = ParkingSpot.objects.all()
    serializers = ParkingSpotSerializer(spots, many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')


def getParkingSpot(request, id):
    spots = ParkingSpot.objects.get(id=id)
    serializers = ParkingSpotSerializer(spots)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')


def deleteParkingSpot(request, id):
    spots = ParkingSpot.objects.get(id=id)
    spots.delete()
    return HttpResponse("Deleted")


@csrf_exempt
def updateParkingSpot(request, id):
    if request.method == 'PUT':
        spots = ParkingSpot.objects.get(id=id)
        received_json_data = request.body
        stream = io.BytesIO(received_json_data)
        pythondata = JSONParser().parse(stream)
        serializers = ParkingSpotSerializer(spots, data=pythondata)
        if serializers.is_valid():
            serializers.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def createParkingSpot(request):
    received_json_data = request.body
    stream = io.BytesIO(received_json_data)
    pythondata = JSONParser().parse(stream)
    serializers = ParkingSpotSerializer(data=pythondata)
    if serializers.is_valid():
        serializers.save()
        res = {'msg': 'Data Created'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    print(request.body)


#--------------------------------------------------------------


# Path: ParkingLot\urls.py


def createParkingLot(request):
    received_json_data = request.body
    stream = io.BytesIO(received_json_data)
    pythondata = JSONParser().parse(stream)
    serializers = ParkingLotSerializer(data=pythondata)
    if serializers.is_valid():
        serializers.save()
        res = {'msg': 'Data Created'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    print(request.body)
def do_something(scheduler):
    # schedule the next call first
    scheduler.enter(60, 1, do_something, (scheduler,))
    print("Doing stuff...")

def getAllParkingLots(request):
    print("Getting")
    my_scheduler = sched.scheduler(time.time, time.sleep)
    my_scheduler.enter(60, 1, do_something, (my_scheduler,))
    my_scheduler.run()

    data=do_something()
    return HttpResponse(data, content_type='application/json')

            #return HttpResponse(json_data, content_type='application/json')
        # then do your stuff





def getParkingLot(request, id):
    spots = ParkingLot.objects.get(id=id)
    serializers = ParkingLotSerializer(spots)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')


def deleteParkingLot(request, id):
    spots = ParkingLot.objects.get(id=id)
    spots.delete()
    return HttpResponse("Deleted")


@csrf_exempt
def updateParkingLot(request, id):
    if request.method == 'PUT':
        spots = ParkingLot.objects.get(id=id)
        received_json_data = request.body
        stream = io.BytesIO(received_json_data)
        pythondata = JSONParser().parse(stream)
        serializers = ParkingLotSerializer(spots, data=pythondata)
        if serializers.is_valid():
            serializers.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')



#--------------------------------------------------------------

def getparkingFloor(request):
    floors = ParkingFloor.objects.all()
    serializers = ParkingFloorSerializer(floors, many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')

def getparkingFloorById(request, id):
    floors = ParkingFloor.objects.filter(id=id).values()
    # print(floors)
    # nn = pintu.serialize('json',floors)

    rafik={}
    for i in floors:
        # print(i)
        name = i['floor_number']
        spot = ParkingSpot.objects.filter(id=name).values()
        for j in spot:
           return JsonResponse(j)
