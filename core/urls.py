# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, IncubatorSettingViewSet, IncubatorDeviceViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'incubatorsettings', IncubatorSettingViewSet)
router.register(r'incubatordevices', IncubatorDeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]