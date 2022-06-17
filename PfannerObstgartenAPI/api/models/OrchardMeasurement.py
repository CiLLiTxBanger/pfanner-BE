from django.db import models
import os

class OrchardMeasurement(models.Model):

    PROBABILITY_CHOICES = [
            ("Viel", "Viel"),
            ("Mittel", "Mittel"),
            ("Wenig", "Wenig"),
    ]
    SEASON_CHOICES = [
                ("Frühling", "Frühling"),
                ("Sommer", "Sommer"),
                ("Herbst", "Herbst"),
                ("Winter", "Winter"),
    ]
    PRECIPITATION_CHOICES = [
                ("Trocken", "Trocken"),
                ("Normal", "Normal"),
                ("Feucht", "Feucht"),
        ]

    description = models.TextField()
    tree = models.ForeignKey(
                    'Tree',
                    on_delete=models.CASCADE
    )
    image_photo = models.ImageField(
                    upload_to ='uploads/',
                    blank = True,
                    null = True
    )
    image_description = models.TextField(max_length=180,
                    default=None,
                    blank=True,
                    null=True
    )
    frostSensitivity = models.CharField(max_length=30, choices = PROBABILITY_CHOICES, blank=True, null=True)
    growthHabit = models.CharField(max_length=30, choices = PROBABILITY_CHOICES, blank=True, null=True)
    yieldHabit = models.CharField(max_length=30, choices = PROBABILITY_CHOICES, blank=True, null=True)
    season = models.CharField(max_length=30, choices = SEASON_CHOICES, blank=True, null=True)
    temperature = models.CharField(max_length=30, choices = PROBABILITY_CHOICES, blank=True, null=True)
    precipitation = models.CharField(max_length=30, choices = PRECIPITATION_CHOICES, blank=True, null=True)
    lateFrost = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

        #delete associated file on server when the image object is destroyed
    def delete(self):
        if self.image_photo:
            if os.path.isfile(self.image_photo.path):
                os.remove(self.image_photo.path)
        super().delete()