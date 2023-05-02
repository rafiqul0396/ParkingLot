from django.db import models
from django_enum import EnumField


class PaymentType(models.TextChoices):
    CASH = "Cash"
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    PAYPAL = "Paypal"
    BITCOIN = "Bitcoin"
    OTHER = "Other"

class PaymentStatus(models.TextChoices):
    PENDING = "Pending"
    COMPLETE = "Complete"
    CANCELLED = "Cancelled"
    REFUNDED = "Refunded"