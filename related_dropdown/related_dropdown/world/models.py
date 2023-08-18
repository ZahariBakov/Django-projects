from django.db import models


class City(models.Model):
    name = models.CharField(
        max_length=50,
    )

    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
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
