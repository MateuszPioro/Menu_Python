from django.contrib import admin
from .models import Meals, Components, Dish

# Register your models here.
 

@admin.register(Meals)
class MealsAdmin(admin.ModelAdmin):
    search_fields=['name','price']
    list_display=['id','name','price']
    list_filter=['name' ]
    

@admin.register(Components)
class ComponentsAdmin(admin.ModelAdmin):
    list_display=['id','name_com']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display=['id','meals']
     


# admin.site.register(Meals)
# admin.site.register(Components)
# admin.site.register(Dish)