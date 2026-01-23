from django.test import TestCase
from django.contrib.auth.models import User
from location.models import Location
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class LocationTestCaseWithApi(APITestCase):
    print('API Location Test 2 : Create object ')
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testadmin2",
            password="admin1234"
        )
        self.client=APIClient()
        self.client.force_authenticate(user=self.user)
    
    def test_locaiotn_create_api(self):
        data = {
            'name': 'Центральный парк',
            'coordinateX' : '56.009498', 
            'coordinateY' : '92.852488'
        }

        response = self.client.post('/api/location/', data, format='json')
        self.assertEqual (response.status_code, status.HTTP_201_CREATED)
        print('COMPLITED! API Location TEST 2: Create object.')
