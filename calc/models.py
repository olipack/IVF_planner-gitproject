from django.db import models

class Drugs(models.Model):

    name = models.CharField(max_length=30)
    drug_start = models.DateField(null=True, blank=True)
    drug_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Cycle(models.Model):

    order = models.SmallIntegerField(default=0)
    name = models.CharField(max_length=15)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    drug1 = models.ForeignKey(Drugs, related_name='drug1', on_delete=models.RESTRICT, null=True)
    drug2 = models.ForeignKey(Drugs, related_name='drug2', on_delete=models.RESTRICT, null=True)
    drug3 = models.ForeignKey(Drugs, related_name='drug3', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return self.name