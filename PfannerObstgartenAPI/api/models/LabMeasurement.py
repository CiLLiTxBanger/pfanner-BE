from django.db import models
from datetime import datetime

class LabMeasurement(models.Model):
    FLAVOR_CHOICES = [
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
    ]

    timestamp = models.DateTimeField(default=datetime.now)
    tree = models.ForeignKey(
                    'Tree',
                    on_delete=models.CASCADE
    )
    strengthMeasurement = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    flavorMeasurement = models.CharField(max_length=30, choices = FLAVOR_CHOICES, blank=True, null=True)
    acidMeasurement = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    sugarMeasurement = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
