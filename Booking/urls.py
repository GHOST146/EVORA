from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("Booking/", views.Booking, name = "Booking"),
    
]

