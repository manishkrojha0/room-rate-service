from django.contrib import admin
from core.forms.room_rate_form import RoomRateForm
from core.models.room_rate import RoomRate


# Register your models here.
@admin.register(RoomRate)
class RoomRateAdmin(admin.ModelAdmin):
    model = RoomRate
    list_filter = ['default_rate', 'room_name']
    search_fields = ['room_name', 'room_id']

