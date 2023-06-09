from django.shortcuts import render, redirect, get_object_or_404
from core.models.overriden_room_rate import OverriddenRoomRate
from core.forms.overridden_room_form import OverriddenRoomRateForm
from django.http import HttpResponseBadRequest


def overridden_rate_create(request):
    if request.method == 'POST':
        form = OverriddenRoomRateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('overridden-rate-list')
    else:
        form = OverriddenRoomRateForm()
    return render(request, 'overridden_rate_create.html', {'form': form})

def overridden_rate_list(request):
    try:
        overridden_rates = OverriddenRoomRate.objects.all()
        return render(request, 'overridden_rate_list.html', {'overridden_rates': overridden_rates})
    except:
        return HttpResponseBadRequest("Bad Request, Please try again with valid request.")

def overridden_rate_update_view(request, pk):
    overridden_rate = get_object_or_404(OverriddenRoomRate, pk=pk)
    if request.method == 'POST':
        form = OverriddenRoomRateForm(request.POST, instance=overridden_rate)
        if form.is_valid():
            form.save()
            return redirect('overridden-rate-list')
    else:
        form = OverriddenRoomRateForm(instance=overridden_rate)
    return render(request, 'overridden_rate_update.html', {'form': form})

def overridden_rate_delete_view(request, pk):
    overridden_rate = get_object_or_404(OverriddenRoomRate, pk=pk)
    if request.method == 'POST':
        overridden_rate.delete()
        return redirect('overridden-rate-list')
    return render(request, 'overridden_rate_delete.html', {'overridden_rate': overridden_rate})