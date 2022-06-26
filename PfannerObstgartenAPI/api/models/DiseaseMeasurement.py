from django.db import models

class DiseaseMeasurement(models.Model):
    value = models.CharField(max_length=50, blank=True, null=True, default="-")
    orchardMeasurement= models.ForeignKey(
            'OrchardMeasurement',
            on_delete=models.CASCADE
    )
    disease = models.ForeignKey('Disease', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
