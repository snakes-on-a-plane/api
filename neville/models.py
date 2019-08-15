from django.db import models
from passengers.models import Passenger

# Create your models here.
class Neville(Passenger):
    quote = models.CharField(max_length=1024)

    def _str__(self):
        return self.name