from rest_framework import viewsets
from api.models import IncubatorDevice
from api.serializers import IncubatorDeviceSerializer


class IncubatorDeviceViewSet(viewsets.ModelViewSet):
    queryset = IncubatorDevice.objects.all()
    serializer_class = IncubatorDeviceSerializer

    def perform_create(self, serializer):
        # Ajuste conforme a lógica de negócio necessária
        serializer.save(user=self.request.user)