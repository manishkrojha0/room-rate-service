from django.contrib import admin
from core.forms.overridden_room_form import OverriddenRoomRateForm
from core.models.overriden_room_rate import OverriddenRoomRate


# Register your models here.
@admin.register(OverriddenRoomRate)
class OverriddenRoomRateAdmin(admin.ModelAdmin):
    form = OverriddenRoomRateForm
    list_filter = ['overridden_room_rate', 'stay_date']
    search_fields = ['room_rate__id']

# admin.site.register(OverriddenRoomRate, OverriddenRoomRateAdmin)


