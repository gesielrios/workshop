from django.shortcuts import render

from djgeojson.serializers import Serializer as GeoJSONSerializer

from .models import Conflito, Climatico, Fome, Peste, TipoEvento

def index(request):
    return render(request, 'core/index.html')

def mapa(request):
    
    fields = ('nome', 'fonte', 'tipo', 'popup_content',)    
    conflitos = Conflito.objects.filter(tipo__iexact=TipoEvento.CONFLITO)
    
    context = {
        'conflitos_geojson': GeoJSONSerializer().serialize(
            conflitos, 
            use_natural_keys=True,
            properties=fields,
            
        ),
    }
    
    return render(request, 'core/mapa.html', context=context)
    