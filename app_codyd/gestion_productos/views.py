from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'gestion_productos/home.html')

def compras(request):
    return render (request,'gestion_productos/compras.html')

def contactos(request):
    return render (request,'gestion_productos/contactos.html')

def facturacion(request):
    return render (request,'gestion_productos/facturacion.html')

def inventario(request):
    return render (request,'gestion_productos/inventario.html')

def ventas(request):
    return render (request,'gestion_productos/ventas.html')






