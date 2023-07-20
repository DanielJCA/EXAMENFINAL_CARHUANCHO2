from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name = "index"),
    path('gestionEditorial/', views.gestionEditorial, name = "gestionEditorial"),
    path('gestionPais/', views.gestionPais, name = "gestionPais"),
]