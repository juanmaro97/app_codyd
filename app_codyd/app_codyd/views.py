from django.http import HttpResponse

def saludo(request): # primera vista

    return HttpResponse("Hola mundo")

def saludo2(request): # primera vista

    return HttpResponse("Hola mundo 2")