from django.db import models


class CategoriesModel(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'categories'

    def __str__(self):
        return self.name
