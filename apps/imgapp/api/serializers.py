from rest_framework import serializers
from apps.imgapp.models import Category
from apps.imgapp.models import Image


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category"""

    class Meta:
        #fields = '__all__'
        fields = ['id', 'name', 'name', 'url']
        model = Category
        extra_kwargs = {
            'url': {
                'view_name': 'api:category-detail'
            },
        }


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for Image"""

    class Meta:
        #fields = '__all__'
        fields = ['id', 'author', 'category', 'name', 'slug',
                  'image', 'description', 'available', 'created', 'updated', 'url']
        model = Image
        extra_kwargs = {
            'url': {
                'view_name': 'api:images-detail'
            },
        }
