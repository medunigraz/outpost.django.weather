from rest_framework.serializers import ModelSerializer

from . import models


class LocationSerializer(ModelSerializer):
    class Meta:
        model = models.Location
