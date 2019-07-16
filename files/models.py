from django.db import models
import hashlib
from taggit.managers import TaggableManager


class File(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    public = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)
    file = models.FileField()

    def hash(self):
        file = open(self.file.path, 'rb').read()
        return hashlib.sha512(file).hexdigest()

    def __str__(self):
        return self.name
