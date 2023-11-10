from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ..views import (
    get_user_info,
    logout,
    sign_up, 
    sign_in, 
)
    

urlpatterns = [
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('info/', get_user_info, name='user_info'),
    path('logout/', logout, name='logout'),
]
