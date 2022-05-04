from django.db import models

class DiseaseMeasurement(models.Model):
    value = models.CharField(max_length=50, blank=False)
    orchardMeasurement_id = models.ForeignKey(
            'OrchardMeasurement',
            on_delete=models.CASCADE
    )
    disease_id = models.ForeignKey(
                'Disease',
                on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('value', )