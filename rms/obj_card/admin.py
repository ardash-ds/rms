from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Object, Picture, Category, Storage

from apps.categories.models import CategoriesModel 
from apps.items.models import ItemsModel 
from apps.storage.models import StorageModel 

class CategoryAdmin(DjangoMpttAdmin):
    ordering = ('name',)
    search_fields = ("name__icontains", )

class PictureInline(admin.StackedInline):
    model = Picture

class ObjectAdmin(admin.ModelAdmin):
    inlines = [PictureInline]

admin.site.register(Object, ObjectAdmin)
admin.site.register(Picture)
admin.site.register(Storage)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoriesModel)
admin.site.register(ItemsModel)
admin.site.register(StorageModel)
