from django.db import models
from django.db.models import Model
from .EnumType import VehicleType, ParkingSpotType, AccountStatus, ParkingTicketStatus, spotStatus, Floor_type


# Create your models here.
class Base_model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ParkingLot(Base_model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
    parking_floor = models.ForeignKey("ParkingFloor", on_delete=models.CASCADE)
    entry_gate = models.ForeignKey("EntryGate", on_delete=models.CASCADE)
    exit_gate = models.ForeignKey("ExitGate", on_delete=models.CASCADE)


class Gate(Base_model):
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
    operators = models.ForeignKey("Operators", on_delete=models.CASCADE)


class Operators(Base_model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    account_status = models.CharField(max_length=100, choices=AccountStatus.choices, default=AccountStatus.ACTIVE)

    def __str__(self):
        return self.name


class EntryGate(Gate):
    display_board = models.OneToOneField("DisplayBoard", on_delete=models.CASCADE, primary_key=True)




class ExitGate(Gate):
    display_board = models.OneToOneField("DisplayBoard", on_delete=models.CASCADE, primary_key=True)


class DisplayBoard(Base_model):
    name = models.CharField(max_length=100,null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)


class ParkingFloor(models.Model):
    floor_number = models.IntegerField()
    floor_name = models.CharField(max_length=100, choices=Floor_type.choices, default=Floor_type.FIRST)

    # def __int__(self):
    #     return self.floor_number


class PaymentCounter(Base_model):
    name = models.CharField(max_length=100)
    counter_number = models.IntegerField()
    amount = models.IntegerField()
    parking_lot = models.ForeignKey("ParkingLot", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def sum(cls):
        return cls.amount


class ParkingSpot(models.Model):
    name = models.CharField(max_length=100)
    spot_type = models.CharField(max_length=100, choices=ParkingSpotType.choices, default=ParkingSpotType.COMPACT)
    spot_status = models.CharField(max_length=100, choices=spotStatus.choices, default=spotStatus.VACANT)
    parking_floor = models.ForeignKey(ParkingFloor, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name
