
from django.db import models
from django_enum import EnumField

class VehicleType(models.TextChoices):
    CAR = "Car"
    TRUCK = "Truck"
    MOTORCYCLE = "Motorcycle"

    VAN = "Van"


class ParkingSpotType(models.TextChoices):
    COMPACT = "Compact"
    LARGE = "Large"
    MOTORCYCLE = "Motorcycle"
    HANDICAPPED = "Handicapped"


class AccountStatus(models.TextChoices):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    SUSPENDED = "Suspended"

class ParkingTicketStatus(models.TextChoices):
    ACTIVE = "Active"
    PAID = "Paid"
    LOST = "Lost"

class spotStatus(models.TextChoices):
    OCCUPIED = "Occupied"
    VACANT = "Vacant"



class Floor_type(models.TextChoices):
    FIRST = "First"
    SECOND = "Second"
    THIRD = "Third"
    FOURTH = "Fourth"
