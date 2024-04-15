from django.urls import path
from Authentication.views import CreateUserView, CustomTokenObtainPairView, TokenRefreshView
from . import views
urlpatterns = [
    path('',views.index),
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]