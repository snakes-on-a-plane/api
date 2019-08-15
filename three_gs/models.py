from django.db import models
from passengers.models import Passenger

# Create your models here.
class ThreeGs(Passenger):
    accessories = models.CharField(max_length=256)

    def descAccessories(self):
        return f'I have: {self.accessories}'
