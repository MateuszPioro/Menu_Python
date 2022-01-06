 
from rest_framework import routers, urlpatterns
from django.urls import include,path
from .views import  ComponentsViewSet,MealsViewSet,DishViewSet

router=routers.DefaultRouter()
router.register(r'components',ComponentsViewSet)
router.register(r'meals',MealsViewSet)
router.register(r'dish',DishViewSet)

urlpatterns=[
    path('api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]