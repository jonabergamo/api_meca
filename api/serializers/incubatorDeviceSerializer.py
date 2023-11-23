from rest_framework import serializers
from api.models import IncubatorDevice
from .incubatorSettingsSerializer import IncubatorSettingSerializer

class IncubatorDeviceSerializer(serializers.ModelSerializer):
    current_setting = IncubatorSettingSerializer(read_only=True)

    class Meta:
        model = IncubatorDevice
        fields = ['unique_id', 'user', 'current_setting', 'is_on', 'humidity_sensor', 'temperature_sensor', 'start_time']