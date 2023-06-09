"""Model file for discount room rate."""
from core.models.discount import Discount
from core.models.room_rate import RoomRate
from django.db import models


class DiscountRoomRate(models.Model):
    """Model class for discount room rate."""

    room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE, null=False)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=False)

    
