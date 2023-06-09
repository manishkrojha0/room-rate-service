from django.urls import path
from core.views import room_rate_view, overridden_rate_view, discount_view, home_view, discount_room_rate_view

urlpatterns = [
    path('', home_view.home, name='home'),
    path('room-rate/create/', room_rate_view.room_rate_create, name='room-rate-create'),
    path('room-rate/list/', room_rate_view.room_rate_list, name='room-rate-list'),
    path('overridden-rate/create/', overridden_rate_view.overridden_rate_create, name='overridden-rate-create'),
    path('overridden-rate/list/', overridden_rate_view.overridden_rate_list, name='overridden-rate-list'),
    path('discount/create/', discount_view.discount_create, name='discount-create'),
    path('discount/list/', discount_view.discount_list, name='discount-list'),
    path('room-rate-update/<int:pk>/', room_rate_view.room_rate_update_view, name='room-rate-update'),
    path('room-rate-delete/<int:pk>/', room_rate_view.room_rate_delete_view, name='room-rate-delete'),
    path('overridden-rate-update/<int:pk>/', overridden_rate_view.overridden_rate_update_view, name='overridden-rate-update'),
    path('overridden-rate-delete/<int:pk>/', overridden_rate_view.overridden_rate_delete_view, name='overridden-rate-delete'),
    path('discount/update/<int:pk>/', discount_view.discount_update_view, name='discount-update'),
    path('discount/delete/<int:pk>/', discount_view.discount_delete_view, name='discount-delete'),
    path('discount_room_rates/', discount_room_rate_view.discount_room_rate_list, name='discount-room-rate-list'),
    path('discount_room_rates/create/', discount_room_rate_view.discount_room_rate_create, name='discount_room_rate_create'),
    path('discount_room_rates/<int:pk>/edit/', discount_room_rate_view.discount_room_rate_edit, name='discount_room_rate_edit'),
    path('discount_room_rates/<int:pk>/delete/', discount_room_rate_view.discount_room_rate_delete, name='discount_room_rate_delete'),
    path('filter_discount_room_rate/', discount_room_rate_view.filter_discount_room_rate, name='filter_discount_room_rate'),
    path('filter_rooms/', discount_room_rate_view.filter_lowest_room_rate_view, name='filter_lowest_room_rate'),
]
