import logging
from datetime import timedelta

from celery import shared_task

from .models import Location

logger = logging.getLogger(__name__)


class WeatherTask:
    @shared_task(bind=True, ignore_result=True, name=f"{__name__}.Weather:synchronize")
    def synchronize(task):
        for wl in Location.objects.all():
            wl.save()
