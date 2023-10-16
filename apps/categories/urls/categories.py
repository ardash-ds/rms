from django.urls import path

from ..views import get_categories, get_categories_with_things


urlpatterns = [
    path(
        route='all/',
        view=get_categories,
        name='get_categories',
    ),
    path(
        route='with_things/',
        view=get_categories_with_things,
        name='get_categories_with_things',
    ),
]


