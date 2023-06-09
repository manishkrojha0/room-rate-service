from django.contrib import admin
from core.models.discount_room_rate import DiscountRoomRate
from django.contrib.admin.views.main import ChangeList
from core.models.overriden_room_rate import OverriddenRoomRate
from core.forms.discount_room_rate_form import DiscountRoomRateForm



@admin.register(DiscountRoomRate)
class RoomRateDiscountAdmin(admin.ModelAdmin):
    model = DiscountRoomRate
    list_display = ('room_id', 'room_name', 'discount')
    list_filter = ['room_rate__over_ridden_rate__stay_date', 'room_rate__room_id', 'discount']
    search_fields = ['room_rate__room_id']

    def room_id(self, obj):
        room_id = obj.room_rate.room_id
        return room_id
    
    def room_name(self, obj):
        return obj.room_rate.room_name
    
    room_id.short_description = 'Room Id'
    room_name.short_description = 'Room Name'

    