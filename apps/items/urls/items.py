from django.urls import path

from ..views import get_items, get_item_info, create_item, delete_item


urlpatterns = [
    path(
        route='all/',
        view=get_items,
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
    path(
        route='<int:item_id>/delete/',
        view=delete_item,
        name='delete_item',
    ),
]
