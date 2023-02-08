from django_filters.rest_framework import DjangoFilterBackend
from outpost.django.base.decorators import docstring_format
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import (
    filters,
    models,
    serializers,
)


@docstring_format(model=models.Location.__doc__)
class LocationViewSet(ReadOnlyModelViewSet):
    """
    List locations with weather forecasts

    {model}
    """

    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = filters.LocationFilter
