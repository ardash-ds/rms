from django.urls import path

from ..views import (
    create_item, 
    delete_item,
    get_items, 
    get_item_info, 
    update_item,
)


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
    path(
        route='<int:item_id>/update/',
        view=update_item,
        name='update_item',
    ),
]
