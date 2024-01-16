from rest_framework.test import APITestCase
from django.test import TestCase
from .models import Team


class TeamViewTestCase(TestCase):

    def test_get_all_teams(self): 
        Team.objects.create(name="Team 1")
        Team.objects.create(name="Team 2")

        response = self.client.get('/api/teams/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_team(self):
        data = {'name': 'New Team'}

        response = self.client.post('/api/teams/', data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'New Team')


class TeamViewAPITests(APITestCase):

    def test_get_team(self):
        team = Team.objects.create(name="Test Team")

        url = f'/api/teams/{team.id}/'
        response = self.client.get(url)

        for team in response.data:
            self.assertEqual(team['name'], "Test Team")