from django.contrib import admin
from .models import Shoe, ShoeType, ShoeColor, Manufacturer

# Register your models here.
admin.site.register(Shoe)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)
admin.site.register(Manufacturer)