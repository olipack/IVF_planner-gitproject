from django.db import models
from multiselectfield import MultiSelectField

class DrugClass(models.Model):

    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Drug classes"

    def __str__(self):
        return self.name

class ActiveIngredient(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Drug(models.Model):

    country_choices = (
        ('GBR', 'United Kingdom'),
        ('ITA', 'Italy'),
        ('NLD', 'Netherlands'),
        ('USA', 'United States'),
        ('ESP', 'Spain'),
        ('CAN', 'Canada'),
        ('GER', 'GER'),
        ('AUS', 'Australia'),
    )

    name = models.CharField(max_length=100)
    active_ingredient = models.ForeignKey(ActiveIngredient, related_name='active_ingredient', on_delete=models.CASCADE, null=True)
    drug_class = models.ForeignKey(DrugClass, related_name='drug_class', on_delete=models.CASCADE, null=True)
    countries = MultiSelectField(choices=country_choices, max_length=255)

    def __str__(self):
        return self.name