import json

from django.core.management.base import BaseCommand

from apps.categories.models import CategoryModel
from apps.items.models import ItemModel
from apps.storage.models import StorageModel
from apps.users.models import UserModel


class Command(BaseCommand):
    help = 'Populates the database with test data'
    
    def add_users(self):
        with open("population/fixtures/users.json") as f:
            fixtures = json.load(f)
            for data in fixtures:
                UserModel.objects.create_user(
                    email=data["fields"]["email"],
                    username=data["fields"]["username"],
                    password=data["fields"]["password"],
                )
                
    def add_categories(self):
        with open("population/fixtures/categories.json") as f:
            fixtures = json.load(f)
            for data in fixtures:
                CategoryModel.objects.create(name=data["fields"]["name"])

    def add_storage(self):
        with open("population/fixtures/storage.json") as f:
            fixtures = json.load(f)
            for data in fixtures:
                StorageModel.objects.create(
                    name=data["fields"]["name"],
                    user=UserModel.objects.get(id=data["fields"]["user"]),
                )
        
    def add_items(self):
        with open("population/fixtures/items.json") as f:
            fixtures = json.load(f)
            for data in fixtures:
                ItemModel.objects.create(
                    name=data["fields"]["name"],
                    description=data["fields"]["description"],
                    user=UserModel.objects.get(id=data["fields"]["user"]),
                    category=CategoryModel.objects.get(id=data["fields"]["category"]),
                    storage=StorageModel.objects.get(id=data["fields"]["storage"]),
                )
        
    def handle(self, *args, **options):
        self.add_users()
        self.add_categories()
        self.add_storage()
        self.add_items()
        