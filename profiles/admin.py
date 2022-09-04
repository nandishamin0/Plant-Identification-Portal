from django.contrib import admin
from .models import plants
from .models import garden

# Register your models here.

admin.site.register(plants)
admin.site.register(garden)