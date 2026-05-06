from django.shortcuts import render
from . models import Reservation
from django.views.generic import CreateView
# Create your views here.

class ReservationView(CreateView):
    model = Reservation