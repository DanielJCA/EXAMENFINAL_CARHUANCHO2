from django.shortcuts import render, HttpResponse, redirect# Create your views here.


def index(request):
    return render(request,'index.html')

def gestionPais(request):
    return render(request,'gestionPais.html')

def gestionEditorial(request):
    return render(request,'gestionEditorial.html')

