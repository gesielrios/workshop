from attr import field
from django.shortcuts import render
from django.http import JsonResponse

from djgeojson.serializers import Serializer as GeoJSONSerializer

from .models import TipoEvento, Conflito, Climatico, Fome, Peste

fields = ('nome', 'fonte', 'tipo', 'popup_content',)

def index(request):
    return render(request, 'core/index.html')

def mapa(request):
           
    conflitos = Conflito.objects.filter(tipo__iexact=TipoEvento.CONFLITO)
    eventos_climaticos = Climatico.objects.filter(tipo__iexact=TipoEvento.CLIMATICO)
    fomes = Fome.objects.filter(tipo__iexact=TipoEvento.FOME)
    pestes = Peste.objects.filter(tipo__iexact=TipoEvento.PESTE)    
        
    context = {
        'conflitos_geojson': GeoJSONSerializer().serialize(
            conflitos, 
            use_natural_keys=True,
            properties=fields,
            
        ),
        'eventos_climaticos_geojson': GeoJSONSerializer().serialize(
            eventos_climaticos, 
            use_natural_keys=True,
            properties=fields,
        ),
        'fomes_geojson': GeoJSONSerializer().serialize(
            fomes, 
            use_natural_keys=True,
            properties=fields,
        ),
        'pestes_geojson': GeoJSONSerializer().serialize(
            pestes, 
            use_natural_keys=True,
            properties=fields,
        ),
    }
    
    return render(request, 'core/mapa.html', context=context)

def filtro_periodo(request):
    
    periodo = request.GET.get('periodo')
    
    conflitos = Conflito.objects.filter(tipo__iexact=TipoEvento.CONFLITO)
    eventos_climaticos = Climatico.objects.filter(tipo__iexact=TipoEvento.CLIMATICO)
    fomes = Fome.objects.filter(tipo__iexact=TipoEvento.FOME)
    pestes = Peste.objects.filter(tipo__iexact=TipoEvento.PESTE) 
    
    if periodo == '1276-1300':
        conflitos = conflitos.filter(p_1276_1300__isnull=False)
        eventos_climaticos = eventos_climaticos.filter(p_1276_1300__isnull=False)
        fomes = fomes.filter(p_1276_1300__isnull=False)
        pestes = pestes.filter(p_1276_1300__isnull=False)
    
    if periodo == '1301-1325':
        conflitos = conflitos.filter(p_1301_1325__isnull=False)
        eventos_climaticos = eventos_climaticos.filter(p_1301_1325__isnull=False)
        fomes = fomes.filter(p_1301_1325__isnull=False)
        pestes = pestes.filter(p_1301_1325__isnull=False)
    
    if periodo == '1326-1350':
        conflitos = conflitos.filter(p_1326_1350__isnull=False)
        eventos_climaticos = eventos_climaticos.filter(p_1326_1350__isnull=False)
        fomes = fomes.filter(p_1326_1350__isnull=False)
        pestes = pestes.filter(p_1326_1350__isnull=False)
    
    if periodo == '1351-1375':
        conflitos = conflitos.filter(p_1351_1375__isnull=False)
        eventos_climaticos = eventos_climaticos.filter(p_1351_1375__isnull=False)
        fomes = fomes.filter(p_1351_1375__isnull=False)
        pestes = pestes.filter(p_1351_1375__isnull=False)
    
    if periodo == '1376-1400':
        conflitos = conflitos.filter(p_1376_1400__isnull=False)
        eventos_climaticos = eventos_climaticos.filter(p_1376_1400__isnull=False)
        fomes = fomes.filter(p_1376_1400__isnull=False)
        pestes = pestes.filter(p_1376_1400__isnull=False)
    
    if periodo == '1401-1425':
        conflitos = conflitos.filter(p_1401_1425__isnull=False)
        eventos_climaticos = eventos_climaticos.filter(p_1401_1425__isnull=False)
        fomes = fomes.filter(p_1401_1425__isnull=False)
        pestes = pestes.filter(p_1401_1425__isnull=False)
    
    if periodo == '1426-1450':
        conflitos = conflitos.filter(p_1426_1450__isnull=False)
        eventos_climaticos = eventos_climaticos.filter(p_1426_1450__isnull=False)
        fomes = fomes.filter(p_1426_1450__isnull=False)
        pestes = pestes.filter(p_1426_1450__isnull=False)
    
    if periodo == '1451-1475':
        conflitos = conflitos.filter(p_1451_1475__isnull=False)
        eventos_climaticos = eventos_climaticos.filter(p_1451_1475__isnull=False)
        fomes = fomes.filter(p_1451_1475__isnull=False)
        pestes = pestes.filter(p_1451_1475__isnull=False)
    
    if periodo == '1476-1500':
        conflitos = conflitos.filter(p_1476_1500__isnull=False)
        eventos_climaticos = eventos_climaticos.filter(p_1476_1500__isnull=False)
        fomes = fomes.filter(p_1476_1500__isnull=False)
        pestes = pestes.filter(p_1476_1500__isnull=False)
    
    context = {
        'conflitos_geojson': GeoJSONSerializer().serialize(
            conflitos, 
            use_natural_keys=True,
            properties=fields,
        ),
        'eventos_climaticos_geojson': GeoJSONSerializer().serialize(
            eventos_climaticos, 
            use_natural_keys=True,
            properties=fields,
        ),
        'fomes_geojson': GeoJSONSerializer().serialize(
            fomes, 
            use_natural_keys=True,
            properties=fields,
        ),
        'pestes_geojson': GeoJSONSerializer().serialize(
            pestes, 
            use_natural_keys=True,
            properties=fields,
        ),
    }
    
    return JsonResponse(context)
    
    
    