from django.shortcuts import render, HttpResponse, redirect# Create your views here.
from .models import Pais

def index(request):
    return render(request,'index.html')

def gestionPais(request):
    listadoPais=Pais.objects.all()
    return render(request,'gestionPais.html', {"Pais": listadoPais})

def gestionEditorial(request):
    return render(request,'gestionEditorial.html')

def eliminarPais(request, id):
    pais=Pais.objects.get(pk=id)
    pais.delete()
    return redirect('/')

def registrarPais(request):
    idpais=request.POST['txtIdPais']
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    poblacion=request.POST['txtPoblacion']
    estado=request.POST['txtEstado']
    
    pais=Pais.objects.create(idpais=idpais, codigo=codigo,nombre=nombre,poblacion=poblacion, estado=estado)
    return redirect('/')
    


