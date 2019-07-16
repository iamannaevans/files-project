from django.shortcuts import render
from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer
import time
import random
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import asyncio
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import _thread

# Create your views here.
def slow():
    time.sleep(random.randint(2, 20))
    return 'something we are waiting for and we need to save it after we have it'

class FileView(viewsets.ModelViewSet, threading.Thread):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            thread = threading.Thread(target=slow)
            thread.start()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
