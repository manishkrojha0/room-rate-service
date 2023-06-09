from django import forms
from core.models.overriden_room_rate import OverriddenRoomRate

class OverriddenRoomRateForm(forms.ModelForm):
    stay_date = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Define the accepted date formats
        widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        error_messages={
            'invalid': 'Please enter a valid date in the format YYYY-MM-DD.',  # Custom error message for invalid format
        }
    )
    class Meta:
        model = OverriddenRoomRate
        fields = ['room_rate', 'overridden_room_rate', 'stay_date']
