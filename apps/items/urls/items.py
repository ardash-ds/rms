from django.urls import path

from ..views import get_items_user


urlpatterns = [
    path(
        route='',
        view=get_items_user,
        name='get_items',
    ),
]


