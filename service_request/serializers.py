from rest_framework import serializers
from .models import ServiceRequest
class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
       model = ServiceRequest
       fields = '__all__' 
   
    def validate(self, data):
        if data.get('service_type') == 'delivery':
            if not data.get('pickup_location'):
               raise serializers.ValidationError({
                   'pickup_location': 'This field is required for a delivery'
               })
            if not data.get('dropoff_location'):
               raise serializers.ValidationError({
                   'dropoff_location': 'This field is required for a delivery'
               })
        if data.get('service_type') == 'shopping':
            if not data.get('delivery_location'):
               raise serializers.ValidationError({
                   'delivery_location': 'This field is required for shopping'
               })
        if data.get('service_type') == 'errands':
            if not data.get('errand_destination'):
               raise serializers.ValidationError({
                   'errand_destination': 'This field is required for errands'
               })
        return data
    
       
           
           
               


    