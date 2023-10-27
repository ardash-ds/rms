from django.contrib import admin
from apps.categories.models import CategoryModel
from apps.storage.models import StorageModel
from apps.items.models import ItemModel, ItemImageModel
from apps.users.models import UserModel


class ItemModelAdmin(admin.ModelAdmin):
    class Meta:
        model = ItemModel
        fields = ['id', 'name']
    
    



admin.site.register(CategoryModel)
admin.site.register(ItemModel, ItemModelAdmin)
admin.site.register(StorageModel)
admin.site.register(UserModel)
admin.site.register(ItemImageModel)
