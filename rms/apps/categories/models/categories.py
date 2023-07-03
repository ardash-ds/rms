from django.db import models


class CategoriesModel(models.Model):

    name = models.CharField(max_length=100, blank=False, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
