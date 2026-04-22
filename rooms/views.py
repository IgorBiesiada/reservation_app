import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from django.contrib import messages

from . forms import SportForm, OfficeForm, EventForm, BeautyForm, LivingForm
from . import models


class AddSportsResourceView(CreateView):
    model = models.SportResource
    form_class = SportForm
    template_name = "rooms/sport_form.html"
    context_object_name = "sport"


class EditSportResourceView(UpdateView):
    model = models.SportResource
    form_class = SportForm
    fields = "__all__"
    context_object_name = "sport"


class AddOfficeResourceView(CreateView):
    model  = models.OfficeResource
    form_class = OfficeForm
    template_name = "rooms/office_form.html"
    context_object_name = "office"


class EditOfficeResourceView(UpdateView):
    model = models.OfficeResource
    form_class = OfficeForm
    fields = "__all__"
    context_object_name = "office"


class AddEventResourceView(CreateView):
    model = models.EventResource
    form_class = EventForm
    template_name = "rooms/event_form.html"
    context_object_name = "event"


class EditEventResourceView(UpdateView):
    model = models.EventResource
    form_class = EventForm
    fields = "__all__"
    context_object_name = "event"


class EventDetailView(DetailView):
    model = models.EventResource
    context_object_name = 'event'
    queryset = models.EventResource.objects.all()
    template_name = "rooms/event_detail.html"

class AddBeautyResourceView(CreateView):
    model = models.BeautyResource
    form_class = BeautyForm
    template_name = "rooms/beauty_form.html"
    context_object_name = "beauty"


class EditBeautyResourceView(UpdateView):
    model = models.BeautyResource
    form_class = BeautyForm
    fields = "__all__"
    context_object_name = "beauty"


class AddLivingResourceView(CreateView):
    model = models.LivingResource
    form_class = LivingForm
    template_name = "rooms/living_form.html"
    context_object_name = "living"


class EditLivingResourceView(UpdateView):
    model = models.LivingResource
    form_class = LivingForm
    fields = "__all__"
    context_object_name = "living"


class DeleteResourceView(DeleteView):
    model = models.BaseResource
    success_url = reverse_lazy("rooms:resource_list") 
    template_name = 'rooms/accept_delete_form.html'


# View for listing all resources
class ResourceListView(ListView):
    model = models.BaseResource  
    template_name = 'rooms/resource_list.html'  
    context_object_name = 'resources'  

    def get_queryset(self):
        return models.BaseResource.objects.select_related(
            'sportresource', 
            'officeresource', 
            'eventresource', 
            'beautyresource', 
            'livingresource'
        ).all()
        


# # View for displaying detailed information about a room
# class DetailRoomView(View):
#     def get(self, request, room_id):
#         room = Room.objects.get(id=room_id)  # Retrieve the room by ID
#         # Get reservations for today and future dates, ordered by date
#         reservations = room.reservations.filter(date__gte=str(datetime.date.today())).order_by('date')
#         return render(request, 'rooms/detailed_view.html', context={'room': room, 'reservations': reservations})


# # Function to show today's reservations
# def today_reservation(request):
#     today = datetime.date.today()  # Get today's date
#     reservations = Reservation.objects.all()  # Retrieve all reservations

#     context = {'reservations': reservations, 'today': today}  # Prepare context for rendering

#     return render(request, 'rooms/rooms.html', context)  # Render the room list with today's reservations


# # View for searching available rooms
# class RoomSearchView(View):
#     def get(self, request):
#         rooms = Room.objects.all()  # Retrieve all rooms
#         selected_capacity = request.GET.get('room_capacity', None)  # Get selected capacity from query parameters
#         projector_available = request.GET.get('projector_available', None)  # Check if projector is available
#         available_rooms = []  # List to store available rooms

#         # Check if any filters are applied
#         if selected_capacity or projector_available is not None:
#             today = datetime.date.today()  # Get today's date
#             # Get the IDs of rooms that are occupied today
#             occupied_rooms = Reservation.objects.filter(date=today).values_list('room', flat=True)

#             # Iterate through all rooms to apply filters
#             for room in rooms:
#                 # Check capacity filter
#                 if selected_capacity and room.room_capacity < int(selected_capacity):
#                     continue

#                 # Check projector availability filter
#                 if projector_available == 'on' and not room.projector_available:
#                     continue

#                 # Check if the room is not occupied
#                 if room.id not in occupied_rooms:
#                     available_rooms.append(room)  # Add room to available rooms list

#         # Render the search results
#         return render(request, 'rooms/search.html', {
#             'rooms': rooms,
#             'available_rooms': available_rooms,
#             'projector_available': projector_available
#         })

