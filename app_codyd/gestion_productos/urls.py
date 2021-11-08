"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from gestion_productos import views

urlpatterns = [
    path('',views.home, name="home"),
    path('compras',views.compras, name="compras"),
    path('contactos',views.contactos, name="contactos"),
    path('facturacion',views.facturacion, name="facturacion"),
    path('inventario',views.inventario, name="inventario"),
    path('ventas',views.ventas, name="ventas"),
    path('nuevo_contacto',views.nuevo_contacto, name="nuevo_contacto"),
    path('editar_contacto/<int:id>', views.editar_contacto, name="editar_contacto"),  
    # path('editar_producto/<int:id>', views.editar_producto, name="editar_producto"),  
    path('actualizar_contacto/<int:id>', views.actualizar_contacto, name="actualizar_contacto"),  
    path('delete/<int:id>', views.eliminar_contacto, name="eliminar_contacto"),
      
    # path('gestion_productos/', include('gestion_productos.urls')),
    
]
