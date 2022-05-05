from django.db import models

class OrchardMeasurement(models.Model):

    description = models.TextField()
    tree = models.ForeignKey(
                    'Tree',
                    on_delete=models.CASCADE
    )
    FrostSensitivity = models.ForeignKey(
                    'FrostSensitivity',
                    on_delete=models.CASCADE
    )
    growthHabit = models.ForeignKey(
                    'GrowthHabit',
                    on_delete=models.CASCADE
    )
    yieldHabit = models.ForeignKey(
                    'YieldHabit',
                    on_delete=models.CASCADE
    )
    season = models.ForeignKey(
                    'Season',
                    on_delete=models.CASCADE
    )
    temperature = models.ForeignKey(
                    'Temperature',
                    on_delete=models.CASCADE
    )
    lateFrost = BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)