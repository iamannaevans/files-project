from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer
import time
import random
from rest_framework.response import Response
from rest_framework import status
import threading


def slow():
    time.sleep(random.randint(2, 20))
    return 'Something we are waiting for.'


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
