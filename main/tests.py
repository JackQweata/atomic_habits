from django.test import TestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from .models import Habit


class HabitCRUDTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="users@sky.pro",
            password="123",
            tg_id="321321"
        )

        self.lesson_data = {
            'title': 'Test Lesson 1',
            'descriptions': 'test',
            'link_video': 'youtube.com',
            'owner': self.user.pk
        }
        self.access_token = self.get_access_token()

    def get_access_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_create_habit(self):

        habit_data = {
            'user': 1,
            'place': 'Дома',
            'time': '08:00',
            'action': 'Работать',
            'is_enjoyable': True,
            'frequency': 1,
            'estimated_time': 60,
        }
        response = self.client.post(
            '/api/habit/create/',
            habit_data,
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        habit = Habit.objects.first()
        self.assertEqual(habit.place, 'Дома')

    def test_read_habit(self):

        habit = Habit.objects.create(
            user=self.user,
            place='Дома',
            time='17:00:00',
            action='Работать',
            is_enjoyable=False,
            frequency=7,
            estimated_time=45,
        )

        response = self.client.get(
            f'/api/habit/{habit.pk}/',
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'], 'Дома')

    def test_update_habit(self):

        habit = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='09:00:00',
            action='Работать',
            is_enjoyable=True,
            frequency=1,
            estimated_time=30,
        )

        updated_data = {
            'place': 'Офис',
            'time': '10:00:00',
        }
        response = self.client.put(
            f'/api/habit/update/{habit.pk}/',
            updated_data,
            content_type='application/json',
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit.refresh_from_db()
        self.assertEqual(habit.place, 'Офис')

    def test_delete_habit(self):

        habit = Habit.objects.create(
            user=self.user,
            place='Парк',
            time='07:00:00',
            action='Пробежка',
            is_enjoyable=True,
            frequency=1,
            estimated_time=45,
        )

        response = self.client.delete(
            f'/api/habit/delete/{habit.pk}/',
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
