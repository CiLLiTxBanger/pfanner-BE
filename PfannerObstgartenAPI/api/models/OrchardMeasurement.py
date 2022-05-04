from django.db import models

class OrchardMeasurement(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('value', )