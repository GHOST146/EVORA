from django.shortcuts import render

# Create your views here.
def Aboutus(request):
    return render(request,'Aboutus/aboutus.html')