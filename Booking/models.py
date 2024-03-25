from django.db import models

class Bookingmodel(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='PropertyImage/', max_length=100)
