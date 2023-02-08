import logging

import requests
from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from outpost.django.base.decorators import signal_connect

from .conf import settings

logger = logging.getLogger(__name__)


@signal_connect
class Location(models.Model):
    """"""

    country = CountryField()
    zip_code = models.CharField(max_length=32)
    forecast = JSONField(editable=False, null=True)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return f"{self.zip_code}, {self.country.code}"

    def pre_save(self, *args, **kwargs):
        try:

            with requests.get(
                f"https://api.openweathermap.org/data/2.5/forecast?zip={self.zip_code},{self.country.code}&units=metric&lang=de&appid={settings.WEATHER_API_KEY}",
                timeout=settings.WEATHER_API_TIMEOUT,
            ) as r:

                r.raise_for_status()

                response = r.json()
                self.forecast = response

        except requests.RequestException as e:
            logger.error(f"Could not fetch weather data: {e}")
