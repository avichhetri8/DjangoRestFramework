from datetime import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=40, blank=False)
    description = models.TextField(max_length=160, blank=True)
    price = models.IntegerField(blank=False)
    published = models.DateTimeField(blank=True, default=timezone.now)




    def __str__(self):
        return self.title