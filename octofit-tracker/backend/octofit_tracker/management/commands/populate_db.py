from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        users = [User(**user) for user in test_users]
        User.objects.bulk_create(users)

        # Populate teams
        teams = []
        for team_data in test_teams:
            team = Team(_id=team_data["_id"], name=team_data["name"])
            team.save()
            team.members.set(User.objects.all())  # Assign all users to the team
            teams.append(team)

        # Populate activities
        activities = [
            Activity(_id=activity["_id"], user=User.objects.first(), activity_type=activity["activity_type"], duration=activity["duration"])
            for activity in test_activities
        ]
        Activity.objects.bulk_create(activities)

        # Populate leaderboard
        leaderboard_entries = [
            Leaderboard(_id=entry["_id"], user=User.objects.first(), score=entry["score"])
            for entry in test_leaderboard
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Populate workouts
        workouts = [Workout(**workout) for workout in test_workouts]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))