# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from comunicacion.lugar.models import Comunidad, Departamento, Municipio, Pais
from comunicacion.utils import get_file_path
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField
from smart_selects.db_fields import ChainedForeignKey
from analisis.configuracion.models import Sector, AreaAccion, SitioAccion, Plataforma
from analysis.configuration.models import Sector_en
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from comunicacion.contrapartes.widgets import ColorPickerWidget
from south.modelsinspector import add_introspection_rules

add_introspection_rules ([], ["^mapeo\.models\.ColorField"])

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)

class Organizaciones(models.Model):
    nombre = models.CharField(_(u'Nombre'), max_length=200)
    siglas = models.CharField(_(u"Siglas o nombre corto"),
                                help_text=_(u"Siglas o nombre corto de la oganización"),
                                max_length=200)
    area_accion = models.ForeignKey(AreaAccion)
    sitio_accion = models.ForeignKey(SitioAccion)
    plataforma = models.ForeignKey(Plataforma)
    sector = models.ForeignKey(Sector,verbose_name=_(u'Sector (Español)'))
    sector_en = models.ForeignKey(Sector_en,verbose_name=_(u'Sector (Ingles)'),null=True, blank=True)
    telefono = models.IntegerField(_(u'Telefono'), null=True, blank=True)
    fax = models.CharField(max_length=50, null=True, blank=True)
    logo = ImageField(upload_to=get_file_path, null=True, blank=True)
    direccion = models.TextField(_(u'Direccion'), null=True, blank=True)

    pais = models.ForeignKey(Pais)
    departamento = ChainedForeignKey(
                                Departamento,
                                chained_field="pais",
                                chained_model_field="pais",
                                show_all=False, auto_choose=True,null=True, blank=True)
    municipio = ChainedForeignKey(
                                Municipio,
                                chained_field="departamento",
                                chained_model_field="departamento",
                                show_all=False, auto_choose=True,null=True, blank=True)
    fundacion = models.CharField(_(u'Año de fundación'),
                                 max_length=200,
                                 blank=True, null=True)
    temas = RichTextField(_(u'Temas'), blank=True, null=True)
    generalidades = RichTextField(_(u'Generalidades'), blank=True, null=True)
    contacto = models.CharField(_(u'Persona de contacto'), max_length=200, blank=True, null=True)
    correo_electronico = models.EmailField(_(u'Correo'), null=True, blank=True)
    telefono = models.CharField(_(u'Telefono'), max_length=200, blank=True, null=True)
    sitio_web = models.URLField(_(u'Sitio web'), blank=True, null=True)
    rss = models.CharField(max_length=200, blank=True, null=True)
    font_color = ColorField(blank=True, unique=True)

    fileDir = 'organizaciones/logos/'

    class Meta:
        verbose_name_plural = _(u"Organizaciones")
        unique_together = ("font_color", "nombre")
        ordering = ['nombre',]

    def __unicode__(self):
        return self.siglas

CHOICE_SEXO = ((1,_(u'Hombre')),(2,_(u'Mujer')))
CHOICE_SEXO_JEFE = ((1,_(u'Hombre')),(2,_(u'Mujer')),(3,_(u'Compartida')))
CHOICE_RANGO = (
                (1, '18 - 25'),
                (2, '26 - 45'),
                (3, '46 - 65'),
                (4, 'Más de 65')
            )

CHOICE_NIVEL_EDUCATIVO = (
                (1, _(u'No sabe leer o escribir')),
                (2, _(u'Primaria Incompleta')),
                (3, _(u'Primaria Completa')),
                (4, _(u'Secundaria Incompleta')),
                (5, _(u'Bachiller')),
                (6, _(u'Universitario')),
            )

CHOICE_TIPO_PERSONA = (
                (1, _(u'Productor o Productora')),
                (2, _(u'Líder o Lideresa comunitaria')),
                (3, _(u'Técnico')),
                (4, _(u'Especialista')),
                (5, _(u'Investigador')),
                (6, _(u'Decisor')),
            )

CHOICE_TIPOLOGIA = (
                (1, _(u'Pequeño campesino de montaña')),
                (2, _(u'Pequeño campesino diversificado')),
                (3, _(u'Finquero cacaotero')),
                (4, _(u'Finquero ganadero cacaotero')),
                (5, _(u'Finquero cafetalero')),
                (6, _(u'Finquero ganadero cafetalero')),
                (7, _(u'Finquero ganadero')),
            )

class Temas(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tema del proyecto/biblioteca'
        verbose_name_plural = 'Temas de los proyectos/bibliotecas'

class TiposProyectos(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo del proyecto'
        verbose_name_plural = 'Tipos de los proyectos'

class Proyectos(models.Model):
    nombre = models.CharField(max_length=250)
    corto = models.CharField(_(u"Nombre corto"),max_length=250)
    codigo = models.CharField(max_length=50)
    inicio = models.DateField(_(u"Fecha de inicio"))
    finalizacion = models.DateField(_(u"Fecha de finalización"))
    descripcion = models.TextField('Descripción del proyecto', null=True, blank=True)
    tipo = models.ForeignKey(TiposProyectos, verbose_name='Tipo proyecto', null=True, blank=True)
    temas = models.ManyToManyField(Temas, blank=True)
    encargado = models.CharField('Encargado del proyecto', max_length=250, null=True, blank=True)
    alianza = models.ManyToManyField(Plataforma, verbose_name=_(u"Alianza de influencia"))
    influencia = models.ManyToManyField(Municipio, verbose_name=_(u"Zona de influencia"))
    ejecutora = models.ForeignKey(Organizaciones, verbose_name=_(u"Organización ejecutora"))
    socias = models.ManyToManyField(Organizaciones, related_name="socias", verbose_name=_(u"Organización socias"))
    informacion = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.corto

    class Meta:
        verbose_name_plural = _(u"Proyectos")

class TimeLineProyecto(models.Model):
    proyecto = models.ForeignKey(Proyectos)
    fecha = models.DateField()
    texto = models.CharField(max_length=100)

    year = models.IntegerField(editable=False)
    mes = models.IntegerField(editable=False)

    def save(self):
        self.year = self.fecha.year
        self.mes = self.fecha.month
        super(TimeLineProyecto, self).save()

    def __unicode__(self):
        return u'%s - %s ' % (self.proyecto.corto, self.proyecto.codigo)



class Persona(models.Model):
    tipo_persona = models.IntegerField(choices=CHOICE_TIPO_PERSONA, null=True, blank=True)
    nombre = models.CharField(_(u'Nombre de la persona'), max_length=200)
    cedula = models.CharField(_(u'cedula de la persona'), max_length=200, null=True, blank=True)
    sexo = models.IntegerField(_(u'Sexo'), choices=CHOICE_SEXO)
    edad = models.IntegerField(_(u'Edad'), choices=CHOICE_RANGO)
    #finca = models.CharField(_(u'Nombre de Finca'), max_length=200, null=True, blank=True)
    pais = models.ForeignKey(Pais)
    departamento = ChainedForeignKey(
                                Departamento,
                                chained_field="pais",
                                chained_model_field="pais",
                                show_all=False, auto_choose=True)
    municipio = ChainedForeignKey(
                                Municipio,
                                chained_field="departamento",
                                chained_model_field="departamento",
                                show_all=False, auto_choose=True)
    comunidad = ChainedForeignKey(
                                Comunidad,
                                chained_field="municipio",
                                chained_model_field="municipio",
                                show_all=False, auto_choose=True)
    #organizacion = models.ManyToManyField(Organizaciones, related_name ="org",
                                        #verbose_name=_(u'Organizaciones que lo apoyan'))
    #nivel_educacion = models.IntegerField(_(u'Nivel de educacion'), choices=CHOICE_NIVEL_EDUCATIVO)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural= _(u'Personas registradas')

class RubrosAgropecuarios(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = _(u'Rubros agropecuarios')

class RubrosNoAgropecuarios(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = _(u'Rubros no agropecuarios')

class FuenteManoObra(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = _(u'Fuentes de mano de obra')

class FormaAtencion(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = _(u'Formas en que atiende')

class Productor(models.Model):
    persona = models.ForeignKey(Persona)
    fecha = models.DateField()
    finca = models.CharField(_(u'Nombre de Finca'), max_length=200, null=True, blank=True)
    organizacion = models.ManyToManyField(Organizaciones, related_name ="organizacion",
                                        verbose_name=_(u'Organizaciones que lo apoyan'), blank=True)
    tamano = models.FloatField(_(u'Tamaño de la finca'), null=True, blank=True)
    ganado = models.IntegerField(_(u'Número de ganado'), null=True, blank=True)
    rubros_agro = models.ManyToManyField(RubrosAgropecuarios, related_name="uno", verbose_name=_(u'Rubros que generan ingreso agropecuario'), blank=True)
    rubro_principal_agro = models.ForeignKey(RubrosAgropecuarios, related_name="dos", null=True, blank=True)
    rubros_no_agro = models.ManyToManyField(RubrosNoAgropecuarios, related_name="tres", verbose_name=_(u'Rubros que generan ingreso no agropecuario'), blank=True)
    rubro_principal_no_agro = models.ForeignKey(RubrosNoAgropecuarios, related_name="cuatro", null=True, blank=True)
    fuente = models.ManyToManyField(FuenteManoObra, verbose_name=_(u'Fuente de mano de obra'), blank=True)
    jefe = models.IntegerField(choices=CHOICE_SEXO_JEFE, verbose_name=_(u'Jefe de familia'), null=True, blank=True)
    tipologia = models.IntegerField(choices=CHOICE_TIPOLOGIA, null=True, blank=True)
    proyecto = models.ManyToManyField(Proyectos, blank=True)

    fecha1 = models.IntegerField(editable=False, null=True, blank=True)

    def save(self):
        self.fecha1 = self.fecha.year
        super(Productor, self).save()

    class Meta:
        verbose_name_plural = _(u'Información productor/productora')



class Lideres(models.Model):
    persona = models.ForeignKey(Persona)
    fecha = models.DateField()
    finca = models.CharField(_(u'Nombre de Finca'), max_length=200, null=True, blank=True)
    organizacion = models.ManyToManyField(Organizaciones, related_name ="org",
                                        verbose_name=_(u'Organizaciones que lo apoyan'),null=True, blank=True)
    tamano = models.FloatField(_(u'Tamaño de la finca'), null=True, blank=True)
    ganado = models.IntegerField(_(u'Número de ganado'), null=True, blank=True)
    rubros_agro = models.ManyToManyField(RubrosAgropecuarios, related_name="agro", verbose_name=_(u'Rubros que generan ingreso agropecuario'), blank=True)
    rubro_principal_agro = models.ForeignKey(RubrosAgropecuarios, related_name="principal", null=True, blank=True)
    rubros_no_agro = models.ManyToManyField(RubrosNoAgropecuarios, related_name="noagro", verbose_name=_(u'Rubros que generan ingreso no agropecuario'), blank=True)
    rubro_principal_no_agro = models.ForeignKey(RubrosNoAgropecuarios, related_name="principalno", null=True, blank=True)
    fuente = models.ManyToManyField(FuenteManoObra, verbose_name=_(u'Fuente de mano de obra'), blank=True)
    jefe = models.IntegerField(choices=CHOICE_SEXO_JEFE, verbose_name=_(u'Jefe de familia'), null=True, blank=True)
    tipologia = models.IntegerField(choices=CHOICE_TIPOLOGIA, null=True, blank=True)
    correo_electronico = models.EmailField(_(u'Correo'), null=True, blank=True)
    atiende = models.IntegerField(_(u'Número de personas que atiende'), null=True, blank=True)
    forma_atiende = models.ManyToManyField(FormaAtencion, verbose_name=_(u'Forma de atención'), blank=True)
    proyecto = models.ManyToManyField(Proyectos, blank=True)

    class Meta:
        verbose_name_plural = _(u'Líder o Lideresa comunitaria')


CHOICE_FORMACION = (
                (1, _(u'(Bachiller')),
                (2, _(u'Técnico')),
                (3, _(u'Ingeniero')),
                (4, _(u'Licenciado')),
                (5, _(u'Maestría')),
                (6, _(u'Doctorado')),
            )

class Especialidades(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = _(u'Especialidades')

class TecnicoEspInvestigador(models.Model):
    persona = models.ForeignKey(Persona)
    formacion = models.IntegerField(choices=CHOICE_FORMACION, null=True, blank=True)
    experiencia = models.CharField(max_length=250, null=True, blank=True)
    correo_electronico = models.EmailField(_(u'Correo'), null=True, blank=True)
    especialidad = models.ManyToManyField(Especialidades, blank=True)
    pertenece = models.ManyToManyField(Organizaciones,
            verbose_name=_(u'Organizaciones a que pertenece'), blank=True)
    proyecto = models.ManyToManyField(Proyectos,
            verbose_name=_(u'Vinculado a proyectos'), blank=True)

    class Meta:
        verbose_name_plural = _(u'Técnico, Especialista o Investigador')

class Accionar(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = _(u'Niveles de accionar')

class CampoAccion(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = _(u'Campos de acción')

class Decisor(models.Model):
    persona = models.ForeignKey(Persona)
    correo_electronico = models.EmailField(_(u'Correo'), null=True, blank=True)
    nivel = models.ManyToManyField(Accionar,
                verbose_name=_(u'Nivel de accionar'), blank=True)
    campo = models.ManyToManyField(CampoAccion,
                verbose_name=_(u'Campo de acción'), blank=True)
    pertenece = models.ManyToManyField(Organizaciones,
            verbose_name=_(u'Organizaciones a que pertenece'), blank=True)
    proyecto = models.ManyToManyField(Proyectos,
            verbose_name=_(u'Vinculado a proyectos'), blank=True)

    class Meta:
        verbose_name_plural = _(u'Decisor')

RELACION_CHOICES = (
    (1,'1-Jefe/Jefa de familia'),
    (2,'2-Cónyuge'),
    (3,'3-Hijo/Hija'),
    (4,'4-Otro familiar'),
    (5,'5-Administrador'),
)

class ProductorGranosBasicos(models.Model):
    persona = models.ForeignKey(Persona)
    # organizacion = models.ManyToManyField(Organizaciones,verbose_name='Organización a la que está afiliado/a.',blank=True, null=True)
    #nombre_finca = models.CharField(max_length=200)
    telefono = models.IntegerField()
    # latitud = models.IntegerField()
    # longitud = models.IntegerField()
    latitud1 = models.FloatField(blank=True, null=True,verbose_name='Latitud')
    longitud1 = models.FloatField(blank=True, null=True,verbose_name='Longitud')
    nombre_productor = models.CharField(max_length=200,verbose_name='Nombre de el/la productor/a de la parcela GB')
    relacion = models.IntegerField(choices=RELACION_CHOICES,verbose_name='Relación de el/la productor/a con el/la responsable de Familia.')

    class Meta:
        verbose_name_plural = 'Productor/a de Granos Básicos'

USO_SUELO_CHOICES = (
    (1,'Área Total'),
    (2,'Cultivos Anuales (GB)'),
    (3,'Cultivos perennes'),
    (4,'Tacotales'),
    (5,'Potreros'),
    (6,'Pasto de Corte'),
)

class UsoSuelo(models.Model):
    persona = models.ForeignKey(Persona)
    uso = models.IntegerField(choices=USO_SUELO_CHOICES)
    cantidad = models.FloatField(verbose_name='Cantidad en mz')

    class Meta:
        verbose_name_plural = 'Uso de Suelo de la finca'

FAMILIA_CHOICES = (
    (1,'1-Padre'),
    (2,'2-Madre'),
    (3,'3-Hijo'),
    (4,'4-Hija'),
    (5,'5-Hermano'),
    (6,'6-Hermana'),
    (7,'7-Sobrino'),
    (8,'8-Sobrina'),
    (9,'9-Abuelo'),
    (10,'10-Abuela'),
    (11,'11-Cuñado'),
    (12,'12-Cuñada'),
    (13,'13-Yerno'),
    (14,'14-Nuera'),
    (15,'15-Otro'),
)

ESCOLARIDAD_CHOICES = (
    (1,'1-Ninguno'),
    (2,'2-Primaria Incompleta'),
    (3,'3-Primaria'),
    (4,'4-Secundaria Incompleta'),
    (5,'5-Secundaria'),
    (6,'6-Técnico'),
    (7,'7-Universitario'),
    (8,'8-Profesional'),
)

SI_NO_CHOICES = (
    (1,'1-Si'),
    (2,'2-No'),
)

class ComposicionFamiliar(models.Model):
    persona = models.ForeignKey(Persona)
    familia = models.IntegerField(choices=FAMILIA_CHOICES)
    edad = models.IntegerField()
    escolaridad = models.IntegerField(choices=ESCOLARIDAD_CHOICES,verbose_name='Nivel de Escolaridad')
    participacion = models.IntegerField(choices=SI_NO_CHOICES,verbose_name='Participa en la parcela de Granos Básicos')

    class Meta:
        verbose_name_plural = 'Composición Familiar'
