from django.shortcuts import render
from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer
import time
import random

# Create your views here.
class FileView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def slow(self, request, *args, **kwargs):
        time.sleep(random.randint(2, 20))
        return super(FileView, self).dispatch(request, *args, **kwargs)
