from django.test import TestCase
from django.contrib.auth.models import User
from location.models import Location

class LocationTestCase(TestCase):
    print('Test 1: Create object Location.')
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testadmin",
            password="admin123"
        )

        self.location =Location.objects.create(
            name = "Красная площадь",
            coordinateX = 56.008733, 
            coordinateY = 92.83873,
        )

    def test_location_create(self):
        self.assertEqual(Location.objects.count(), 1)
        self.assertEqual(str(self.location.name), 'Красная площадь')
        self.assertEqual(str(self.location.coordinateX), '56.008733')
        self.assertEqual(str(self.location.coordinateY), '92.83873')
        print('COMPLITED! TEST 1: Create object Location.')
            

