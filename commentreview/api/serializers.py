from rest_framework.serializers import ModelSerializer
from commentreview.models import CommentReview


class CommentReviewSerializer(ModelSerializer):
    class Meta:
        model = CommentReview
        fields = ('id', 'user', 'comment', 'date', 'approved')
