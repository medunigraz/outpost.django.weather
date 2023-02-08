from . import api

v1 = [
    (r"weather/location", api.LocationViewSet, "weather-location"),
]
