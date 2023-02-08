from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WeatherConfig(AppConfig):
    name = "outpost.django.weather"
    verbose_name = _("Weather")
