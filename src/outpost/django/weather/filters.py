import django_filters

from . import models


class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = models.Location
        fields = ["country", "zip_code"]
