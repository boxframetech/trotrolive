from django.contrib import admin
from .models import StationModel, Stops, Trip, FareRules, Routes, MissingItem
# Register your models here.


admin.site.register(StationModel)

admin.site.register(Stops)

admin.site.register(Trip)

admin.site.register(FareRules)

admin.site.register(Routes)

admin.site.register(MissingItem)