from rest_framework import serializers
from api.models import IncubatorDevice, IncubatorSetting

class IncubatorSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncubatorSetting
        fields = ['id', 'name', 'temperature', 'humidity', 'incubation_duration', 'user']
