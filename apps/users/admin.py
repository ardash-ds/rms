from django.contrib import admin
from apps.categories.models import CategoryModel
from apps.storage.models import StorageModel
from apps.items.models import ItemModel
from apps.users.models import UserModel


admin.site.register(CategoryModel)
admin.site.register(ItemModel)
admin.site.register(StorageModel)
admin.site.register(UserModel)
