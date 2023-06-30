from django import forms
from django.forms import TextInput

from the_weather.weather.models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'input',
                'placeholder': 'City Name'
            }),
        }
