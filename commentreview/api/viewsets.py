from rest_framework.viewsets import ModelViewSet
from commentreview.models import CommentReview
from .serializers import CommentReviewSerializer


class CommentReviewViewSet(ModelViewSet):
    queryset = CommentReview.objects.all()
    serializer_class = CommentReviewSerializer
