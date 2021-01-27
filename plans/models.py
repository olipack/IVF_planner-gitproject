from django.db import models
from drugs.models import Drug

class ProcedureGroup(models.Model):

    name = models.CharField(max_length=70)
    order = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Procedure(models.Model):

    description = models.CharField(max_length=150)
    drug_1 = models.ForeignKey(Drug, related_name='drug_1', on_delete=models.PROTECT, null=True, blank=True)
    dosage_1 = models.CharField(max_length=150, blank=True, verbose_name="Dosage")
    drug_2 = models.ForeignKey(Drug, related_name='drug_2', on_delete=models.PROTECT, null=True, blank=True)
    dosage_2 = models.CharField(max_length=150, blank=True, verbose_name="Dosage")
    drug_3 = models.ForeignKey(Drug, related_name='drug_3', on_delete=models.PROTECT, null=True, blank=True)
    dosage_3 = models.CharField(max_length=150, blank=True, verbose_name="Dosage")
    group = models.ForeignKey(ProcedureGroup, related_name='group', on_delete=models.RESTRICT, null=True)
    order = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.description

class PrescriptionGroup(models.Model):

    name = models.CharField(max_length=70)
    order = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Prescription(models.Model):

    title = models.CharField(max_length=100)
    group = models.ForeignKey(PrescriptionGroup, related_name='group', on_delete=models.RESTRICT, null=True)
    drug1 = models.ForeignKey(Drug, related_name='drug1', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Drug 1")
    dosage1 = models.CharField(max_length=150, blank=True)
    drug2 = models.ForeignKey(Drug, related_name='drug2', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Drug 2")
    dosage2 = models.CharField(max_length=150, blank=True)
    drug3 = models.ForeignKey(Drug, related_name='drug3', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Drug 3")
    dosage3 = models.CharField(max_length=150, blank=True)
    drug4 = models.ForeignKey(Drug, related_name='drug4', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Drug 4")
    dosage4 = models.CharField(max_length=150, blank=True)
    order = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['group']

    def __str__(self):
        return self.title

class CycleTemplate(models.Model):

    name = models.CharField(max_length=30)
    duration = models.SmallIntegerField(default=21)
    p1 = models.ForeignKey(Prescription, related_name='p1', on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Prescription 1")
    p1_start = models.SmallIntegerField(default=1, verbose_name="Start day")
    p1_end = models.SmallIntegerField(default=21, verbose_name="End day")
    p2 = models.ForeignKey(Prescription, related_name='p2', on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Prescription 2")
    p2_start = models.SmallIntegerField(default=1, verbose_name="Start day")
    p2_end = models.SmallIntegerField(default=21, verbose_name="End day")
    p3 = models.ForeignKey(Prescription, related_name='p3', on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Prescription 3")
    p3_start = models.SmallIntegerField(default=1, verbose_name="Start day")
    p3_end = models.SmallIntegerField(default=21, verbose_name="End day")
    p4 = models.ForeignKey(Prescription, related_name='p4', on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Prescription 4")
    p4_start = models.SmallIntegerField(default=1, verbose_name="Start day")
    p4_end = models.SmallIntegerField(default=21, verbose_name="End day")
    proc1 = models.ForeignKey(Procedure, related_name='proc1', on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Procedure 1")
    proc1_cycleday = models.SmallIntegerField(default=0, verbose_name="Cycle day")
    proc2 = models.ForeignKey(Procedure, related_name='proc2', on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Procedure 2")
    proc2_cycleday = models.SmallIntegerField(default=0, verbose_name="Cycle day")
    proc3 = models.ForeignKey(Procedure, related_name='proc3', on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Procedure 3")
    proc3_cycleday = models.SmallIntegerField(default=0, verbose_name="Cycle day")
    proc4 = models.ForeignKey(Procedure, related_name='proc4', on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Procedure 4")
    proc4_cycleday = models.SmallIntegerField(default=0, verbose_name="Cycle day")

    def __str__(self):
        return self.name