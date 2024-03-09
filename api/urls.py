from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from api.openapi import schema_view
from api.views.currency import CurrencyViewSet

app_name = "api"
router = DefaultRouter()
# router.register("auth", AuthViewSet, basename="auth")
router.register("currencies", CurrencyViewSet, basename="currencies")

urlpatterns = router.urls
urlpatterns += [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
