from django.contrib.auth.models import User
from rest_framework import viewsets
from api.models import IncubatorSetting
from api.serializers import IncubatorSettingSerializer


class IncubatorSettingViewSet(viewsets.ModelViewSet):
    queryset = IncubatorSetting.objects.all()
    serializer_class = IncubatorSettingSerializer
