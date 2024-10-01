from django.urls import path
from .views import hola_mundo
from .views import index

urlpatterns = [
    path('', index, name='index'),
]