from django.urls import re_path
from aplicacion1 import views

urlpatterns = [
     re_path('', views.vista2, name="vista2")
]