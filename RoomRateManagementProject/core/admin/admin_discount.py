from django.contrib import admin
from core.forms.discount_form import DiscountForm
from core.models.discount import Discount


# Register your models here.
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    form = DiscountForm
    list_filter = ['discount_type']
    search_fields = ['discount_name']


# admin.site.register(Discount, DiscountAdmin)