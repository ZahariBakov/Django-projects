from django.db import models


class City(models.Model):
    name = models.CharField(
        max_length=50,
    )

    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    current_population = models.FloatField(
        blank=True,
        null=True,
    )

    permanent_address_population = models.FloatField(
        blank=True,
        null=True,
    )

    geographic_location = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    tourist_attractions = models.TextField(
        blank=True,
        null=True,
        help_text="Enter tourist attractions separated by <br> tag for new lines.",
    )

    culinary_delights = models.TextField(
        blank=True,
        null=True,
    )

    events_and_festivals = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class Country(models.Model):
    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
