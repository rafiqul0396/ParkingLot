from django.contrib import admin

from .models import Payment, ParkingTicket, Invoice, Vehicle



admin.site.register(Payment)
admin.site.register(ParkingTicket)
admin.site.register(Invoice)
admin.site.register(Vehicle)


# Register your models here.
