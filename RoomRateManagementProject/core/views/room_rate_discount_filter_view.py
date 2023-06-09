from django.shortcuts import render
from core.forms.room_rate_filter_form import RoomRateFilterForm
from core.models.discount_room_rate import DiscountRoomRate
from core.manager.filter_room_rate_manager import FilterRoomRateManager


def room_rates_filer(request):
    form = RoomRateFilterForm(request.GET)
    room_rates = []

    if form.is_valid():
        room_id = form.cleaned_data['room_id']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        pass
        # from core.manager.


    # context = {'form': form, 'room_rates': room_rates}
    # return render(request, 'room_rates.html', context)

