from django.shortcuts import render, redirect, get_object_or_404
from core.models.discount_room_rate import DiscountRoomRate
from core.forms.discount_room_rate_form import DiscountRoomRateForm
from core.forms.filter_discount_room_rate_form import DiscountRoomRateFilterForm
from core.manager.filter_room_rate_manager import FilterRoomRateManager
from core.forms.filter_lowest_room_rate_filter_form import FilterLowestRoomRateForm

def discount_room_rate_list(request):
    discount_room_rates = DiscountRoomRate.objects.all()
    return render(request, 'discount_room_rate_list.html', {'discount_room_rates': discount_room_rates})

def discount_room_rate_create(request):
    if request.method == 'POST':
        form = DiscountRoomRateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discount-room-rate-list')
    else:
        form = DiscountRoomRateForm()
        
    return render(request, 'create_discount_room_rate.html', {'form': form})

def discount_room_rate_edit(request, pk):
    discount_room_rate = get_object_or_404(DiscountRoomRate, pk=pk)
    if request.method == 'POST':
        form = DiscountRoomRateForm(request.POST, instance=discount_room_rate)
        if form.is_valid():
            form.save()
            return redirect('discount-room-rate-list')
    else:
        form = DiscountRoomRateForm(instance=discount_room_rate)
    return render(request, 'edit_discount_room_rate.html', {'form': form, 'discount_room_rate': discount_room_rate})

def discount_room_rate_delete(request, pk):
    discount_room_rate = get_object_or_404(DiscountRoomRate, pk=pk)
    if request.method == 'POST':
        discount_room_rate.delete()
        return redirect('discount-room-rate-list')
    return render(request, 'delete_discount_room_rate.html', {'discount_room_rate': discount_room_rate})

def filter_discount_room_rate(request):
    if request.method == 'POST':
        form = DiscountRoomRateFilterForm(request.POST)
        if form.is_valid():
            room_id = form.cleaned_data['room_id']
            discount = form.cleaned_data['discount']
            # Perform filtering based on room ID and discount
            print(room_id, discount)
            query_set = DiscountRoomRate.objects.all()
            if room_id:
                query_set = query_set.filter(room_rate__room_id=room_id)
            if discount:
                query_set = query_set.filter(discount__discount_name=discount)

            return render(request, 'filter_discount_room_rate.html', {'form': form, 'discount_room_rates': query_set})
    else:
        form = DiscountRoomRateForm()
    
    return render(request, 'filter_discount_room_rate.html', {'form': form})

def filter_lowest_room_rate_view(request):
    if request.method == 'POST':
        mgr = FilterRoomRateManager()
        form = FilterLowestRoomRateForm(request.POST)
        rates_list = []
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            room_id = form.cleaned_data['room_id']

            rates_list = mgr.filter_rooms(start_date=start_date, end_date=end_date, room_id=room_id)

        context = {
                    'form': form,
                    'rates_list': rates_list,
                }
        return render(request, 'filter_lowest_room_rates.html', context)
    else:
        form = FilterLowestRoomRateForm()

    context = {
        'form': form,
    }

    return render(request, 'filter_lowest_room_rates.html', context)
