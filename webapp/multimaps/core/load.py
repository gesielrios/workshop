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

def conflito_mapping(verbose=True):
    lm = LayerMapping(Conflito, conflitos_shp_path, evento_mapping)
    lm.save(strict=True, verbose=verbose)