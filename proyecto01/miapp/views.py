from django.shortcuts import render, HttpResponse, redirect# Create your views here.
from .models import Pais, Editorial

def index(request):
    return render(request,'index.html')

def gestionPais(request):
    listadoPais=Pais.objects.all()
    return render(request,'gestionPais.html', {"Pais": listadoPais})

def gestionEditorial(request):
    listadoEditorial=Editorial.objects.all()
    return render(request,'gestionEditorial.html', {"Editorial": listadoEditorial})

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
    
def eliminarEditorial(request, id):
    editorial=Editorial.objects.get(pk=id)
    editorial.delete()
    return redirect('/')

def registrarEditorial(request):
    ideditorial=request.POST['txtIdEditorial']
    nombre=request.POST['txtNombre']
    url=request.POST['txtUrl']
    imagen=request.POST['txtImagen']
    estado=request.POST['txtEstado']
    
    editorial=Editorial.objects.create(ideditorial=ideditorial,nombre=nombre,url=url, imagen=imagen, estado=estado)
    return redirect('/')

def gestionAlumno(request):
    return render(request,'gestionAlumno.html')


