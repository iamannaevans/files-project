from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from .models import File

class FileSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = File
        fields = ('id', 'name', 'description', 'public', 'tags', 'file', 'hash')
