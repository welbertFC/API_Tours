from rest_framework.serializers import ModelSerializer
from tourist_point.models import TouristPoint


class TouristPointSerializer(ModelSerializer):
    class Meta:
        model = TouristPoint
        fields = ('id', 'name', 'description')
