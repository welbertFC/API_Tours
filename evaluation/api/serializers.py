from rest_framework.serializers import ModelSerializer
from evaluation.models import Evaluation


class EvaluationSerializer(ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('id', 'user', 'comment', 'note', 'date')
