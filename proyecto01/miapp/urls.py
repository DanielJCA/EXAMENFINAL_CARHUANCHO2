from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name = "index"),
    path('gestionEditorial/', views.gestionEditorial, name = "gestionEditorial"),
    path('gestionPais/', views.gestionPais, name = "gestionPais"),
    path('eliminarPais/<int:id>', views.eliminarPais, name = "eliminarPais"),
    path('registrarPais/', views.registrarPais, name = "registrarPais"),
    path('eliminarEditorial/<int:id>', views.eliminarEditorial, name = "eliminarEditorial"),
    path('registrarEditorial/', views.registrarEditorial, name = "registrarEditorial"),
    path('gestionAlumno/', views.gestionAlumno, name = "gestionAlumno"),

    
]