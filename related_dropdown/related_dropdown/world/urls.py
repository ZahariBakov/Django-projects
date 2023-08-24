from django.urls import path

from related_dropdown.world.views import index, get_details, city_details, get_city_pk

urlpatterns = [
    path('', index, name='index'),
    path('get-details', get_details, name='get details'),
    path('city/<int:pk>/', city_details, name='city details'),
    path('get-city-pk', get_city_pk, name='get city pk'),
]
