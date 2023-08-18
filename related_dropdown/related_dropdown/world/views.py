from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from related_dropdown.world.models import Country, City


def index(request):
    countries = Country.objects.all()
    return render(request, 'index.html', {'countries': countries})


def get_details(request):
    country_name = request.GET.get('cnt')

    if country_name:
        selected_country = Country.objects.filter(name=country_name).first()
        if selected_country:
            cities = selected_country.city_set.all()
            city_names = [city.name for city in cities]
            return JsonResponse({'cities': city_names})

    return JsonResponse({'cities': []})


def city_details(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'city_details.html', {'city': city})


def get_city_pk(request):
    city_name = request.GET.get('city')
    city = City.objects.filter(name=city_name).first()
    if city:
        return JsonResponse({'pk': city.pk})
    else:
        return JsonResponse({'pk': None})
