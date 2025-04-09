from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Test MongoDB connection and list collections in the database'

    def handle(self, *args, **kwargs):
        try:
            # Connect to MongoDB
            client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
            db = client[settings.DATABASES['default']['NAME']]

            # List collections
            collections = db.list_collection_names()
            self.stdout.write(self.style.SUCCESS(f"Connected to MongoDB. Collections: {collections}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to connect to MongoDB: {e}"))