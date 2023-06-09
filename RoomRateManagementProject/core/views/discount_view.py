from django.shortcuts import render, redirect, get_object_or_404
from core.models.discount import Discount
from core.forms.discount_form import DiscountForm
from django.http import HttpResponseBadRequest

def discount_create(request):
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discount-list')
    else:
        form = DiscountForm()
    return render(request, 'discount_create.html', {'form': form})

def discount_list(request):
    try:
        discounts = Discount.objects.all()
        return render(request, 'discount_list.html', {'discounts': discounts})
    except Exception:
        return HttpResponseBadRequest("Bad Request, please try with valid input")
    
def discount_update_view(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    if request.method == 'POST':
        form = DiscountForm(request.POST, instance=discount)
        if form.is_valid():
            form.save()
            return redirect('discount-list')
    else:
        form = DiscountForm(instance=discount)
    return render(request, 'discount_update.html', {'form': form})

def discount_delete_view(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    if request.method == 'POST':
        discount.delete()
        return redirect('discount-list')
    return render(request, 'discount_delete.html', {'discount': discount})