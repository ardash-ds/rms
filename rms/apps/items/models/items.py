from django.db import models


class ItemsModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    user = models.ForeignKey(
        'auth.User',  
        on_delete=models.PROTECT,
        related_name='item_user',
        verbose_name='Пользователь',
    )
    category = models.ForeignKey(
        'categories.CategoriesModel',
        on_delete=models.SET_NULL,
        related_name='item_category',
        verbose_name='Категория',
        blank=True, 
        null=True, 
    )
    storage = models.ForeignKey(
        'storage.StorageModel',
        on_delete=models.SET_NULL,
        related_name='item_storage',
        verbose_name='Место хранения',
        blank=True, 
        null=True, 
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'
        db_table = 'items'

    def __str__(self):
        return self.name

class ImageItemModel(models.Model):
    image = models.ImageField(upload_to='%Y/%m/%d/')
    item = models.ForeignKey(
        'items.ItemModel', 
        related_name='image_item_for_items', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )

    class Meta:
        db_table = 'item_images'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        