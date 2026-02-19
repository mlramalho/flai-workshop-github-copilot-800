from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            password="password123"
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsNotNone(self.user._id)
    
    def test_user_str(self):
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            description="A test team",
            captain_id="123456",
            members=["123456", "789012"]
        )
    
    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(len(self.team.members), 2)
        self.assertIsNotNone(self.team._id)
    
    def test_team_str(self):
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id="123456",
            activity_type="Running",
            duration=30,
            distance=5.0,
            calories=300,
            date=datetime.now()
        )
    
    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)
        self.assertIsNotNone(self.activity._id)


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'name': 'API Test User',
            'email': 'apitest@example.com',
            'password': 'testpass123'
        }
    
    def test_create_user(self):
        response = self.client.post(
            reverse('user-list'),
            self.user_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'API Test User')
    
    def test_get_users(self):
        User.objects.create(**self.user_data)
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            'name': 'API Test Team',
            'description': 'Test team description',
            'captain_id': '123456',
            'members': ['123456']
        }
    
    def test_create_team(self):
        response = self.client.post(
            reverse('team-list'),
            self.team_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
    
    def test_get_teams(self):
        Team.objects.create(**self.team_data)
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.activity_data = {
            'user_id': '123456',
            'activity_type': 'Running',
            'duration': 30,
            'distance': 5.0,
            'calories': 300,
            'date': datetime.now().isoformat()
        }
    
    def test_create_activity(self):
        response = self.client.post(
            reverse('activity-list'),
            self.activity_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)
    
    def test_get_activities(self):
        Activity.objects.create(
            user_id=self.activity_data['user_id'],
            activity_type=self.activity_data['activity_type'],
            duration=self.activity_data['duration'],
            distance=self.activity_data['distance'],
            calories=self.activity_data['calories'],
            date=datetime.now()
        )
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        self.workout_data = {
            'name': 'Morning Run',
            'description': 'A refreshing morning run',
            'activity_type': 'Running',
            'difficulty': 'Medium',
            'duration': 30,
            'calories_estimate': 300,
            'instructions': ['Warm up', 'Run 5km', 'Cool down']
        }
    
    def test_create_workout(self):
        response = self.client.post(
            reverse('workout-list'),
            self.workout_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 1)
    
    def test_get_workouts(self):
        Workout.objects.create(**self.workout_data)
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIRootTest(APITestCase):
    """Test cases for API root endpoint"""
    
    def setUp(self):
        self.client = APIClient()
    
    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
