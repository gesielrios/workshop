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