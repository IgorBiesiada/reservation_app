from django.db import models
from rooms.models import BaseResource
from django.core.exceptions import ValidationError
from users.models import User
 
# Create your models here.

class Reservation(models.Model):
    start_date = models.DateField()  # Reservation start date as a date field
    end_date = models.DateField()   #Reservation end date
    room = models.ForeignKey(BaseResource, on_delete=models.CASCADE, related_name='room') 
    comment = models.TextField(null=True)  
    booker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booker')
    is_active = models.BooleanField(default=True)
    
    def clean(self):
        super().clean()

        if not hasattr(self, 'room') or not self.start_date or not self.end_date:
            return
        
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError("Data zakończenia nie możę być wcześniejsza niż data rozpoczęcia")
        
        if self.start_date and self.end_date:
            valid_date = Reservation.objects.filter(
                start_date__lt = self.end_date,
                end_date__gt = self.start_date,
                room = self.room
        )
            
            if self.pk:
                valid_date = valid_date().exlude(pk=self.pk)

            if valid_date.exists():
                raise ValidationError("Ten termin jest już zajęty")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)