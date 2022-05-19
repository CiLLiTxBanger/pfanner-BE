from django.db import models

class Image(models.Model):
    photo = models.ImageField(
            upload_to ='uploads/',
            blank = True,
            null = True
    )
    description = models.CharField(max_length=180,
            default=None,
            blank=True,
            null=True
    )

    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
