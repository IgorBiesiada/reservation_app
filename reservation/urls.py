from django.urls import path
from reservation.views import ReservationView


app_name = 'reservation'

urlpatterns = [
    path('reservation/<int:pk>/', ReservationView.as_view(), name='reservation')
]