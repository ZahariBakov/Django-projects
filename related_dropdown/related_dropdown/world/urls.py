from django.urls import path

from related_dropdown.world.views import index, get_details

urlpatterns = [
    path('', index, name='index'),
    path('get-details', get_details, name='get details'),
]
