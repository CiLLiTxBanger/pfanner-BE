from django.db import models

class AcidMeasurement(models.Model):
    scale = models.DecimalField(max_digits=4, decimal_places=1)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
