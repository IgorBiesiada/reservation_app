from django.core.management.base import BaseCommand
from reservation.models import Reservation
from django.utils import timezone


class Command(BaseCommand):
    help = "command to close all completed reservations"


    def handle(self, *args, **options):
        expired_reservations = Reservation.objects.filter(end_date__lt=timezone.now(), is_active=True)
        expired_reservations.update(is_active=False)

        self.stdout.write(
            self.style.SUCCESS("completed reservations closed")
        )
    