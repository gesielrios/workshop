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