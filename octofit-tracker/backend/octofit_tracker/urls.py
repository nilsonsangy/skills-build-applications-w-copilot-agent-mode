from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit Tracker API!",
        "endpoints": {
            "users": "/users/",
            "teams": "/teams/",
            "activities": "/activities/",
            "leaderboard": "/leaderboard/",
            "workouts": "/workouts/",
        }
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
]