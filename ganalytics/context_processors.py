import logging

from django.conf import settings


log = logging.getLogger(__name__)


def ganalytics(request):
    try:
        code = settings.GANALYTICS_CODE
    except AttributeError:
        log.warning('The ganalytics context processor is enabled, but the GANALYTICS_CODE setting is not set')
        return {}
    else:
        return {
            'ganalytics_code': code,
        }
