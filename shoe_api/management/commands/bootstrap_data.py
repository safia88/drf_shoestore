from django.core.management.base import BaseCommand
from shoe_api.models import ShoeColor, ShoeType


class Command(BaseCommand):
    help = 'populates ShoeColor and ShoeType tables with data.'

    def _shoe_type(self, *args, **options):
        ShoeType(style='sneaker').save()
        ShoeType(style='boot').save()
        ShoeType(style='sandal').save()
        ShoeType(style='dress').save()
        ShoeType(style='other').save()

    def _shoe_color(self, *args, **options):
        ShoeColor(color_name='Red').save()
        ShoeColor(color_name='Orange').save()
        ShoeColor(color_name='Yellow').save()
        ShoeColor(color_name='Green').save()
        ShoeColor(color_name='Blue').save()
        ShoeColor(color_name='Indigo').save()
        ShoeColor(color_name='Violet').save()
        ShoeColor(color_name='White').save()
        ShoeColor(color_name='Black').save()

    def handle(self, *args, **options):
        self._shoe_color()
        self._shoe_type()
