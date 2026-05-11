from django import forms
from . models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_date', 'end_date', 'comment']
        widgets = {
            'start_date': forms.DateInput(format="%d/%m/%Y", attrs={'type': 'date', 'class': 'mini-date'}),
            'end_date': forms.DateInput(format="%d/%m/%Y", attrs={'type': 'date', 'class': 'mini-date'}) 
        }