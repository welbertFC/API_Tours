from django.db import models


class Location(models.Model):
    line1 = models.CharField(max_length=150, null=True, blank=True)
    line2 = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.city
