from django.db import models

# Create your models here.
class Passenger(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class CarryOn(models.Model):
    name = models.CharField(max_length=256)
    attack = models.IntegerField(default=100)
    passenger = models.ForeignKey(Passenger, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return f'{self.name} - {self.attack}'
