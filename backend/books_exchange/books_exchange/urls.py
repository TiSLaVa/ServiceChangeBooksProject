from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from mainapp.views import ActivateUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('mainapp.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/users/activation/<uid>/<token>/', ActivateUser.as_view()),
    path('auth/token/', TokenObtainPairView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),

]
