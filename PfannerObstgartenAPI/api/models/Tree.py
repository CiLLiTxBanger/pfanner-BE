from django.db import models
from datetime import datetime

class Tree(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    variety = models.ForeignKey(
        'Variety',
        on_delete=models.SET(999999)
    )
    row = models.IntegerField()
    column = models.IntegerField()
    planted_on = models.DateTimeField(default=datetime.now)
    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE
    )
    organic = models.BooleanField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    cut = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)  #auto_now_add -> created time
    edited_on = models.DateTimeField(auto_now=True)   #auto_now -> changes at each update
    
    class Meta:
        ordering = ('row', 'column', )