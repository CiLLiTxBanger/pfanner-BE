from django.db import models

#Sorte
class Variety(models.Model):
    name = models.CharField(max_length=100, blank=False)
    photo = models.ForeignKey(
                        'Image',
                        on_delete=models.SET_NULL,
                        default=None,
                        blank=True,
                        null=True
    )
    blossom = models.CharField(max_length=180, blank=False)
    fruit = models.CharField(max_length=180, blank=False)
    climate = models.CharField(max_length=180, blank=False)
    pick_maturity = models.CharField(max_length=180, blank=False)
    usage = models.CharField(max_length=250, blank=False)
    bio = models.BooleanField(default=False) #bio sorte???
    pollinator = models.CharField(max_length=250, blank=False)
    properties = models.CharField(max_length=250, blank=False)
    output = models.CharField(max_length=250, blank=False)
    disease_possibility = models.CharField(max_length=250, blank=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )