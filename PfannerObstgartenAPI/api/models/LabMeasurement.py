from django.db import models

class LabMeasurement(models.Model):

    tree = models.ForeignKey(
                    'Tree',
                    on_delete=models.CASCADE
    )
    strengthMeasurement = models.ForeignKey(
                    'StrengthMeasurement',
                    on_delete=models.CASCADE
    )
    flavorMeasurement = models.ForeignKey(
                    'FlavorMeasurement',
                    on_delete=models.CASCADE
    )
    acidMeasurement = models.ForeignKey(
                     'AcidMeasurement',
                     on_delete=models.CASCADE
    )
    sugarMeasurement = models.ForeignKey(
                    'SugarMeasurement',
                    on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
