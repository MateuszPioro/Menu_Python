from django.db.models import fields
from django.db.models.base import Model
from .models import Components,Meals,Dish
from rest_framework import serializers

class ComponentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Components
        fields =['id','name_com']
        
class MealsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Meals
        fields=['id','name','price']
        
class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Dish
        fields=['id','meals']