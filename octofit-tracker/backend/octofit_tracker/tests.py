from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        self.assertEqual(user.username, "testuser")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Team Alpha")
        self.assertEqual(team.name, "Team Alpha")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        activity = Activity.objects.create(user=user, activity_type="Running", duration="00:30:00")
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Morning Run", description="A quick morning run")
        self.assertEqual(workout.name, "Morning Run")