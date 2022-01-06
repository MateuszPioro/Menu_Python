from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Components(models.Model):
    name_com=CharField(max_length=30)
     
    
    def __str__(self):
        return self.name_com
     
    
class Meals(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    components=models.ManyToManyField(Components)
    
    def __str__(self):
        return f'{self.name}'
    
 
class Dish(models.Model):
    meals=models.ForeignKey(Meals,on_delete=models.CASCADE)
   
    def __str__(self):
        return ' '
  
   