from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def mapa(request):
    return render(request, 'core/mapa.html')
    