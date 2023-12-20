from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', app_view, name='app_view'),
    # path('auth/', obtain_auth_token),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]
