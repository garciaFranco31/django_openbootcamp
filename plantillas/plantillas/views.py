from django.shortcuts import render #render permite renderizar el contenido de un archivo

def simple(request):
    return render(request, 'simple.html',{})