from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
