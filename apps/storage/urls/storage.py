from django.urls import path

from ..views import (
    create_storage, 
    delete_storage,
    get_storage_all,
    get_storage_with_things,
)


urlpatterns = [
    path(
        route='add/',
        view=create_storage,
        name='create_storage',
    ),
    path(
        route='all/',
        view=get_storage_all,
        name='get_storage_all',
    ),
    path(
        route='with_things/',
        view=get_storage_with_things,
        name='get_storage_with_things',
    ),
    path(
        route='delete/<int:storage_id>/',
        view=delete_storage,
        name='delete_storage',
    ),
]
