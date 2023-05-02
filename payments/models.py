from django.db import models
from parkingapp.models import *
from payments.EnumPayment import *
from parkingapp.EnumType import VehicleType


class Vehicle(models.Model):
    vehicle_id = models.IntegerField()
    vehicle_license_plate = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100, choices=VehicleType.choices, default=VehicleType.CAR)
    vehicle_number = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_color = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_license_plate


class ParkingTicket(models.Model):
    ticket_id = models.IntegerField()
    parkingSpot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    entryTime = models.DateTimeField(auto_now_add=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    entryGate = models.ForeignKey(EntryGate, on_delete=models.CASCADE)
    entryOperator = models.ForeignKey(Operators, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ticket_id)


class Payment(models.Model):
    payment_id = models.IntegerField()
    # invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, choices=PaymentType.choices, default=PaymentType.CASH)
    payment_status = models.CharField(max_length=100, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    payment_amount = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.payment_id)


class Invoice(models.Model):
    invoice_id = models.IntegerField()
    parkingTicket = models.ForeignKey(ParkingTicket, on_delete=models.CASCADE)
    exitTime = models.DateTimeField(auto_now_add=True)
    exitGate = models.ForeignKey(ExitGate, on_delete=models.CASCADE)
    exitOperator = models.ForeignKey(Operators, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.invoice_id)

# Create your models here.
