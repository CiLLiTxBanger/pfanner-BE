from django.db import models

class OrchardMeasurement(models.Model):

    description = models.CharField(max-length= 800)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)