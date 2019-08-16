# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from passengers.models import Passenger


# Create your models here.
class ClaireMiller(Passenger):

    #Should default to Claire Miller
    name = models.CharField(
        max_length=256, 
        default='Claire Miller',
    )

    #Job could link to a Jobs table, should give the person some 'skills'
    job = models.CharField(
        max_length=20, 
        default='Flight Attendant',
    )

    #Default the image to the image created in the src filie    
    imageUrl = models.CharField(
        max_length=255, 
        default='/ClaireMiller/src/clare_profile.jpg',
    )

    #Details about the character
    flavorText = models.CharField(
        max_length=255, 
        default='Claire Miller is a determined, resourceful woman with the strength to survive any catastrophe' 
    )

    def __str__(self):
        return self.name


