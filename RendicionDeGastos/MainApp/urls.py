from django.urls import path
from .views import index, trabajador

urlpatterns = [
    path('', index, name='index'),
    path('trabajador/', trabajador, name='trabajador')
]