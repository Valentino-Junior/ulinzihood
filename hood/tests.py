from django.test import TestCase

from hood.views import facilities
from .models import *
from django.contrib.auth.models import User

class TestNeighbourhoodModel(TestCase):
  '''
  test class for  the neighbour model
  '''
  def setUp(self):
    '''
    the startup class of the class
    '''
    self.new_user = User(username = 'Jim')
    self.new_user.save()
    self.new_neighbourhood = Hood(name = 'shiru',location = 'makadara',image='hood.jpg', datecreated = '2019-10-30', facilities='4565',user = self.new_user)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_neighbourhood,Hood))

  def test_create_neighbourhood(self):
    self.new_neighbourhood.save_neighborhood()
    neighborhoods = Hood.objects.all()
    self.assertTrue(len(neighborhoods) > 0)


class TestBusinessModels(TestCase):
  '''
  test classs that test the business model and its functions
  '''
  def setUp(self):
    '''
    the functions that runs at the begin of the test
    '''
    self.new_user = User(username = 'Kim')
    self.new_user.save()
    self.new_neighbourhood = Hood(name = 'Kwon',location = 'Esto',image='hood.jpg', datecreated = '2019-10-30', facilities='4565',user = self.new_user)



    self.new_neighborhood.save()
    self.new_business = Business(name = 'mama mboga',email= 'kim33@gmail.com', user=self.new_user, neighborhood=self.new_neighborhood )

  def test_business_instance(self):
    self.assertTrue(isinstance(self.new_business,Business))

  def test_create_a_business(self):
    self.new_business.save_business()
    business = Business.objects.all()
    self.assertTrue(len(business) > 0)



  def test_search_neighbourhood_by_name(self):
    self.new_user = User(username = 'Insta')
    self.new_user.save()
    self.new_neighbourhood = Hood(name = 'shiru',location = 'makadara',image='hood.jpg', datecreated = '2019-10-30', facilities='4565',user = self.new_user)

    self.new_business.save_business()
    search_result = Business.search_by_name('mama mboga')
    self.assertEqual(len(search_result),1)










    

    
