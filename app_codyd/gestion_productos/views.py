from django.shortcuts import render, redirect
# from app_codyd.gestion_productos.forms import ProductoForm
from gestion_productos.models import Contacto, Inventario
from gestion_productos.forms import ContactoForm

# Create your views here.
def home(request):
    return render (request,'gestion_productos/home.html')

def compras(request):
    return render (request,'gestion_productos/compras.html')

def contactos(request):
    contactos = Contacto.objects.all()
    return render (request,'gestion_productos/contactos.html',{'contactos':contactos})

def facturacion(request):
    return render (request,'gestion_productos/facturacion.html')

def inventario(request):
    productos = Inventario.objects.all()
    return render (request,'gestion_productos/inventario.html',{'productos':productos})

def ventas(request):
    return render (request,'gestion_productos/ventas.html')


def nuevo_contacto(request):
    if request.method == "POST":  
        form = ContactoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/contactos')  
            except:  
                pass 
    else:  
        form = ContactoForm()  
    return render(request,'gestion_productos/nuevo_contacto.html',{'form':form})  

def editar_contacto(request, id):
    contacto = Contacto.objects.get(id=id)
    return render(request,'gestion_productos/editar_contacto.html', {'contacto':contacto})

# def editar_producto(request, id):
#     producto = Inventario.objects.get(id=id)
#     return render(request,'gestion_productos/editar_producto.html', {'producto':producto})


def actualizar_contacto(request, id):  
    contacto = Contacto.objects.get(id=id)  
    form = ContactoForm(request.POST, instance = contacto)  
    if form.is_valid():  
        form.save()  
        return redirect("/contactos")  
    return render(request, 'gestion_productos/editar_contacto.html', {'contacto': contacto})  

def eliminar_contacto(request, id):  
    contacto = Contacto.objects.get(id=id)  
    contacto.delete()  
    return redirect("/contactos")  




