"""Model file of discount."""
from django.db import models
from core.utils.constants import DISCOUNT_TYPES, FIXED

class Discount(models.Model):
    """Discount model class."""

    discount_id = models.PositiveIntegerField(null=False, blank=False, unique=True)
    discount_name = models.CharField(max_length=200, null=False, blank=False)
    discount_type = models.CharField(max_length=250, choices=DISCOUNT_TYPES, default=FIXED)
    discount_value = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    
    def __str__(self) -> str:
        return self.discount_name