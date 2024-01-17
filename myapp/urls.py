from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views
from .views import UserRegistrationView, LoginAPIView, CustomUserScoreUpdate, CustomUserViewSet, UserScoreUpdateAPI

user_list = CustomUserViewSet.as_view({
    'get': 'list',
})


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/register/', UserRegistrationView.as_view(), name='api_user_register'),
    path('users/<int:pk>/score/', UserScoreUpdateAPI.as_view(), name='user-score-update'),
    path('users/', user_list, name='customuser-list'),
    ]
