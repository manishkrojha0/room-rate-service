from django import forms
from core.models.room_rate import RoomRate
from core.models.discount_room_rate import DiscountRoomRate

class DiscountRoomRateForm(forms.ModelForm):
    room_id = forms.ModelChoiceField(queryset=RoomRate.objects.values_list('room_id', flat=True), empty_label=None, label='Room ID', required=True)

    class Meta:
        model = DiscountRoomRate
        fields = ['room_id', 'discount']

    
    def save(self, commit=True):
        room_id = self.cleaned_data['room_id']
        room_rate = RoomRate.objects.get(room_id=room_id)
        instance = super().save(commit=False)
        instance.room_rate = room_rate
        if commit:
            instance.save()
        return instance

