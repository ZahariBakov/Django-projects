from django.contrib import admin

from the_weather.weather.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
