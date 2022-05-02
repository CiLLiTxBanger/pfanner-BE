from django.db import models

class Tree(models.Model):
    type = models.CharField(max_length=50, blank=False)
    variety_id = models.ForeignKey(
        'Variety',
        on_delete=models.CASCADE,
    )
    row = models.IntegerField()
    column = models.IntegerField()
    planted_on = models.DateTimeField(auto_now_add=True)
    location_id = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE
    )
    organic = models.BooleanField()
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    cut = models.CharField(max_length=50, blank=False)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='trees', on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(auto_now_add=True)  #auto_now_add -> created time
    edited_on = models.DateTimeField(auto_now=True)   #auto_now -> changes at each update
    
    class Meta:
        ordering = ('row', 'column', )