from django.db import models

class OrchardMeasurement(models.Model):

    #Not sure if needed
    #timestamp = models.DateTimeField(default=datetime.now)

    description = models.TextField()
    tree = models.ForeignKey(
                    'Tree',
                    on_delete=models.CASCADE
    )
    photo = models.ForeignKey(
                    'Image',
                    on_delete=models.SET_NULL,
                    default=None,
                    blank=True,
                    null=True
    )
    frostSensitivity = models.ForeignKey('FrostSensitivity', on_delete=models.DO_NOTHING)
    growthHabit = models.ForeignKey('GrowthHabit', on_delete=models.DO_NOTHING)
    yieldHabit = models.ForeignKey('YieldHabit', on_delete=models.DO_NOTHING)
    season = models.ForeignKey('Season', on_delete=models.DO_NOTHING)
    temperature = models.ForeignKey( 'Temperature', on_delete=models.DO_NOTHING)
    lateFrost = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)