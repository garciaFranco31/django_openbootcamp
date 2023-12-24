from django.http import HttpResponse

def saludo(request): 
    """todas las funciones que realicemos, por lo general siempre van a recibir al menos un parametro de nombre 'request' """
    return HttpResponse("hola mundo")

def despedida(request):
    return HttpResponse("Hasta luego")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse('Eres mayor de edad')
    else:
        return HttpResponse('No eres mayor de edad')