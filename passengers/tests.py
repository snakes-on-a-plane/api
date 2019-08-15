from django.test import TestCase
from .models import Passenger
from .models import CarryOn

class NevilleTestCase(TestCase):
    def setUp(self):
        rake = CarryOn.objects.create(name="rake")
        laptop = CarryOn.objects.create(name="laptop")
        Passenger.objects.create(name="Neville", carry_on=rake, personal_item=laptop)
        

    def test_neville_name(self):
        neville = Passenger.objects.get(name = "Neville")
        self.assertEqual(neville.name, "Neville")

    # def test_neville_quote(self):
    #     neville = Neville.objects.get(name = "Neville")
    #     self.assertEqual(neville.quote, "ouch")

    def test_neville_carry_on(self):
        neville = Passenger.objects.get(name = "Neville")
        self.assertEqual(neville.carry_on.name, "rake")

    def test_neville_personal_item(self):
        neville = Passenger.objects.get(name = "Neville")
        self.assertEqual(neville.personal_item.name, "laptop")
