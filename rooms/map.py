from rooms.models import SportResource, OfficeResource, LivingResource, BeautyResource, EventResource
from rooms.forms import SportForm, OfficeForm, LivingForm, BeautyForm, EventForm

RESOURCE_CONFIG = {
    'sport': {
        'model': SportResource,
        'form': SportForm,
        'template': 'rooms/sport_form.html',
        'category': 'SPORT',
    },

    'office': {
        'model': OfficeResource,
        'form': OfficeForm,
        'template': 'rooms/office_form.html',
        'category': 'OFFICE',
    },

    'event': {
        'model': EventResource,
        'form': EventForm,
        'template': 'rooms/event_form.html',
        'category': 'EVENT',
    },

    'beauty': {
        'model': BeautyResource,
        'form': BeautyForm,
        'template': 'rooms/beauty_form.html',
        'category': 'BEAUTY',
    },

    'living': {
        'model': LivingResource,
        'form': LivingForm,
        'template': 'rooms/living_form.html',
        'category': 'LIVING',
    }
}