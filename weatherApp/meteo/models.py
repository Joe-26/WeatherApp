from django.db import models

# Create your models here.
class WorldCities(models.Model):
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    lat = models.FloatField()
    lng = models.FloatField()
    #id = models.IntegerField(blank=False, primary_key=True, null=False)
    
    # This is a string representation of the WorldCities
    def __str__(self):
        return (f"\nID:{self.id}\nLocation: {self.city}, {self.country}\nCoordinates: {self.lat}, {self.lng}")
    
