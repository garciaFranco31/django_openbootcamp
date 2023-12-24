from django.shortcuts import render #render permite renderizar el contenido de un archivo

def simple(request):
    return render(request, 'simple.html',{})

def dinamico(request, name):
    categories = ['code', 'design', 'marketing', 'CEO', 'manager']
    context = {'name': name, 'categories': categories}
    return render(request, 'dinamico.html', context)