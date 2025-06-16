from django.shortcuts import render

def index(request):
    return render(request, 'pagina/index.html')

def inicio(request):
    return render(request, 'pagina/hola.html')

def dreamjournal(request):
    return render(request, 'pagina/dreamjournal.html')
