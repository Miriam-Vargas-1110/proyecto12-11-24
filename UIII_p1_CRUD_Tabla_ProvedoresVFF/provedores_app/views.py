from django.shortcuts import render,redirect
from .models import Provedores


def inicio_vista(request):
    losprovedores=Provedores.objects.all()

    return render(request,"gestionarprovedores.html",{"misprovedores":losprovedores})

def registrarprovedores(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    numero=request.POST["txtnumero"]
    direccion=request.POST["skzdireccion"]
    idproductos=request.POST["skzidproductos"]
    precio=request.POST["skzprecio"]
    marca=request.POST["skzmarca"]

    guardarprovedores=Provedores.objects.create(id=id,nombre=nombre,numero=numero,direccion=direccion,idproductos=idproductos,precio=precio,marca=marca)

    return redirect('/') 

def seleccionarprovedores(request,id):
    
    provedores=Provedores.objects.get(id=id)
    return render(request,"editardatos.html",{"misprovedores":provedores})

def editarprovedores(request,id):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    numero=request.POST["txtnumero"]
    direccion=request.POST["skzdireccion"]
    idproductos=request.POST["skzidproductos"]
    precio=request.POST["skzprecio"]
    marca=request.POST["skzmarca"]

    provedores=Provedores.objects.get(id=id)
    provedores.nombre=nombre
    provedores.numero=numero
    provedores.direccion=direccion
    provedores.idproductos=idproductos
    provedores.precio=precio
    provedores.marca=marca
    provedores.save()
    return redirect('/') 

def borrarprovedores(request,id):
    ProvedoresS=Provedores.objects.get(id=id)
    ProvedoresS.delete()
    return redirect('/')

# Create your views here.
