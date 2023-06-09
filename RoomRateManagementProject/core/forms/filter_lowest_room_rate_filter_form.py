from django import forms
from core.models.room_rate import RoomRate

class FilterLowestRoomRateForm(forms.Form):
    room_id = forms.ModelChoiceField(queryset=RoomRate.objects.values_list('room_id', flat=True), empty_label='None', label='Room ID')
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}))
