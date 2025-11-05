from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from Auth.views import RegisterViewSet,NotFoundViewSet

router = DefaultRouter()
router.register("auth/register",RegisterViewSet,basename='register')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/",include(router.urls)),
    re_path(r"^.*$", NotFoundViewSet.as_view(), name="not_found"),
]
