
from django.urls import path

from payments import views
from payments.views import*


urlpatterns = [
    path("all/", views.getAllPayments, name="getAllPayments"),
    path("get/<int:id>", views.getPayment, name="getPayment"),
    path("delete/<int:id>", views.deletePayment, name="deletePayment"),
    path("update/<int:id>", views.updatePayment, name="updatePayment"),
    path("create/", views.createPayment, name="createPayment"),



    path("createTicket/", views.createTicket, name="createTicket"),
    path("getTicket/<int:id>", views.getTicket, name="getTicket"),
    path("updateTicket/<int:id>", views.updateTicket, name="updateTicket"),
    path("deleteTicket/<int:id>", views.deleteTicket, name="deleteTicket"),
    path("getPrice/<int:id>", views.getPrice, name="getPrice"),

    ]
    
