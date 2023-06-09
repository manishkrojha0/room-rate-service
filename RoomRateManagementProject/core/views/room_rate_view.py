from django.shortcuts import render, redirect, get_object_or_404
from core.forms.room_rate_form import RoomRateForm
from core.models.room_rate import RoomRate
from django.http import HttpResponseBadRequest

def room_rate_create(request):
    if request.method == 'POST':
        form = RoomRateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room-rate-list')
    else:
        form = RoomRateForm()
    return render(request, 'room_rate_create.html', {'form': form})

def room_rate_list(request):
    try:
        room_rates = RoomRate.objects.all()
        print("fgjjjjjjjjjjjj", len(room_rates))
        return render(request, 'room_rate_list.html', {'room_rates': room_rates})
    except Exception as e:
        print(e)
        return HttpResponseBadRequest("Bad request, Please try with valid request.")

def room_rate_update_view(request, pk):
    room_rate = get_object_or_404(RoomRate, pk=pk)
    if request.method == 'POST':
        form = RoomRateForm(request.POST, instance=room_rate)
        print("form=============================================================")
        if form.is_valid():
            form.save()
            return redirect('room-rate-list')
    else:
        form = RoomRateForm(instance=room_rate)
    return render(request, 'room_rate_update.html', {'form': form})

def room_rate_delete_view(request, pk):
    room_rate = get_object_or_404(RoomRate, pk=pk)
    if request.method == 'POST':
        room_rate.delete()
        return redirect('room-rate-list')
    return render(request, 'room_rate_delete.html', {'room_rate': room_rate})



