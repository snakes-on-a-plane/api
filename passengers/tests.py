from django.test import TestCase
from .models import CarryOn

class CarryOnTestCase(TestCase):
    def setUp(self):
        rake = CarryOn.objects.create(name="rake")
        

    def test_rake_name(self):
        rake = CarryOn.objects.get(name = "rake")
        self.assertEqual(rake.name, "rake")

    def test_default_attack(self):
        rake = CarryOn.objects.get(name = "rake")
        self.assertEqual(rake.attack, 100)
