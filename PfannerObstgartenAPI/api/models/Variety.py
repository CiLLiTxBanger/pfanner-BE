from django.db import models

#Sorte
class Variety(models.Model):
    name = models.CharField(max_length=50, blank=False)
    blossom = models.CharField(max_length=100, blank=False)
    fruit = models.CharField(max_length=100, blank=False)
    climate = models.CharField(max_length=100, blank=False)
    pick_maturity = models.CharField(max_length=100, blank=False)
    usage = models.CharField(max_length=100, blank=False)
    bio = models.BooleanField(default=False)
    pollinator = models.CharField(max_length=100, blank=False)
    properties = models.CharField(max_length=100, blank=False)
    output = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )