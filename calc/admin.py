from django.contrib import admin
from .models import DrugClass, ActiveIngredient, Drug, PrescriptionGroup, Prescription, CycleType, Cycle

@admin.register(DrugClass)
class Admin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ActiveIngredient)
class Admin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Drug)
class Admin(admin.ModelAdmin):
    list_display = ('name','active_ingredient','drug_class','countries')
    list_filter = ('drug_class',)

@admin.register(PrescriptionGroup)
class Admin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Prescription)
class Admin(admin.ModelAdmin):
    list_display = ('title','group','drug1','drug2','drug3','drug4')

@admin.register(CycleType)
class Admin(admin.ModelAdmin):
    list_display = ('name','order')
    
@admin.register(Cycle)
class Admin(admin.ModelAdmin):
    list_display = ('id','cycle_type','start_date','end_date','prescription1','prescription2','prescription3')