from django.urls import path

from ..views import create_storage, get_storage_user


urlpatterns = [
    path(
        route='',
        view=get_storage_user,
        name='get_storage',
    ),
    path(
        route='add/',
        view=create_storage,
        name='create_storage',
    ),
]


