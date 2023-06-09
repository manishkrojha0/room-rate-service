from django import forms
from core.models.room_rate import RoomRate

class RoomRateForm(forms.ModelForm):
    class Meta:
        model = RoomRate
        fields = ['room_id', 'room_name', 'default_rate']
