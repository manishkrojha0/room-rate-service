from django import forms
from core.models.room_rate import RoomRate
from core.models.discount import Discount

class DiscountRoomRateFilterForm(forms.Form):
    room_id = forms.ModelChoiceField(queryset=RoomRate.objects.values_list('room_id', flat=True), empty_label='All', required=False, label='Room ID', initial=None)
    discount = forms.ModelChoiceField(queryset=Discount.objects.values_list('discount_name', flat=True), required=False, label='Discount', initial=None)

    def __init__(self, *args, **kwargs):
        super(DiscountRoomRateFilterForm, self).__init__(*args, **kwargs)
        self.fields['room_id'].empty_label = 'None'
