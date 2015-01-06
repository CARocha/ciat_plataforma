# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from comunicacion.utils import *
from south.modelsinspector import add_introspection_rules
from ckeditor.fields import RichTextField
import datetime
from comunicacion.lugar.models import *
from sorl.thumbnail import ImageField

add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])

add_introspection_rules ([], ["^contrapartes\.models\.ColorField"])

# Create your models here.
from comunicacion.contrapartes.widgets import ColorPickerWidget

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)

CHOICE_LISTA = (
        (1, "Asociados"),
        (2, "Aliados")
    )

class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    codigo = models.CharField(max_length=2, 
                help_text='Código de 2 letras del país, ejemplo : Nicaragua (ni)')

    class Meta:
        verbose_name_plural = "Países"

    def __unicode__(self):
        return self.nombre

class Contraparte(models.Model):
    nombre = models.CharField(max_length=200)
    siglas = models.CharField("Siglas o nombre corto",help_text="Siglas o nombre corto de la oganización",max_length=200,blank=True, null=True)
    frecuecia = models.CharField('Frecuencia',max_length=50, null=True, blank=True)
    logo = ImageField(upload_to=get_file_path,null=True, blank=True)
    fileDir = 'contrapartes/logos/'
    pais = models.ForeignKey(Pais)
    municipio = models.ForeignKey(Municipio)
    tipo = models.IntegerField(choices=CHOICE_LISTA, null=True, blank=True)
    fundacion = models.CharField('Año de fundación', max_length=200, 
                                 blank=True, null=True)
    temas = RichTextField(blank=True, null=True)
    generalidades = RichTextField(blank=True, null=True)
    contacto = models.CharField(max_length=200,blank=True, null=True)
    telefono = models.CharField(max_length=200, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    rss = models.CharField(max_length=200,blank=True, null=True)
    font_color = ColorField(blank=True,unique=True)

    class Meta:
        verbose_name_plural = "Asociados"
        unique_together = ("font_color", "nombre")
        ordering = ['nombre',]

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return '/contrapartes/%d/' % (self.id,)

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # Other fields here
    contraparte = models.ForeignKey(Contraparte)
    avatar = ImageField(upload_to=get_file_path,
                                   null=True, blank=True)
    fileDir = 'usuario/avatar/'

    def __unicode__(self):
        return u"%s - %s" % (self.user.username, self.contraparte.nombre)

    def get_absolute_url(self):
        return '/usuario/%d/' % (self.user.id)

class Mensajero(models.Model):
    user = models.ManyToManyField(User)
    fecha = models.DateField(default=datetime.date.today())
    mensaje = RichTextField()
    usuario = models.CharField(max_length=200,blank=True, null=True)

    def __unicode__(self):
        return u'%s - %s ' % (self.fecha, self.mensaje)
