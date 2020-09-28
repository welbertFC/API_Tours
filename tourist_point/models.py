from django.db import models
from attractions.models import Attractions
from commentreview.models import CommentReview
from evaluation.models import Evaluation
from location.models import Location


class TouristPoint(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions)
    comment = models.ManyToManyField(CommentReview)
    evaluation = models.ManyToManyField(Evaluation)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
