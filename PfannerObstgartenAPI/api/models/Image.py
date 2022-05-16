from django.db import models

class Image(models.Model):
    url = models.CharField(max_length=150, blank=False)
    photo = models.ImageField(
            upload_to ='uploads/',
            blank = True,
            null = True
    )
    orchardMeasurement = models.ForeignKey(
            'OrchardMeasurement',
            on_delete=models.CASCADE
    )
    #blank allows you to pass it a null value, but null tells the database to accept null values
    variety = models.ForeignKey(
                'Variety',
                on_delete=models.CASCADE,
                default=None,
                blank=True,
                null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
