from django.db import models
from datetime import datetime

class LabMeasurement(models.Model):

    timestamp = models.DateTimeField(default=datetime.now)
    tree = models.ForeignKey(
                    'Tree',
                    on_delete=models.CASCADE
    )
    strengthMeasurement = models.ForeignKey('StrengthMeasurement', on_delete=models.DO_NOTHING)
    flavorMeasurement = models.ForeignKey('FlavorMeasurement', on_delete=models.DO_NOTHING)
    acidMeasurement = models.ForeignKey('AcidMeasurement', on_delete=models.DO_NOTHING)
    sugarMeasurement = models.ForeignKey('SugarMeasurement', on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
