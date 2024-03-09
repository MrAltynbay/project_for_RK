from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Project for RK API",
        default_version="v1",
        description="API description",
    ),
    public=True,
    permission_classes=[AllowAny],
    authentication_classes=[JWTAuthentication],
)
