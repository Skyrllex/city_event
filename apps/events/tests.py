from django.test import TestCase
from django.contrib.auth.models import User
from location.models import Location
from events.models import Event
from datetime import datetime
from django.utils import timezone


class EventTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="testadmin",
            password="admin123"
        )


        self.location =Location.objects.create(
            name = "Центральная набережная",
            coordinateX = 56.009498,
            coordinateY = 92.852488,
        )
        self.events = Event.objects.create(
            name = "Фестиваль фонарей",
            description = "Отмечаем прзданик весны в китайском стиле запускаем фонари",
            start_date=timezone.make_aware(datetime(2025,3,3,17,0,0)),
            end_date=timezone.make_aware(datetime(2025,3,3,22,0,0)),
            id_location=self.location,
            pub_date=timezone.now(),
            top=23,
            status='publication',
            author=self.user
        )
    def test_events_create(self):
        self.assertEqual(Event.objects.count(),1)
        self.assertEqual(str(self.events.name), 'Фестиваль фонарей')
        self.assertEqual(str(self.events.author.username), 'testadmin')
        self.assertEqual(str(self.events.id_location.name), 'Центральная набережная')
        print('Мероприятие создалось успешно')
            
