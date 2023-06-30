from django.urls import path

from the_weather.weather.views import index

urlpatterns = [
    path('', index, name='index'),
]
