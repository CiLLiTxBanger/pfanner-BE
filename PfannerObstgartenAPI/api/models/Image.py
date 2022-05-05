from django.db import models

class Image(models.Model):
    url = models.CharField(max_length=150, blank=False)
    image = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    orchardMeasurement = models.ForeignKey(
            'OrchardMeasurement',
            on_delete=models.CASCADE
    )
    tree = models.ForeignKey(
                'Tree',
                on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
