from django.db import models

#Aromagehalt
class FlavorMeasurement(models.Model):
    scale = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('scale', )