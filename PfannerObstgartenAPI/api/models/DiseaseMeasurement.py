from django.db import models

class DiseaseMeasurement(models.Model):
    value = models.CharField(max_length=50, blank=False)
    orchardMeasurement= models.ForeignKey(
            'OrchardMeasurement',
            on_delete=models.CASCADE
    )
    disease = models.ForeignKey('Disease')
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
