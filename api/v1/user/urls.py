from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    UserApi, 
    UserEditApi,
    LogoutApi
)

urlpatterns = [
    path('register/', UserApi.as_view()),
    path('details/<int:pk>/', UserEditApi.as_view()),
    path('logout/', LogoutApi.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]