from django.db import models
from users.models import User
from polymorphic.models import PolymorphicModel


class Modified(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Stworzony")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Zaktualizowany")

    class Meta:
        abstract = True


class BaseResource(Modified, PolymorphicModel):
    class Category(models.TextChoices):
        SPORT = 'SPORT', 'Obiekt sportowy'
        OFFICE = 'OFFICE', 'Przestrzeń biurowa'
        EVENT = 'EVENT', 'Miejsce eventowe'
        BEAUTY = 'BEAUTY', 'Gabinet urody'
        LIVING = 'LIVING', 'Przestrzeń mieszkalna'

    category = models.CharField(max_length=50, choices=Category.choices, verbose_name="Typ kategorii")
    name = models.CharField(max_length=100, verbose_name="Nazwa")
    equipment = models.TextField(blank=True, verbose_name="Wyposażenie")
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena za h')
    address = models.CharField(max_length=255, verbose_name="Adres")
    city = models.CharField(max_length=100, verbose_name="Miasto")
    description = models.TextField(max_length=2000, blank=True, verbose_name="Opis")
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Zasób bazowy"

    def __str__(self):
        return self.name


# --- MODELE SPECYFICZNE ---

class SportResource(BaseResource):
    class SportType(models.TextChoices):
        FOOTBALL = 'FOOTBALL', 'Piłka nożna'
        TENNIS = 'TENNIS', 'Tenis'
        VOLLEYBALL = 'VOLLEYBALL', 'Siatkówka'
        GOLF = 'GOLF', 'Golf'

    sport_type = models.CharField(max_length=50, choices=SportType.choices, verbose_name='Dyscyplina')
    surface = models.CharField(max_length=50, blank=True, verbose_name='Nawierzchnia')
    is_outside = models.BooleanField(default=False, verbose_name='Na zewnątrz')
    capacity = models.PositiveIntegerField(null=True, blank=True, verbose_name='Liczba graczy')


    def get_template(self, template_type=''):
        valid_types = ('form', 'detail')
        if template_type not in valid_types:
            raise ValueError("pass form or detail")

        return f'rooms/sport_{template_type}.html'


class OfficeResource(BaseResource):
    desks = models.PositiveIntegerField(verbose_name='Liczba biurek')
    meeting_rooms = models.PositiveIntegerField(default=0, verbose_name='Liczba sal konferencyjnych')
    has_wifi = models.BooleanField(default=True, verbose_name="WIFI")
    has_parking = models.BooleanField(default=False, verbose_name="Parking")


    def get_template(self, template_type=''):
        valid_types = ('form', 'detail')
        if template_type not in valid_types:
            raise ValueError("pass form or detail")

        return f'rooms/office_{template_type}.html'


class EventResource(BaseResource):
    class EventType(models.TextChoices):
        BUSINESS = 'BUSINESS', 'Event biznesowy'
        INTEGRATION = 'INTEGRATION', 'Event integracyjny'
        MARKETING = 'MARKETING', 'Event marketingowy'
        ENTERTAINMENT = 'ENTERTAINMENT', 'Event rozrywkowy'

    class EventMode(models.TextChoices):
        ONLINE = 'ONLINE', 'Online'
        HYBRID = 'HYBRID', 'Hybrydowy'
        ONSITE = 'ONSITE', 'Stacjonarny'

    event_type = models.CharField(max_length=50, choices=EventType.choices, verbose_name='Typ eventu')
    event_mode = models.CharField(max_length=50, choices=EventMode.choices, verbose_name='Tryb eventu')
    capacity = models.PositiveIntegerField(verbose_name='Liczba miejsc')
    sound_system = models.BooleanField(default=False, verbose_name='Nagłośnienie')
    tv_set = models.BooleanField(default=False, verbose_name='Telewizor/Ekran')
    stage = models.BooleanField(default=False, verbose_name='Scena')
    catering = models.BooleanField(default=False, verbose_name='Catering')
    parking = models.BooleanField(default=False, verbose_name='Parking')
    wifi = models.BooleanField(default=True, verbose_name='WIFI')


class BeautyResource(BaseResource):
    class BeautyType(models.TextChoices):
        HAIRDRESSER = 'HAIRDRESSER', 'Fryzjer'
        BARBER = 'BARBER', 'Barber'
        NAILS = 'NAILS', 'Paznokcie'
        COSMETOLOGY = 'COSMETOLOGY', 'Kosmetologia'
        MASSAGE = 'MASSAGE', 'Masaż'

    beauty_type = models.CharField(max_length=50, choices=BeautyType.choices, verbose_name='Typ salonu')
    chairs = models.PositiveIntegerField(null=True, blank=True, verbose_name='Liczba foteli')
    beds = models.PositiveIntegerField(null=True, blank=True, verbose_name='Liczba łóżek')
    has_mirror = models.BooleanField(default=True, verbose_name='Lustro')
    has_sink = models.BooleanField(default=False, verbose_name='Zlew')
    has_shower = models.BooleanField(default=False, verbose_name='Prysznic')
    parking = models.BooleanField(default=False, verbose_name='Parking')
    wifi = models.BooleanField(default=True, verbose_name='WIFI')


    def get_template(self, template_type=''):
        valid_types = ('form', 'detail')
        if template_type not in valid_types:
            raise ValueError("pass form or detail")

        return f'rooms/beauty_{template_type}.html'


class LivingResource(BaseResource):
    class LivingType(models.TextChoices):
        ROOM = 'ROOM', 'Pokój'
        APARTMENT = 'APARTMENT', 'Mieszkanie'
        SUMMER_HOUSE = 'SUMMER', 'Dom letniskowy'
        HOUSE = 'HOUSE', 'Dom jednorodzinny'

    living_type = models.CharField(max_length=50, choices=LivingType.choices, default=LivingType.ROOM, verbose_name="Typ obiektu")
    rooms_count = models.PositiveIntegerField(default=1, verbose_name='Liczba pokoi')
    parking = models.BooleanField(default=False, verbose_name='Parking')
    wifi = models.BooleanField(default=False, verbose_name='WIFI')
    capacity = models.PositiveIntegerField(verbose_name='Liczba osób')
    full_equipment = models.BooleanField(default=False, verbose_name='Pełne wyposażenie')


    def get_template(self, template_type=''):
        valid_types = ('form', 'detail')
        if template_type not in valid_types:
            raise ValueError("pass form or detail")

        return f'rooms/living_{template_type}.html'

class ResourceImage(models.Model):
    image = models.ImageField(upload_to="resource_images/")
    resource = models.ForeignKey(BaseResource, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"Zdjęcie dla {self.resource}"
