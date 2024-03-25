"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Evora/', include('Homepage.urls')),
    path('Evora/', include('Signup.urls')),
    path('Evora/', include('Login.urls')),
    path('Evora/', include('Buy.urls')),
    path('Evora/', include('ForgotPassword.urls')),
    path('Evora/', include('Profile.urls')),
    path('Evora/', include('Buydetails.urls')),
    path('Evora/', include('Aboutus.urls')),
    path('Evora/', include('Rent.urls')),
    path('Evora/', include('Rentdetails.urls')),
    path('Evora', include('ChangePassword.urls')),
    path('Evora/', include('Booking.urls')),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)