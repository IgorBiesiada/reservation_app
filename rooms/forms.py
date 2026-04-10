from django import forms
from .models import SportResource, OfficeResource, EventResource, BeautyResource, LivingResource


class SportForm(forms.ModelForm):
    class Meta:
        model = SportResource
        fields = "__all__"

class OfficeForm(forms.ModelForm):
    class Meta:
        model = OfficeResource
        fields = "__all__"

class EventForm(forms.ModelForm):
    class Meta:
        model = EventResource
        fields = "__all__"

class BeautyForm(forms.ModelForm):
    class Meta:
        model = BeautyResource
        fields = "__all__"

class LivingForm(forms.ModelForm):
    class Meta:
        model = LivingResource
        fields = "__all__"