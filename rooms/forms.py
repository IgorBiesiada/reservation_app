from django import forms
from .models import SportResource, OfficeResource, EventResource, BeautyResource, LivingResource, BaseResource


base_fields = ['name', 'equipment', 'price_per_hour', 'address',
                  'city', 'description']


class SportForm(forms.ModelForm):
    class Meta:
        model = SportResource
        fields = base_fields + ['sport_type', 'surface', 'is_outside', 'capacity']

class OfficeForm(forms.ModelForm):
    class Meta:
        model = OfficeResource
        fields = base_fields + ['desks', 'meeting_rooms', 'has_wifi', 'has_parking']

class EventForm(forms.ModelForm):
    class Meta:
        model = EventResource
        fields = base_fields + ['event_type', 'event_mode', 'capacity', 'sound_system',
                                'tv_set', 'stage', 'catering', 'parking', 'wifi']

class BeautyForm(forms.ModelForm):
    class Meta:
        model = BeautyResource
        fields = base_fields + ['beauty_type', 'chairs', 'beds', 'has_mirror', 
                                'has_sink', 'has_shower', 'parking', 'wifi']

class LivingForm(forms.ModelForm):
    class Meta:
        model = LivingResource
        fields = base_fields + ['living_type', 'rooms_count', 'parking', 'wifi', 'capacity',
                                'full_equipment']