from django.test import TestCase
from .models import Troy
from passengers.models import CarryOn
# Create your tests here.

class TroyTestCase(TestCase): 

  def setUp(self):
    troy = Troy.objects.create(quote="Look at the Howard Hughes of rap.",
                               flight_simulator_skill=1000,
                               way_with_words=1000,
                               bodyguarding=1000,
                               personal_item=CarryOn.objects.create(name='Ps3',
                                                                    attack=9000),
                               carry_on=CarryOn.objects.create(name='Ps2',
                                                               attack=9000),
                                                               name="Troy")
    troy.save()                                                           

  def test_flight_simulator_skill(self):
    
    test_troy_fly = Troy.objects.get(name = "Troy")

    self.assertEqual(test_troy_fly.flight_simulator_skill, 1000)

  def test_way_with_words(self): 

    test_words = Troy.objects.get(name= "Troy") 

    self.assertEqual(test_words.way_with_words, 1000)  

  def test_bodyguard(self): 

    test_bodyguard = Troy.objects.get(name="Troy")

    self.assertEqual(test_bodyguard.bodyguarding, 1000) 

  def test_quote(self): 

    test_quote = Troy.objects.get(name="Troy") 

    self.assertEqual(test_quote.quote, "Look at the Howard Hughes of rap.")    


    
  
