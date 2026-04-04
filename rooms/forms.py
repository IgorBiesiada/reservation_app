from django import forms
from . models import SportResource, BeautyResource


base_fields = ['name', 'equipment', 'price_per_hour', 'address', 'city', 'description']


class SportFrom(forms.ModelForm):
    class Meta:
        model = SportResource

        fields = [
            'sport_type', 'surface', 'is_outside', 
            'capacity'
        ] + base_fields

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa obiektu'}),
            'sport_type': forms.Select(attrs={'class': 'form-select'}), 
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price_per_hour': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_outside': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }

        labels = {
            'sport_type': 'Wybierz dyscyplinę sportu',
            'is_outside': 'Czy obiekt jest na zewnątrz?'
        }

class OfficeForm(forms.ModelForm):
    class Meta:
        model = SportResource

        fields = [
             'desk', 'meeting_rooms', 'has_wifi', 'has_parking'] + base_fields
        
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'})
        }