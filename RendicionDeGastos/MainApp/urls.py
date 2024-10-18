from django.urls import path
from .views import index, trabajador, contador

urlpatterns = [
    path('', index, name='index'),
    path('trabajador/', trabajador, name='trabajador'),
    path('contador/', contador, name='contador')
]