from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    public = models.BooleanField(default=False)
    file = models.FileField()

    def __str__(self):
        return self.name
