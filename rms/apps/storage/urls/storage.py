from django.urls import path

from ..views import GetStorageView


urlpatterns = [
    path(
        route='',
        view=GetStorageView,
        name='get_storage',
    ),
]


