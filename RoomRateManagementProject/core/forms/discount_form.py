from django import forms
from core.models.discount import Discount

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['discount_id', 'discount_name', 'discount_type', 'discount_value']
