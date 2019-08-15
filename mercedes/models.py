from django.db import models
from passengers.models import Passenger

# Create your models here.
class Mercedes(Passenger):
    quote = models.CharField(max_length=1024)
    money = models.CharField(max_length=10, default=None)
    def __str__(self):
        return self.name