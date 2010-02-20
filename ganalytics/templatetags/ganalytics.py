import datetime
import sgmllib
import time

from django.conf import settings
from django.template import Library, Node
from django.template.loader import get_template


register = Library()


class GanalyticsNode(Node):

    def __init__(self, nodelist):
        self.nodelist = nodelist
        self.tmpl = 

    def render(self, context):
        context.push()
        if 'ganalytics_code' not in context:
            try:
                context['ganalytics_code'] = settings.GANALYTICS_CODE
            except AttributeError:
                raise AttributeError("A template used the 'ganalytics' template tag with no 'ganalytics_code' variable in context and no GANALYTICS_CODE setting set")

        insides = self.nodelist.render(context)
        context['insides'] = insides

        try:
            return get_template('ganalytics/ganalytics.html').render(context)
        finally:
            context.pop()


@register.tag
def ganalytics(parser, token):
    nodelist = parser.parse(('endganalytics',))
    parser.delete_first_token()
    return GanalyticsNode(nodelist)
