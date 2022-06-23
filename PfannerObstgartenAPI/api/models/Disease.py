from django.db import models

#Krankheit
class Disease(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    scale = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
