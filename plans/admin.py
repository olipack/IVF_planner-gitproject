from django.contrib import admin
from .models import ProcedureGroup, Procedure, PrescriptionGroup, Prescription, CycleTemplate

@admin.register(ProcedureGroup)
class Admin(admin.ModelAdmin):
    list_display = ('name','order')
    list_editable = ('order',)

@admin.register(Procedure)
class Admin(admin.ModelAdmin):
    list_display = ('description','drug_1','drug_2','drug_3','group','order')
    list_editable = ('order',)

@admin.register(PrescriptionGroup)
class Admin(admin.ModelAdmin):
    list_display = ('name','order')
    list_editable = ('order',)

@admin.register(Prescription)
class Admin(admin.ModelAdmin):
    list_display = ('title','group','drug1','drug2','drug3','drug4','order')
    list_editable = ('order',)

@admin.register(CycleTemplate)
class Admin(admin.ModelAdmin):
    list_display = ('name','duration','p1','p1_start','p1_end','p2','p2_start','p2_end','p3','p3_start','p3_end','p4','p4_start','p4_end','proc1','proc1_cycleday','proc2','proc2_cycleday','proc3','proc3_cycleday','proc4','proc4_cycleday')
    list_editable = ('duration',)
    fields = ('name','duration',('p1','p1_start','p1_end'),('p2','p2_start','p2_end'),('p3','p3_start','p3_end'),('p4','p4_start','p4_end'),('proc1','proc1_cycleday'),('proc2','proc2_cycleday'),('proc3','proc3_cycleday'),('proc4','proc4_cycleday'))