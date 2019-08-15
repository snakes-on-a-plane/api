from django.db import models

class CarryOn(models.Model):
    name = models.CharField(max_length=256)
    attack = models.IntegerField(default=100)
    
    def __str__(self):
        return f'{self.name} - {self.attack}'
        
class Passenger(models.Model):
    name = models.CharField(max_length=256)
    personal_item = models.ForeignKey(CarryOn, on_delete=models.SET_DEFAULT, default=None, related_name='personal_item')
    carry_on = models.ForeignKey(CarryOn, on_delete=models.SET_DEFAULT, default=None, related_name='carry_on')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name



