from django.contrib import admin
from .models import DrugClass, ActiveIngredient, Drug

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