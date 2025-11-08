from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from Auth.views import LoginViewSet, NotFoundViewSet, RegisterViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
router.register("auth/register",RegisterViewSet,basename='register')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/",include(router.urls)),
    path("api/auth/login", LoginViewSet.as_view(), name="login"),
    path("api/auth/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/token/verify", TokenVerifyView.as_view(), name="token_verify"),
    re_path(r"^.*$", NotFoundViewSet.as_view(), name="not_found"),
]
