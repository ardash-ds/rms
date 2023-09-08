from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ..views import refresh_token_cookies, sign_up, sign_in, sign_in_cookies


urlpatterns = [
    path('sign_in_base/', TokenObtainPairView.as_view(), name='sign_in_base'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_in_cookies/', sign_in_cookies, name='sign_in_cookies'),
    path('refresh_cookies/', refresh_token_cookies, name='refresh_token_cookies'),
]
