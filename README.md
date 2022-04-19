<p align="center">
    <img src="github/multimaps-logo.svg" alt="Logo" width="300"/><br><br>
</p>

# Workshop MultiMaps

## 📖 Sobre

Workshop realizado junto ao Programa de Pós-Graduação em História Social-FFLCH-USP e Laboratório de Estudos Medievais sobre as ferramentas utilizadas no MultiMapas.

------------
## 🧪 Tecnologias

O projeto foi desenvolvido utilizando:

&rarr; <a href="https://www.python.org/" target="_blank">Python</a> <br>
&rarr; <a href="https://www.djangoproject.com/" target="_blank">DJango</a> <br>

------------
## 🔌 Começando

Clone o projeto:

```bash
$ git clone https://github.com/gesielrios/workshop.git
```

Acessando o diretório e instalando as dependências:

```bash
$ cd workshop

# Create a virtual env for the dependencies
$ python -m venv .venv
$ source .venv/bin/activate

# Install the dependencies
$ pip install -r requirements.txt
```

### Gerando os modelos a partir dos shapefiles:

O comando `ogrinspect` é utilizado para inspecionar um arquivo shapefile e tem como saída um modelo, no qual o seu nome deve ser fornecido pelo usuário, e os campos, definidos de acordo com os atributos do arquivo lido.

```bash
python manage.py ogrinspect ../../data/shp/conflitos.shp Evento --srid 4326 --mapping
```

Com o `LayerMapping` é possível criar o arquivo `load.py`:

```python
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
```

Gerando os modelos:

```python
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

class TipoEvento(models.TextChoices):
        CONFLITO = 'CONFLITO', _('conflito')
        CLIMATICO = 'CLIMATICO', _('evento_climatico')
        FOME = 'FOME', _('fome')
        PESTE = 'PESTE', _('peste')    

class Evento(models.Model):
    
    nome = models.CharField(max_length=255)
    nome_semacento = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    fonte = models.CharField(max_length=255, null=True, blank=True)
    p_1276_1300 = models.FloatField(null=True, blank=True)
    p_1301_1325 = models.FloatField(null=True, blank=True)
    p_1326_1350 = models.FloatField(null=True, blank=True)
    p_1351_1375 = models.FloatField(null=True, blank=True)
    p_1376_1400 = models.FloatField(null=True, blank=True)
    p_1401_1425 = models.FloatField(null=True, blank=True)
    p_1426_1450 = models.FloatField(null=True, blank=True)
    p_1451_1475 = models.FloatField(null=True, blank=True)
    p_1476_1500 = models.FloatField(null=True, blank=True)
    geom = models.PointField(srid=4326)
    
    @property
    def popup_content(self):
        popup = "<b>Evento</b><br/>"
        popup += "Nome: {}<br/>".format(self.nome)
            
        if self.fonte is not None:
            popup += "Fonte: {}<br/>".format(self.fonte)
        
        if self.p_1276_1300 is not None:
            popup += "Período 1276 a 1300: " + str(int(self.p_1276_1300)) + "<br/>"
        
        if self.p_1301_1325 is not None:
            popup += "Período 1301 a 1325: " + str(int(self.p_1301_1325)) + "<br/>"
        
        if self.p_1326_1350 is not None:
            popup += "Período 1326 a 1350: " + str(int(self.p_1326_1350)) + "<br/>"
        
        if self.p_1351_1375 is not None:
            popup += "Período 1351 a 1375: " + str(int(self.p_1351_1375)) + "<br/>"
        
        if self.p_1376_1400 is not None:
            popup += "Período 1376 a 1400: " + str(int(self.p_1376_1400)) + "<br/>"
        
        if self.p_1401_1425 is not None:
            popup += "Período 1401 a 1425: " + str(int(self.p_1401_1425)) + "<br/>"
        
        if self.p_1426_1450 is not None:
            popup += "Período 1426 a 1450: " + str(int(self.p_1426_1450)) + "<br/>"
        
        if self.p_1451_1475 is not None:
            popup += "Período 1451 a 1475: " + str(int(self.p_1451_1475)) + "<br/>"
        
        if self.p_1476_1500 is not None:
            popup += "Período 1476 a 1500: " + str(int(self.p_1476_1500)) + "<br/>"
        
        return popup
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

class Conflito(Evento):
    tipo = models.CharField(
        max_length=10,
        choices=TipoEvento.choices,
        default=TipoEvento.CONFLITO,
    )
    
    class Meta:
        db_table = "conflitos"

class Climatico(Evento):
    tipo = models.CharField(
        max_length=10,
        choices=TipoEvento.choices,
        default=TipoEvento.CLIMATICO,
    )
    
    class Meta:
        db_table = "eventos_climaticos"

class Fome(Evento):
    tipo = models.CharField(
        max_length=10,
        choices=TipoEvento.choices,
        default=TipoEvento.FOME,
    )
    
    class Meta:
        db_table = "fomes"
    
class Peste(Evento):
    tipo = models.CharField(
        max_length=10,
        choices=TipoEvento.choices,
        default=TipoEvento.PESTE,
    )
    
    class Meta:
        db_table = "pestes"  
```

Mapeamento (arquivo `load.py`) :

```python
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

```

### Carga de dados:

```bash
from core.load import conflitos_mapping, eventos_climaticos_mapping, fome_mapping, peste_mapping

conflitos_mapping()
eventos_climaticos_mapping()
fome_mapping()
peste_mapping()
```

------------
## 🎓 Agradecimentos

👨‍🏫  Prof. José Francisco Sanches Fonseca do Programa de Pós-Graduação em História Social  FFLCH-USP ao Laboratório de Estudos Medievais.

------------
## 📝 Licença
Este projeto está licenciado sob a Licença MIT.