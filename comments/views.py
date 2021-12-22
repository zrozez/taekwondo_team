from rest_framework import serializers
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Comments
from .serializers import CommentSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]
