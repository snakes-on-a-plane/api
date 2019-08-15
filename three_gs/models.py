from django.db import models
from passengers.models import Passenger

# Create your models here.
class ThreeGs(Passenger):
    accessories = models.CharField(max_length=256)

    def sanitizer_spray(snake):
        snake.health -= 10
        print("Ew gross!")
