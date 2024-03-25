from django.shortcuts import render
from .models import Bookingmodel

def Booking(request):
    queryset = Bookingmodel.objects.filter(email=request.user.email).order_by('date')


    return render(request,'Booking/booking.html', {'objects_list': queryset,})