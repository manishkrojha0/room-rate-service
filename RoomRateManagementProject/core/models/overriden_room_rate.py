"""Model class for overridden room rate."""
from django.db import models
from core.models.room_rate import RoomRate

class OverriddenRoomRate(models.Model):
    """model class for overridden room rate."""

    room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE, related_name='over_ridden_rate')
    overridden_room_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    stay_date = models.DateField(null=False, blank=False)

    def __str__(self) -> str:
        return self.room_rate.room_name + "_overridden_room_rate"