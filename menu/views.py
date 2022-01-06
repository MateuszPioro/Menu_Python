from rest_framework.serializers import Serializer
from .models import Components,Meals,Dish
from rest_framework import viewsets
from .serializer import ComponentsSerializer,MealsSerializer,DishSerializer



class ComponentsViewSet(viewsets.ModelViewSet):
    queryset=Components.objects.all()
    serializer_class=ComponentsSerializer
    
class MealsViewSet(viewsets.ModelViewSet):
    queryset=Meals.objects.all()
    serializer_class=MealsSerializer
    
class DishViewSet(viewsets.ModelViewSet):
    queryset=Dish.objects.all()
    serializer_class=DishSerializer