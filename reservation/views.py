from django.shortcuts import render
from . models import Reservation
from django.views.generic import CreateView
from reservation.forms import ReservationForm
# Create your views here.

class ReservationView(CreateView):
    model = Reservation
    form_class = ReservationForm
    context_object_name = 'reservation'
    template_name = 'reservation/reservation.html'