from django.db import models
from rooms.models import BaseResource
from django.core.exceptions import ValidationError

# Create your models here.

class Reservation(models.Model):
    start_date = models.DateField()  # Reservation start date as a date field
    end_date = models.DateField()   #Reservation end date
    room = models.ForeignKey(BaseResource, on_delete=models.CASCADE, related_name='reservations') 
    comment = models.TextField(null=True)  

    def clean(self):
        super().clean()

        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError("Data zakończenia nie możę być wcześniejsza niż data rozpoczęcia")
        
        if self.start_date and self.end_date:
            valid_date = Reservation.objects.filter(
                start_date__lt = self.end_date,
                end_date__gt = self.star_date,
                room = self.room
        )
            
            if self.pk:
                valid_date = valid_date().exlude(pk=self.pk)

            if valid_date.exists():
                raise ValidationError("Ten termin jest już zajęty")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)