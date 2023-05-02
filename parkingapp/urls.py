
from django.urls import path
from parkingapp import views

urlpatterns = [
    path("parkingspot/all/", views.getAllParkingSpots, name="getallParkingSpots"),
    path("parkingspot/get/<int:id>", views.getParkingSpot, name="getParkingSpot"),
    path("parkingspot/delete/<int:id>", views.deleteParkingSpot, name="deleteParkingSpot"),
    path("parkingspot/update/<int:id>", views.updateParkingSpot, name="updateParkingSpot"),
    path("parkingspot/create/", views.createParkingSpot, name="createParkingSpot"),

    path("parkingLot/all/", views.getAllParkingLots, name="getallParkingSpots"),
    path("parkingLot/get/<int:id>", views.getParkingSpot, name="getParkingSpot"),
    path("parkingLot/delete/<int:id>", views.deleteParkingSpot, name="deleteParkingSpot"),
    path("parkingLot/update/<int:id>", views.updateParkingSpot, name="updateParkingSpot"),
    path("parkingLot/create/", views.createParkingSpot, name="createParkingSpot"),


    path("parkingFloor/all",views.getparkingFloor,name="getparkingFloor"),
    path("parkingFloor/get/<int:id>",views.getparkingFloorById,name="getparkingFloorById"),

]
