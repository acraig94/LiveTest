from django.contrib import admin

from .models import Location, Plant, Collection, PlantCollection, Track, TrackPoint

admin.site.register(Plant)
admin.site.register(Collection)
admin.site.register(PlantCollection)
admin.site.register(Track)
