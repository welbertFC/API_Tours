from rest_framework.viewsets import ModelViewSet
from tourist_point.models import TouristPoint
from .serializers import TouristPointSerializer


class TouristPointViewSet(ModelViewSet):
    queryset = TouristPoint.objects.all()
    serializer_class = TouristPointSerializer
