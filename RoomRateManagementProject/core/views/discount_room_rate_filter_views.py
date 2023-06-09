from django.shortcuts import render
from core.models.discount_room_rate import DiscountRoomRate
from core.forms.discount_room_rate_form import DiscountRoomRateForm

def discount_room_rate_list(request):
    form = DiscountRoomRateForm(request.GET)
    discount_room_rates = DiscountRoomRate.objects.all()

    if form.is_valid():
        room_id = form.cleaned_data['room_id']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']

        if room_id:
            discount_room_rates = discount_room_rates.filter(room_rate__room_id=room_id)
        if start_date and end_date:
            discount_room_rates = discount_room_rates.filter(room_rate__over_ridden_rate__stay_date__range=(start_date, end_date))

    context = {
        'form': form,
        'discount_room_rates': discount_room_rates,
    }

    return render(request, 'discount_room_rate_list.html', context)
