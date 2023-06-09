"""Model file for room rate."""
from django.db import models

# Create your models here.

class RoomRate(models.Model):
    """Model Class for Room Rate."""
    
    room_id = models.IntegerField(unique=True, null=False, blank=False)
    room_name = models.CharField(max_length=250, blank=False, null=False)
    default_rate = models.DecimalField(max_digits=8, decimal_places=2, null=False)

    def __str__(self) -> str:
        return self.room_name