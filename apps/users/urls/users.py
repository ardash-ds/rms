from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ..views import sign_up


urlpatterns = [
    path('sign_in/', TokenObtainPairView.as_view(), name='sign_in'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sign_up/', sign_up, name='sign_up'),
    # path('sign_in/', SignInView, name='sign_in'),
]
