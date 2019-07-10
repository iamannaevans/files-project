from rest_framework import serializers
from .models import File

class StringListField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        return ' '.join(data.values_list('name', flat=True))


class FileSerializer(serializers.ModelSerializer):
    tags = StringListField()

    class Meta:
        model = File
        fields = ('id', 'name', 'description', 'public', 'tags', 'file', 'hash')
