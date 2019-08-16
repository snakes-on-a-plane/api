# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import ClaireMiller
from passengers.models import CarryOn

# Create your tests here.
class ClaireMillerTestCase(TestCase):
    def setUp(self):
        potato = CarryOn.objects.create(name="potato")
        neckPillow = CarryOn.objects.create(name="neckPillow")
        clare = ClaireMiller.objects.create(
            personal_item = neckPillow,
            carry_on = potato
        )

    def test_clare_name(self):
        clare = ClaireMiller.objects.get(name='Claire Miller')
        self.assertEqual(clare.name, 'Claire Miller')

    def test_clare_job(self):
        clare = ClaireMiller.objects.get(name='Claire Miller')
        self.assertEqual(clare.job, 'Flight Attendant')

    def test_clare_flavorText(self):
        clare = ClaireMiller.objects.get(name='Claire Miller')
        self.assertEqual(clare.flavorText, 'Claire Miller is a determined, resourceful woman with the strength to survive any catastrophe')

    def test_clare_image_url(self):
        clare = ClaireMiller.objects.get(name='Claire Miller')
        self.assertEqual(clare.imageUrl, '/ClaireMiller/src/clare_profile.jpg')