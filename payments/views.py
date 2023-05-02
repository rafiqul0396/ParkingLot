import pytz
from django.utils.datetime_safe import datetime
import datetime
from django.utils.timezone import utc
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

from .models import *
from .serailzers import *


# Create your views here.
def getAllPayments(request):
    payments = Payment.objects.all()
    serializers = PaymentSerializer(payments, many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')


def getPayment(request, id):
    payment = Payment.objects.get(id=id)
    serializers = PaymentSerializer(payment)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')


def updatePayment(request):
    return None


def createPayment(request):
    return None


def deletePayment(request, id):
    payment = Payment.objects.get(id=id)
    payment.delete()
    return HttpResponse("Deleted")


# -----------------Ticket-----------------

def getTicket(request, id):
    ticket = ParkingTicket.objects.get(id=id)
    serializers = ParkingTicketSerializer(ticket)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data, content_type='application/json')


def deleteTicket(request, id):
    ticket = ParkingTicket.objects.get(id=id)
    ticket.delete()
    return HttpResponse("Deleted")


def updateTicket(request):
    return None


def createTicket(request):
    return None



def getPrice(request, id):
    ticket = ParkingTicket.objects.get(id=id)

    entry_time = ticket.entryTime
    print(entry_time)
    now=datetime.datetime.now()
    exit_time=now.astimezone(pytz.utc)
    print(exit_time)
    diff = exit_time - entry_time
    print(diff.seconds//3600)
    hr=diff.seconds//3600
    price=hr*10
    print(diff)



    return HttpResponse(price, content_type='application/json')



