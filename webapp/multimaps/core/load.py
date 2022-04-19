import os

from django.contrib.gis.utils import LayerMapping

from .models import Conflito, Climatico, Fome, Peste

evento_mapping = {
    'id': 'id',
    'nome': 'nome',
    'nome_semacento': 'nome_semac',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'fonte': 'fonte',
    'p_1276_1300': 'p_1276_130',
    'p_1301_1325': 'p_1301_132',
    'p_1326_1350': 'p_1326_135',
    'p_1351_1375': 'p_1351_137',
    'p_1376_1400': 'p_1376_140',
    'p_1401_1425': 'p_1401_142',
    'p_1426_1450': 'p_1426_145',
    'p_1451_1475': 'p_1451_147',
    'p_1476_1500': 'p_1476_150',
    'geom': 'POINT',
}

conflitos_shp_path = os.path.abspath(os.path.join('../../data/shp', 'conflitos.shp'))
eventos_climaticos_shp_path = os.path.abspath(os.path.join('../../data/shp', 'eventos_climaticos.shp'))
fome_shp_path = os.path.abspath(os.path.join('../../data/shp', 'fome.shp'))
peste_shp_path = os.path.abspath(os.path.join('../../data/shp', 'peste.shp'))

def conflitos_mapping(verbose=True):
    conflitos_lm = LayerMapping(Conflito, conflitos_shp_path, evento_mapping)
    conflitos_lm.save(strict=True, verbose=verbose, progress=True)

def eventos_climaticos_mapping(verbose=True):
    eventos_climaticos_lm = LayerMapping(Climatico, eventos_climaticos_shp_path, evento_mapping)
    eventos_climaticos_lm.save(strict=True, verbose=verbose, progress=True)

def fome_mapping(verbose=True):
    fome_lm = LayerMapping(Fome, fome_shp_path, evento_mapping)
    fome_lm.save(strict=True, verbose=verbose, progress=True)

def peste_mapping(verbose=True):
    peste_lm = LayerMapping(Peste, peste_shp_path, evento_mapping)
    peste_lm.save(strict=True, verbose=verbose, progress=True)
