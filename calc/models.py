from django.db import models
from multiselectfield import MultiSelectField


class DrugClass(models.Model):

    name = models.CharField(max_length=30)

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
    active_ingredient = models.ForeignKey(ActiveIngredient, related_name='active_ingredient', on_delete=models.RESTRICT, null=True)
    drug_class = models.ForeignKey(DrugClass, related_name='drug_class', on_delete=models.RESTRICT, null=True)
    countries = MultiSelectField(choices=country_choices, max_length=255)

    def __str__(self):
        return self.name

class PrescriptionGroup(models.Model):

    name = models.CharField(max_length=70)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Prescription(models.Model):
    title = models.CharField(max_length=100)
    group = models.ForeignKey(PrescriptionGroup, related_name='group', on_delete=models.RESTRICT, null=True)
    drug1 = models.ForeignKey(Drug, related_name='drug1', on_delete=models.RESTRICT, null=True, blank=True)
    dosage1 = models.CharField(max_length=50, blank=True)
    drug2 = models.ForeignKey(Drug, related_name='drug2', on_delete=models.RESTRICT, null=True, blank=True)
    dosage2 = models.CharField(max_length=50, blank=True)
    drug3 = models.ForeignKey(Drug, related_name='drug3', on_delete=models.RESTRICT, null=True, blank=True)
    dosage3 = models.CharField(max_length=50, blank=True)
    drug4 = models.ForeignKey(Drug, related_name='drug4', on_delete=models.RESTRICT, null=True, blank=True)
    dosage4 = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class CycleType(models.Model):

    name = models.CharField(max_length=30)
    order = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Cycle(models.Model):

    cycle_type = models.ForeignKey(CycleType, related_name='cycle_type', on_delete=models.RESTRICT, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    prescription1 = models.ForeignKey(Prescription, related_name='prescription1', on_delete=models.RESTRICT, null=True)
    prescription1_start = models.DateField(null=True, blank=True)
    prescription1_end = models.DateField(null=True, blank=True)
    prescription2 = models.ForeignKey(Prescription, related_name='prescription2', on_delete=models.RESTRICT, null=True)
    prescription2_start = models.DateField(null=True, blank=True)
    prescription2_end = models.DateField(null=True, blank=True)
    prescription3 = models.ForeignKey(Prescription, related_name='prescription3', on_delete=models.RESTRICT, null=True)
    prescription3_start = models.DateField(null=True, blank=True)
    prescription3_end = models.DateField(null=True, blank=True)
    prescription4 = models.ForeignKey(Prescription, related_name='prescription4', on_delete=models.RESTRICT, null=True)
    prescription4_start = models.DateField(null=True, blank=True)
    prescription4_end = models.DateField(null=True, blank=True)
    prescription5 = models.ForeignKey(Prescription, related_name='prescription5', on_delete=models.RESTRICT, null=True)
    prescription5_start = models.DateField(null=True, blank=True)
    prescription5_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.cycle_type