from django.test import TestCase
from django.contrib.auth.models import User
from location.models import Location
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from datetime import datetime
from django.utils import timezone


class EventTestCaseWithApi(APITestCase):
    print('Events API Test 2 : Create object Events')
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testadmin",
            password="admin123"
        )
        self.client=APIClient()
        self.client.force_authenticate(user=self.user)
        
        self.location =Location.objects.create(
            name = "Центральная набережная",
            coordinateX = 56.009498,
            coordinateY = 92.852488,
        )

    def test_events_create_api(self):
       data = {
            'name' : "Фестиваль фонарей",
            'description' : "Отмечаем прзданик весны в китайском стиле запускаем фонари",
            'start_date': timezone.make_aware(datetime(2025,3,3,17,0,0)),
            'end_date': timezone.make_aware(datetime(2025,3,3,22,0,0)),
            'id_location_info': self.location.id,
            'pub_date': timezone.now(),
            'top': 23,
            'status':'publication',
            'author_info': self.user.id
        }
       response = self.client.post('/api/events/', data, format='json')
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       print('COMPLITED! API Events TEST 2: Create object.')



 
