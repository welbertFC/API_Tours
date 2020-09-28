from django.db import models


class Attractions(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_hours = models.TextField()
    age_min = models.IntegerField()

    def __str__(self):
        return self.name
