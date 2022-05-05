from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
