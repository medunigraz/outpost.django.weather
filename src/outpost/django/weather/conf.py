from appconf import AppConf
from django.conf import settings


class WeatherAppConf(AppConf):
    API_KEY = ""
    API_TIMEOUT = 10

    class Meta:
        prefix = "weather"
