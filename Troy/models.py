from django.db import models
from passengers.models import Passenger

# Create your models here.
class Troy(Passenger):
    quote = models.CharField(max_length=1024)
    flight_simulator_skill = models.IntegerField(default=100)
    way_with_words = models.IntegerField(default=100)
    bodyguarding = models.IntegerField(default=100)

    def fly_the_plane(Plane):
        pass