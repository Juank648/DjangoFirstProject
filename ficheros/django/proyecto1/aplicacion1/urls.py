from django.urls import path
from aplicacion1 import views

app_name = 'aplicacion1'

urlpatterns = [
    path('pagina4/', views.pagina4, name='pagina4'),
    path('pagina5/', views.pagina5, name='pagina5'),
    path('plantilla/', views.plantilla, name='plantilla'),

]

