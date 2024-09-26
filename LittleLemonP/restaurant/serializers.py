from rest_framework import serializers
from .models import Menu, Booking
import bleach

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
    
    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
    
    def validate(self, attrs):
        attrs['name'] = bleach.clean(attrs['name'])