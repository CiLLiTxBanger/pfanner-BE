from django.db import models

class LabMeasurement(models.Model):

    timestamp = models.DateTimeField(default=datetime.now)
    tree = models.ForeignKey(
                    'Tree',
                    on_delete=models.CASCADE
    )
    strengthMeasurement = models.ForeignKey('StrengthMeasurement')
    flavorMeasurement = models.ForeignKey('FlavorMeasurement')
    acidMeasurement = models.ForeignKey('AcidMeasurement')
    sugarMeasurement = models.ForeignKey('SugarMeasurement')
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
