from django.db import models
from django.utils import timezone

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=250)
    banner = models.URLField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name