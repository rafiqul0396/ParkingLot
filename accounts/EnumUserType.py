from django.db import models


class ProfileType(models.TextChoices):
    CUSTOMER = "Customer"
    PARKING_ATTENDANT = "Parking Attendant"
    ADMIN = "Admin"