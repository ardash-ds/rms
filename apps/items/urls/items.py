from django.urls import path

from ..views import get_items_user, get_item_info, create_item


urlpatterns = [
    path(
        route='all/',
        view=get_items_user,
        name='get_items',
    ),
    path(
        route='<int:item_id>/',
        view=get_item_info,
        name='get_item_info',
    ),
    path(
        route='add/',
        view=create_item,
        name='create_item',
    ),
]
