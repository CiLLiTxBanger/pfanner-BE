from django.db import models

class AcidMeasurement(models.Model):
#key, value Paare
    SCALE_CHOICES = [
        ("A", "A"),
        ("B", "B"),
        ("C", "B"),
    ]
    scale = models.CharField(max_length=30, choices = SCALE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
