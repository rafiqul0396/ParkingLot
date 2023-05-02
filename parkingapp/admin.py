from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ParkingLot)

admin.site.register(PaymentCounter)
admin.site.register(EntryGate)
admin.site.register(ExitGate)
admin.site.register(DisplayBoard)
admin.site.register(Operators)
admin.site.register(Address)


@admin.register(ParkingFloor)
class ParkingFloorAdmin(admin.ModelAdmin):
    list_display = ('id','floor_name','floor_number')


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ('id','name','spot_type','spot_status','parking_floor')


