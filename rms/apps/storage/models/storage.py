from django.db import models


class StorageModel(models.Model):

    name = models.CharField(max_length=100, blank=False, unique=True)
    user = models.ForeignKey(
        'users.UserModel', 
        related_name='storage_user', 
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Мосто хранения'
        verbose_name_plural = 'Места хранения'
        db_table = 'storage'

    def __str__(self):
        return self.name
