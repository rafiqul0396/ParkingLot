from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from accounts import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("createUser/",views.createUser,name="createUser"),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/user/all',views.getAllUsers,name="getAllUsers"),
]