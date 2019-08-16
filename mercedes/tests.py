from django.test import TestCase
# from passengers.models import Passenger
from .models import Mercedes
from passengers.models import CarryOn

# Create your tests here.
class MercedesTestCase(TestCase):
    def setUp(self):
        dog = CarryOn.objects.create(name="dog")
        phone = CarryOn.objects.create(name="phone")
        mercedes = Mercedes.objects.create(name="mercedes", quote="quote", money="millions", personal_item=dog, carry_on=phone)

    def test_mercedes_name(self):
        mercedes = Mercedes.objects.get(name="mercedes")
        self.assertEqual(mercedes.name, "mercedes")

    def test_mercedes_quote(self):
        mercedes = Mercedes.objects.get(quote="quote")
        self.assertEqual(mercedes.quote, "quote")

    def test_mercedes_money(self):
        mercedes = Mercedes.objects.get(money="millions")
        self.assertEqual(mercedes.money, "millions")

    def test_mercedes_personal_item(self):
        mercedes = Mercedes.objects.get(name="mercedes")
        self.assertEqual(mercedes.personal_item.name, "dog")

    def test_mercedes_carry_on(self):
        mercedes = Mercedes.objects.get(name="mercedes")
        self.assertEqual(mercedes.carry_on.name, "phone")