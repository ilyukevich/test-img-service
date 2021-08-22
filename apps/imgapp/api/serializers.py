from rest_framework import serializers
from apps.imgapp.models import Category
from apps.imgapp.models import Image


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category"""

    class Meta:
        fields = '__all__'
        model = Category


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for Image"""

    class Meta:
        fields = '__all__'
        model = Image
