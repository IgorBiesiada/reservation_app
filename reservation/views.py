from django.shortcuts import render
from . models import Reservation
from django.views.generic import CreateView
from reservation.forms import ReservationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from . models import BaseResource
from django.urls import reverse_lazy
# Create your views here.

class ReservationView(LoginRequiredMixin ,CreateView):
    model = Reservation
    form_class = ReservationForm
    context_object_name = 'reservation'
    template_name = 'reservation/reservation.html'
    success_url = reverse_lazy('rooms:resource_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resource'] = get_object_or_404(BaseResource, pk=self.kwargs.get('pk'))

        return context
    
    
    def form_valid(self, form):
        res_id = self.kwargs.get('pk')

        resource_obj = get_object_or_404(BaseResource, pk=res_id)

        form.instance.room = resource_obj
        form.instance.booker = self.request.user

        return super().form_valid(form)