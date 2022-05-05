from django.db import models

class OrchardMeasurement(models.Model):

    #Not sure if needed
    #timestamp = models.DateTimeField(default=datetime.now)

    description = models.TextField()
    tree = models.ForeignKey(
                    'Tree',
                    on_delete=models.CASCADE
    )
    FrostSensitivity = models.ForeignKey('FrostSensitivity')
    growthHabit = models.ForeignKey('GrowthHabit')
    yieldHabit = models.ForeignKey('YieldHabit')
    season = models.ForeignKey('Season')
    temperature = models.ForeignKey( 'Temperature')
    lateFrost = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)