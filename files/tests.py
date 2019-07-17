from .models import File
from rest_framework import status
from rest_framework.test import APITestCase
import json
import tempfile


class FileTests(APITestCase):
    def test_upload_file(self):
        with tempfile.TemporaryDirectory() as temporary_dir:
            with self.settings(MEDIA_ROOT=temporary_dir):
                file = tempfile.NamedTemporaryFile()
                file.write(b'This is a file.')
                file.seek(0)

                response = self.client.post('/files/', {
                    'name': 'myfile',
                    'description': 'this is my file',
                    'public': True,
                    'tags': json.dumps([]),
                    'file': file
                })

                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(File.objects.count(), 1)
                self.assertEqual(File.objects.get().name, 'myfile')
