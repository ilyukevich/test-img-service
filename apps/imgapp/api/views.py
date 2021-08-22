from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer, ImageSerializer
from ..models import Category, Image


class CategoryView(viewsets.ModelViewSet):
    """Viewsets for Category"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated,]


class ImageView(viewsets.ModelViewSet):
    """Viewsets for Image"""

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated,]
