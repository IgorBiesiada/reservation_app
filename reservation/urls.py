from django.urls import path
from reservation.views import reservation_view


app_name = 'reservation'

urlpatterns = [
    path('reservation/', reservation_view, name='reservation')
]