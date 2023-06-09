"""Manager file to filter the room rate."""
from django.db.models import F, Value, Case, When, Max, DecimalField, FloatField, ExpressionWrapper
from core.models.discount_room_rate import DiscountRoomRate
from core.models.overriden_room_rate import OverriddenRoomRate
from core.utils.constants import FIXED, PERCENTANGE

class FilterRoomRateManager(object):

    def __init__(self) -> None:
        pass
    
    def filter_rooms(Self, start_date, end_date, room_id):
        """Filtering rooms."""
        overridden_room_rate_objs = OverriddenRoomRate.objects.filter(room_rate__room_id=room_id, stay_date__range=(start_date, end_date))
        rates_list = []
        for overridden_obj in overridden_room_rate_objs:
            data_dic = {
                'room_id': room_id,
                'room_name': overridden_obj.room_rate.room_name,
                'stay_date': overridden_obj.stay_date,
            }
            if not overridden_obj.overridden_room_rate:
                data_dic['room_rate'] = overridden_obj.room_rate.default_rate   # here we are assigning the default rate.
            else:
                data_dic['room_rate'] = overridden_obj.overridden_room_rate
            
            fixed_discounts = DiscountRoomRate.objects.filter(room_rate__room_id=room_id,
                                                            room_rate__over_ridden_rate__stay_date=overridden_obj.stay_date,
                                                            discount__discount_type=FIXED)
            percentage_discounts = DiscountRoomRate.objects.filter(room_rate__room_id=room_id,
                                                                    room_rate__over_ridden_rate__stay_date=overridden_obj.stay_date,
                                                                    discount__discount_type=PERCENTANGE)
            
            
            print(fixed_discounts, "========================================================")

            max_fixed_discount = fixed_discounts.order_by('-discount__discount_value').first().discount.discount_value if fixed_discounts else 0
            max_percentage_discount = percentage_discounts.annotate(calculated_discount=F('discount__discount_value') * data_dic['room_rate'] / 100).order_by('-calculated_discount').first().calculated_discount
            
            print(max_fixed_discount, max_percentage_discount)

            max_discount = max(max_fixed_discount, round(max_percentage_discount,2))

            data_dic['final_rate'] = data_dic['room_rate'] - max_discount
            data_dic['discounted_value'] = max_discount
   
            
            rates_list.append(data_dic)

        return rates_list
 

    
    def filter_room_rate_based_on_date(self, start_date, end_date, room_id):
        """Filtering the room rate based on the date range."""
        room_rates = []
        discount_room_rates = DiscountRoomRate.objects.filter(
            room_rate__room_id=room_id,
            room_rate__over_ridden_rate__stay_date__range=(start_date, end_date)
        )

        for discount_room_rate in discount_room_rates:
            room_rate = discount_room_rate.room_rate
            discount_obj = discount_room_rate
            final_rate, overridden_rates_lowest_value = self.calculate_final_rate(room_rate, discount_obj)
            room_rates.append({
                'room_id': room_rate.room_id,
                'room_name': room_rate.room_name,
                'room_rate': overridden_rates_lowest_value if overridden_rates_lowest_value else room_rate.default_rate,
                'final_rate': final_rate,
            })
        
        return room_rates
    
    def calculate_final_rate(self, room_rate, discount_obj):
        """Final room rate calculation logic"""
        overridden_rates = room_rate.over_ridden_rate
        overridden_rates_lowest_value_obj = overridden_rates.order_by('overridden_room_rate').values().first()
        overridden_rates_lowest_value = overridden_rates_lowest_value_obj.get('overridden_room_rate')
        discount_type =  discount_obj.discount_type
        discount_value = discount_obj.discount_value
        default_rate = room_rate.default_rate
        if discount_type == FIXED:   
            final_rate = self.fixed_discount_type_rate(discount_value, overridden_rates_lowest_value, default_rate) 
        else:
            final_rate = self.percentange_discount_type_rate(discount_value, overridden_rates_lowest_value, default_rate)

        return final_rate, overridden_rates_lowest_value
    
    def fixed_discount_type_rate(self, discount_value, overridden_rate=None, default_rate=None):
        if overridden_rate:
            final_rate = overridden_rate - discount_value
        else:
            final_rate = default_rate - discount_value
        
        return final_rate

    def percentange_discount_type_rate(self, discount_value, overridden_rate=None, default_rate=None):
        if overridden_rate:
            final_rate = overridden_rate - (overridden_rate * (discount_value/100))
        else:
            final_rate = default_rate - (default_rate * (discount_value/100))
        
        return final_rate