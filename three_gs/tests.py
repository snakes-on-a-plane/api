from django.test import TestCase
from passengers.models import CarryOn
from .models import ThreeGs

class Three3GsTestCase(TestCase):
    def setUp(self):
        rake = CarryOn.objects.create(name="rake")
        cell = CarryOn.objects.create(name="cell")
        three3 = ThreeGs.objects.create(
            name = 'OG',
            carry_on = rake,
            personal_item = cell,
            accessories = 'Gold Chain')

    def test_accessories(self):
        three3 = ThreeGs.objects.get(name = 'OG')
        self.assertEquals(three3.accessories, 'Gold Chain')

    def test_descAccessories(self):
        three3 = ThreeGs.objects.get(name = 'OG')
        self.assertEquals(three3.descAccessories(), 'I have: Gold Chain')
