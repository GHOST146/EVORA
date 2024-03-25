from django.db import models

class Property(models.Model):
    property_name = models.CharField(max_length=100)
    residence_type = models.CharField(max_length=50)
    tenure_type = models.CharField(max_length=50)
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    furnishing = models.CharField(max_length=50)
    extra_facilities = models.IntegerField()
    size = models.DecimalField(max_digits=8, decimal_places=2)
    location_category = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='PropertyImage/', max_length=100)
    image2 = models.ImageField(upload_to='PropertyImage/', max_length=100)
    image3 = models.ImageField(upload_to='PropertyImage/', max_length=100)