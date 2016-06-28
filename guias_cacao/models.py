# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from mapeo.models import Persona
from sorl.thumbnail import ImageField
from multiselectfield import MultiSelectField

# Create your models here.
class FichaSombra(models.Model):
    productor = models.ForeignKey(
        Persona,
        verbose_name='Nombre de productor o productora',
        related_name='persona_productor')
    tecnico = models.ForeignKey(
        Persona,
        verbose_name='Nombre de técnico',
        related_name='persona_tecnico')
    fecha_visita = models.DateField()

    def __unicode__(self):
        return self.productor.nombre

    class Meta:
        verbose_name = "Ficha sombra"
        verbose_name_plural = "Ficha sombra"


class Foto1(models.Model):
    """docstring for Foto1"""
    foto = ImageField(upload_to='foto1Sombra')
    ficha = models.ForeignKey(FichaSombra)

CHOICE_TIPO_PUNTO = (
    (1, 'Perennifolia'),
    (2, 'Caducifolia'),
)

CHOICE_TIPO_USO_PUNTO = (
    (1, 'Leña'),
    (2, 'Fruta'),
    (3, 'Madera'),
    (4, 'Sombra'),
    (5, 'Nutrientes'),
)

class Especies(models.Model):
    nombre = models.CharField('Nombre de la especie', max_length=250)
    nombre_cientifico = models.CharField('Nombre cientifico de la especie', max_length=250, blank=True, null=True)
    tipo = models.IntegerField(choices=CHOICE_TIPO_PUNTO, blank=True, null=True)
    tipo_uso = MultiSelectField(choices=CHOICE_TIPO_USO_PUNTO, verbose_name='Tipo de uso', blank=True, null=True)
    foto = ImageField(upload_to='fotoEspecies', blank=True, null=True)
    #pequenio
    p_altura = models.FloatField('Altura en (mt)', blank=True, null=True)
    p_diametro = models.FloatField('Diametro en (cm)', blank=True, null=True)
    p_ancho = models.FloatField('Ancho copa en (mt)s', blank=True, null=True)
    #mediano
    m_altura = models.FloatField('Altura en (mt)', blank=True, null=True)
    m_diametro = models.FloatField('Diametro en (cm)', blank=True, null=True)
    m_ancho = models.FloatField('Ancho copa en (mt)s', blank=True, null=True)
    #grande
    g_altura = models.FloatField('Altura en (mt)', blank=True, null=True)
    g_diametro = models.FloatField('Diametro en (cm)', blank=True, null=True)
    g_ancho = models.FloatField('Ancho copa en (mt)s', blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Especie"
        verbose_name_plural = "Especies"


CHOICE_TIPO_COPA_PUNTO = (
    (1, 'Copa ancha'),
    (2, 'Copa angosta'),
    (3, 'Copa mediana'),
)


class Punto1(models.Model):
    especie = models.ForeignKey(Especies)
    pequena = models.FloatField(verbose_name='Pequeña')
    mediana = models.FloatField(verbose_name='Mediana')
    grande = models.FloatField(verbose_name='Grande')
    tipo = models.IntegerField(choices=CHOICE_TIPO_PUNTO)
    tipo_de_copa = models.IntegerField(choices=CHOICE_TIPO_COPA_PUNTO)
    uso = models.IntegerField(choices=CHOICE_TIPO_USO_PUNTO)

    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name_plural = "Punto1"


class Cobertura1(models.Model):
    cobertura = models.FloatField('% de cobertura de sombra')
    ficha = models.ForeignKey(FichaSombra)

#------------------- fin de punto 1 --------------------------------------


class Foto2(models.Model):
    """docstring for Foto2"""
    foto = ImageField(upload_to='foto2Sombra')
    ficha = models.ForeignKey(FichaSombra)


class Punto2(models.Model):
    especie = models.ForeignKey(Especies)
    pequena = models.FloatField(verbose_name='Pequeña')
    mediana = models.FloatField(verbose_name='Mediana')
    grande = models.FloatField(verbose_name='Grande')
    tipo = models.IntegerField(choices=CHOICE_TIPO_PUNTO)
    tipo_de_copa = models.IntegerField(choices=CHOICE_TIPO_COPA_PUNTO)
    uso = models.IntegerField(choices=CHOICE_TIPO_USO_PUNTO)

    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name_plural = "Punto2"


class Cobertura2(models.Model):
    cobertura = models.FloatField('% de cobertura de sombra')
    ficha = models.ForeignKey(FichaSombra)

#------------------- fin de punto 2 --------------------------------------


class Foto3(models.Model):
    """docstring for Foto3"""
    foto = ImageField(upload_to='foto3Sombra')
    ficha = models.ForeignKey(FichaSombra)


class Punto3(models.Model):
    especie = models.ForeignKey(Especies)
    pequena = models.FloatField(verbose_name='Pequeña')
    mediana = models.FloatField(verbose_name='Mediana')
    grande = models.FloatField(verbose_name='Grande')
    tipo = models.IntegerField(choices=CHOICE_TIPO_PUNTO)
    tipo_de_copa = models.IntegerField(choices=CHOICE_TIPO_COPA_PUNTO)
    uso = models.IntegerField(choices=CHOICE_TIPO_USO_PUNTO)

    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name_plural = "Punto3"


class Cobertura3(models.Model):
    cobertura = models.FloatField('% de cobertura de sombra')
    ficha = models.ForeignKey(FichaSombra)

#------------------- fin de punto 3 --------------------------------------


class AnalisisSombra(models.Model):
    densidad = models.IntegerField(
        choices=(
            (1,
             'Alta'),
            (2,
             'Adecuada'),
            (3,
             'Baja'),
        ),
        verbose_name='Densidad de árboles de sombra')
    forma_copa = models.IntegerField(
        choices=(
            (1,
             'Ancha'),
            (2,
             'Adecuada'),
            (3,
             'Angosta'),
        ),
        verbose_name='Forma de copa de árboles de sombra')
    arreglo = models.IntegerField(choices=((1, 'Uniforme'), (2, 'Desuniforme'),),
                                  verbose_name='Arreglo de árboles')
    hojarasca = models.IntegerField(
        choices=(
            (1,
             'Suficiente'),
            (2,
             'No Suficiente'),
        ),
        verbose_name='Cantidad de hojarasca ')
    calidad_hojarasca = models.IntegerField(
        choices=(
            (1,
             'Rico en nutrientes'),
            (2,
             'Pobre en nutriente'),
        ),
        verbose_name='Calidad de hojarasca ')
    competencia = models.IntegerField(
        choices=(
            (1,
             'Fuerte'),
            (2,
             'Mediana'),
            (3,
             'Leve'),
        ),
        verbose_name='Competencia de árboles con cacao')
    Problema = models.IntegerField(
        choices=(
            (1,
             'Cobertura'),
            (2,
             'Mal arreglo'),
            (3,
             'Competencia'),
            (4,
             'Densidad Tipo de árboles'),
            (5,
             'Ninguno')),
        verbose_name='Problema de sombra')
    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name_plural = "Análisis sobre sombra y árboles de sombra"

CHOICE_ACCIONES_SOMBRA = (
    (1, 'Reducir la sombra'),
    (2, 'Aumentar la sombra'),
    (3, 'Ninguna'),
)

CHOICE_PODA = (
    (1, 'Si'),
    (2, 'No'),
)

CHOICE_TODO = (
    (1, 'En todo la parcela '),
    (2, 'Solo en una parte de la parcela'),
)


class AccionesSombra(models.Model):
    accion = models.IntegerField(
        choices=CHOICE_ACCIONES_SOMBRA,
        verbose_name="Que acciones hay que realizar ")
    ficha = models.ForeignKey(FichaSombra)


class ReducirSombra(models.Model):
    poda = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Podando árboles")
    poda_cuales = models.CharField(max_length=350)
    eliminando = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Cambiando árboles")
    eliminando_cuales = models.CharField(max_length=350)
    todo = models.IntegerField(
        choices=CHOICE_TODO,
        verbose_name="En todo la parcela o Solo en una parte de la parcela")
    que_parte = models.CharField(max_length=250)
    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name_plural = "Si marca reducir la sombra"


class AumentarSombra(models.Model):
    sembrando = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Sembrando árboles")
    sembrando_cuales = models.CharField(max_length=350)
    cambiando = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Cambiando árboles")
    cambiando_cuales = models.CharField(max_length=350)
    todo = models.IntegerField(
        choices=CHOICE_TODO,
        verbose_name="En todo la parcela o Solo en una parte de la parcela")
    que_parte = models.CharField(max_length=250)
    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name_plural = "Si marca aumentar la sombra"


class ManejoSombra(models.Model):
    herramientas = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Tiene herramienta para manejo de sombra? ")
    formacion = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Tiene formación para manejo de sombra? ")
    ficha = models.ForeignKey(FichaSombra)

    class Meta:
        verbose_name = "Herramienta y formación de sombras"

#-------------------------- fin ficha sombra ------------------------------

class FichaPoda(models.Model):
    productor = models.ForeignKey(
        Persona,
        verbose_name='Nombre de productor o productora',
        related_name='setproductor')
    tecnico = models.ForeignKey(
        Persona,
        verbose_name='Nombre de técnico',
        related_name='settecnico')
    fecha_visita = models.DateField()

    def __unicode__(self):
        return self.productor.nombre

    class Meta:
        verbose_name = "Ficha poda"
        verbose_name_plural = "Ficha poda"

CHOICE_SI_NO = (
    (1, 'Si'),
    (2, 'No'),
)
CHOICE_PRODUCCION = (
    (1, 'Alta'),
    (2, 'Media'),
    (3, 'Baja'),
)
CHOICE_PLANTAS1 = (
    (1, 'Altura en mt'),
    (2, 'Ancho de copa mt'),
)
CHOICE_PLANTAS2 = (
    (1,
     'Formación de horqueta'),
    (2,
     'Ramas en contacto '),
    (3,
     'Ramas entrecruzadas'),
    (4,
     'Ramas cercanas al suelo'),
    (5,
     'Chupones'),
    (6,
     'Penetración de Luz'),
    )
CHOICE_PLANTAS3 = (
    (1, 'Nivel de producción'),
)


class Punto1A(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS1)
    uno = models.FloatField(verbose_name='1')
    dos = models.FloatField(verbose_name='2')
    tres = models.FloatField(verbose_name='3')
    cuatro = models.FloatField(verbose_name='4')
    cinco = models.FloatField(verbose_name='5')
    seis = models.FloatField(verbose_name='6')
    siete = models.FloatField(verbose_name='7')
    ocho = models.FloatField(verbose_name='8')
    nueve = models.FloatField(verbose_name='9')
    diez = models.FloatField(null=True, blank=True, verbose_name='10')

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto1B(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS2)
    uno = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto1C(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return self.get_plantas_display()

#----------------------------- fin del punto 1 ---------------------------


class Punto2A(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS1)
    uno = models.FloatField(verbose_name='1')
    dos = models.FloatField(verbose_name='2')
    tres = models.FloatField(verbose_name='3')
    cuatro = models.FloatField(verbose_name='4')
    cinco = models.FloatField(verbose_name='5')
    seis = models.FloatField(verbose_name='6')
    siete = models.FloatField(verbose_name='7')
    ocho = models.FloatField(verbose_name='8')
    nueve = models.FloatField(verbose_name='9')
    diez = models.FloatField(null=True, blank=True, verbose_name='10')

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto2B(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS2)
    uno = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto2C(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return self.get_plantas_display()

#------------ fin del punto 2 ----------------------------


class Punto3A(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS1)
    uno = models.FloatField(verbose_name='1')
    dos = models.FloatField(verbose_name='2')
    tres = models.FloatField(verbose_name='3')
    cuatro = models.FloatField(verbose_name='4')
    cinco = models.FloatField(verbose_name='5')
    seis = models.FloatField(verbose_name='6')
    siete = models.FloatField(verbose_name='7')
    ocho = models.FloatField(verbose_name='8')
    nueve = models.FloatField(verbose_name='9')
    diez = models.FloatField(null=True, blank=True, verbose_name='10')

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto3B(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS2)
    uno = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_SI_NO, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return self.get_plantas_display()


class Punto3C(models.Model):
    plantas = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='1')
    dos = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='2')
    tres = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='3')
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='4')
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='5')
    seis = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='6')
    siete = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='7')
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='8')
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='9')
    diez = models.IntegerField(choices=CHOICE_PRODUCCION, verbose_name='10', null=True, blank=True)

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return self.get_plantas_display()

# -------------------- fin punto 3 ----------------------------

CHOICES_PROBLEMA_PLANTA = (('A', 'Altura'),
                           ('B', 'Ancho'),
                           ('C', 'Ramas'),
                           ('D', 'Horqueta'),
                           ('E', 'Chupones'),
                           ('F', 'Poca entrada de Luz'),
                           ('G', 'Baja productividad'),
                           ('H', 'Ninguna'),
                           )
CHOICES_TIPO_PODA = (('A', 'Poda de copa'),
                     ('B', 'Poda de ramas'),
                     ('C', 'Ramas'),
                     ('D', 'Formar horquetas'),
                     ('E', 'Deschuponar'),
                     ('F', 'Ninguna'),
                     )

CHOICE_REALIZA_PODA = (
    (1, 'En toda la parcela'),
    (2, 'En Varios partes'),
    (3, 'En algunas partes'), )
CHOICE_VIGOR = (
    (1, 'Todas'),
    (2, 'Algunas'),
    (3, 'Ninguna'), )
CHOICE_ENTRADA_LUZ = (
    (1, 'Poda de copa'),
    (2, 'Quitar ramas entrecruzadas'),
    (3, 'Arreglar la sombra'),
)

CHOICES_FECHA_PODA = (('A', 'Enero'),
                      ('B', 'Febrero'),
                      ('C', 'Marzo'),
                      ('D', 'Abril'),
                      ('E', 'Mayo'),
                      ('F', 'Junio'),
                      ('G', 'Julio'),
                      ('H', 'Agosto'),
                      ('I', 'Septiembre'),
                      ('J', 'Octubre'),
                      ('K', 'Noviembre'),
                      ('L', 'Diciembre'),
                      )


class AnalisisPoda(models.Model):
    campo1 = MultiSelectField(choices=CHOICES_PROBLEMA_PLANTA, verbose_name='¿Cuáles son los problemas principales en cuanto a las estructuras de las plantas?')
    campo2 = MultiSelectField(choices=CHOICES_TIPO_PODA, verbose_name='¿Qué tipo de poda podemos aplicar para mejorar la estructura de las plantas?')
    campo3 = models.IntegerField(choices=CHOICE_REALIZA_PODA, verbose_name='¿Dónde se va a realizar la poda para mejorar la estructura de las plantas?')
    campo4 = models.IntegerField(choices=CHOICE_VIGOR, verbose_name='Las plantas tienen suficiente vigor, hojas y ramas para ser podadas?')
    campo5 = models.IntegerField(choices=CHOICE_ENTRADA_LUZ, verbose_name='¿Cómo podemos mejorar la entrada de luz en las plantas con la poda?')
    campo6 = MultiSelectField(choices=CHOICES_FECHA_PODA, verbose_name='¿Cuándo se van a realizar las podas?')

    ficha = models.ForeignKey(FichaPoda)

    def __unicode__(self):
        return 'Analisis'

    class Meta:
        verbose_name_plural = 'Análisis de poda y acciones'

class ManejoPoda(models.Model):
    herramientas = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Tiene herramienta para manejo de poda? ")
    formacion = models.IntegerField(
        choices=CHOICE_PODA,
        verbose_name="Tiene formación para manejo de poda? ")
    ficha = models.ForeignKey(FichaPoda)

    class Meta:
        verbose_name = "Herramienta y formación de poda"

# ---------------------------- fin de ficha poda ------------------------------

class FichaPlaga(models.Model):
    productor = models.ForeignKey(Persona,
            verbose_name='Nombre de productor o productora',
            related_name='persona_productor_plaga')
    tecnico = models.ForeignKey(Persona,
            verbose_name='Nombre de técnico',
            related_name='persona_tecnico_plaga')
    fecha_visita = models.DateField()

    def __unicode__(self):
        return self.productor.nombre

    class Meta:
        verbose_name = "Ficha plaga"
        verbose_name_plural = "Ficha plaga"


CHOICE_ENFERMEDADES_CACAOTALES = (
        (1, 'Monilia'),
        (2, 'Mazorca negra'),
        (3, 'Mal de machete'),
        (4, 'Mal de talluelo en el vivero'),
        (5, 'Barrenadores de tallo'),
        (6, 'Zompopos'),
        (7, 'Chupadores o áfidos'),
        (8, 'Escarabajos'),
        (9, 'Comején'),
        (10, 'Ardillas'),
        (10, 'Otros'),
    )

class PlagasEnfermedad(models.Model):
    plagas = models.IntegerField(choices=CHOICE_ENFERMEDADES_CACAOTALES,
                blank=True, null=True, verbose_name="Plagas y enfermedades")
    visto = models.IntegerField(choices=CHOICE_SI_NO,
                blank=True, null=True, verbose_name="He visto en mi cacaotal")
    dano = models.IntegerField(choices=CHOICE_SI_NO,
                            blank=True, null=True, verbose_name="Hace daño año con año")
    promedio = models.FloatField("¿Promedio nivel de daño en %?")

    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"PlagasEnfermedad"

CHOICE_ACCIONES_ENFERMEDADES = (
        (1, 'Recuento de plagas'),
        (2, 'Cortar las mazorcas enfermas'),
        (3, 'Abonar las plantas'),
        (4, 'Aplicar Caldos'),
        (5, 'Aplicar Fungicidas'),
        (6, 'Manejo de sombra'),
        (7, 'Podar las plantas de cacao'),
        (8, 'Aplicar venenos para Zompopo'),
        (9, 'Control de Comején'),
        (10, 'Ahuyar Ardillas'),
        (11, 'Otras'),
    )

class AccionesEnfermedad(models.Model):
    plagas_acciones = models.IntegerField(choices=CHOICE_ACCIONES_ENFERMEDADES,
                    blank=True, null=True, verbose_name="Manejo de Plagas y enfermedadess")
    realiza_manejo = models.IntegerField(choices=CHOICE_SI_NO,
                blank=True, null=True, verbose_name="Realiza en manejo")
    cuantas_veces = models.IntegerField(blank=True, null=True,
                verbose_name="Cuantas veces realizan el manejo")
    meses = MultiSelectField(choices=CHOICES_FECHA_PODA,
            verbose_name='En qué meses realizan el manejo')
    ficha = models.ForeignKey(FichaPlaga)


    def __unicode__(self):
        return u"AccionesEnfermedad"

    class Meta:
        verbose_name = "ACCIONES MANEJO DE PLAGAS Y ENFERMEDADE"

CHOICE_ORIENTACION = (
    ("A", 'Técnico'),
    ("B", 'Casa comercial'),
    ("C", 'Cooperativa'),
    ("D", 'Otros productores'),
    ("E", 'Experiencia propia/costumbres'),
    ("F", 'Otros medio de comunicación'),
)

class Orientacion(models.Model):
    fuentes = MultiSelectField(choices=CHOICE_ORIENTACION,
            verbose_name='3. Las fuentes de orientación para manejo de las plagas y enfermedades')
    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"Orientacion"


CHOICE_OBSERVACION_PUNTO1 = (
        (1, 'Monilia'),
        (2, 'Mazorca Negra'),
        (3, 'Mal de machete'),
        (4, 'Daño de ardilla'),
        (5, 'Daño de barrenador'),
        (6, 'Chupadores'),
        (7, 'Daño de zompopo'),
        (8, 'Bejuco'),
        (9, 'Tanda'),
        (10, 'Daño de comején'),
        (11, 'Daño de minador de la hoja'),
        (12, 'Daño por lana'),
        (13, 'Otros'),
    )

class ObservacionPunto1(models.Model):
    planta = models.IntegerField(choices=CHOICE_OBSERVACION_PUNTO1,
                                blank=True, null=True)
    uno = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)

    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"Punto1"

class ObservacionPunto1Nivel(models.Model):
    planta = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    ficha = models.ForeignKey(FichaPlaga)


    def __unicode__(self):
        return u"Punto1 nivel produccion"


class ObservacionPunto2(models.Model):
    planta = models.IntegerField(choices=CHOICE_OBSERVACION_PUNTO1,
                                blank=True, null=True)
    uno = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)

    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"Punto2"

class ObservacionPunto2Nivel(models.Model):
    planta = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)

    ficha = models.ForeignKey(FichaPlaga)


    def __unicode__(self):
        return u"Punto2 nivel produccion"

class ObservacionPunto3(models.Model):
    planta = models.IntegerField(choices=CHOICE_OBSERVACION_PUNTO1,
                                blank=True, null=True)
    uno = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_SI_NO, blank=True, null=True)

    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"Punto3"

class ObservacionPunto3Nivel(models.Model):
    planta = models.IntegerField(choices=CHOICE_PLANTAS3)
    uno = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dos = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    tres = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cuatro = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    cinco = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    seis = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    siete = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    ocho = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    nueve = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)
    dies = models.IntegerField(choices=CHOICE_PRODUCCION,
            blank=True, null=True)

    ficha = models.ForeignKey(FichaPlaga)


    def __unicode__(self):
        return u"Punto3 nivel produccion"

CHOICE_ENFERMEDADES = (
        ("A", 'Monilia'),
        ("B", 'Mazorca negra'),
        ("C", 'Mal de machete'),
        ("D", 'Mal de talluelo en el vivero'),
        ("E", 'Barrenadores de tallo'),
        ("F", 'Zompopos'),
        ("G", 'Chupadores o áfidos'),
        ("H", 'Escarabajos'),
        ("J", 'Comején'),
        ("K", 'Minador de la hoja'),
        ("L", 'Lana'),
        ("M", 'Ardillaa'),
        ("N", 'Bejuco'),
        ("O", 'Tanda'),
    )

CHOICE_SITUACION_PLAGAS = (
        (1, 'Varias plagas en todos los puntos'),
        (2, 'Varias plagas en algunos puntos'),
        (3, 'Pocas plagas en todos los puntos'),
        (4, 'Pocas plagas en algunos puntos'),
        (5, 'Una plaga en todos los puntos'),
        (6, 'Una plaga en algunos puntos'),
    )

class ProblemasPrincipales(models.Model):
    observadas = MultiSelectField(choices=CHOICE_ENFERMEDADES,
            verbose_name='Las plagas y enfermedades observadas en la parcela')
    situacion = models.IntegerField(choices=CHOICE_SITUACION_PLAGAS,blank=True, null=True)
    principales = MultiSelectField(choices=CHOICE_ENFERMEDADES,
            verbose_name='Las plagas y enfermedades principales en la parcela')
    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"problemas principales"


CHOICE_ENFERMEDADES_PUNTO6_1 = (
        ("A", 'Suelo erosionado'),
        ("B", 'Suelo poco fértil'),
        ("C", 'Mucha competencia'),
        ("D", 'Mal drenaje'),
        ("E", 'Falta obras de conservación'),
        ("F", 'Suelo compacto'),
        ("G", 'Suelo con poca MO'),
        ("H", 'No usa abono o fertilizante'),
    )

CHOICE_ENFERMEDADES_PUNTO6_2 = (
        (1, 'Sombra muy densa'),
        (2, 'Sombra muy rala'),
        (3, 'Sombra mal distribuida'),
        (4, 'Arboles de sombra no adecuada'),
        (5, 'Mucha auto-sombra'),
        (6, 'Mucho banano'),
    )

CHOICE_ENFERMEDADES_PUNTO6_3 = (
        ("A", 'Poda no adecuada'),
        ("B", 'Piso no manejado'),
        ("C", 'No eliminan mazorcas enfermas'),
        ("D", 'No hay manejo de plagas'),
        ("E", 'Plantas desnutridas'),
        ("F", 'Plantación vieja'),
        ("G", 'Variedades susceptibles'),
        ("H", 'Variedades no productivas'),
    )

class Punto6Plagas(models.Model):
    observaciones = MultiSelectField(choices=CHOICE_ENFERMEDADES_PUNTO6_1,
            verbose_name='Observaciones de suelo ')
    sombra = models.IntegerField(choices=CHOICE_ENFERMEDADES_PUNTO6_2,
            verbose_name="Observaciones de sombra", blank=True, null=True)
    manejo = MultiSelectField(choices=CHOICE_ENFERMEDADES_PUNTO6_3,
            verbose_name='Observaciones de manejo ')

    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"punto 6"


CHOICE_ACCIONES_PUNTO7_1 = (
        (1, 'Recuento de plagas'),
        (2, 'Cortar las mazorcas enfermas'),
        (3, 'Abonar las plantas'),
        (4, 'Aplicar Caldos'),
        (5, 'Aplicar Fungicidas'),
        (6, 'Manejo de sombra'),
        (7, 'Podar las plantas de cacao'),
        (8, 'Aplicar venenos para Zompopo'),
        (9, 'Control de Comején'),
    )

CHOICE_ACCIONES_PUNTO7_2 = (
        (1, 'Toda la parcela'),
        (2, 'Alguna parte de la parcela'),
    )

class Punto7Plagas(models.Model):
    manejo = models.IntegerField(choices=CHOICE_ACCIONES_PUNTO7_1,
            verbose_name="Manejo de plagas y enfermedades", blank=True, null=True)
    parte = models.IntegerField(choices=CHOICE_ACCIONES_PUNTO7_2,
            verbose_name="En que parte", blank=True, null=True)
    meses = MultiSelectField(choices=CHOICES_FECHA_PODA,
            verbose_name='En qué meses vamos a realizar el manejo')

    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"punto 7"

CHOICE_ENFERMEDADES_PUNTO8 = (
        ("A", 'Medial Luna'),
        ("B", 'Tijera'),
        ("C", 'Serrucho'),
        ("D", 'Bomba de mochila'),
        ("E", 'Barril'),
        ("F", 'Cutacha'),
        ("G", 'No tiene'),
        ("H", 'Coba'),
    )
class Punto8y9Plagas(models.Model):
    equipos = MultiSelectField(choices=CHOICE_ENFERMEDADES_PUNTO8,
            verbose_name='8.¿Tenemos los equipos necesarios para realizar manejo de plagas y enfermedades?')

    opcion = models.IntegerField(choices=CHOICE_SI_NO,
            verbose_name="9.¿Tenemos la formación para realizar el manejo de plagas y enfermedades?",
            blank=True, null=True)

    ficha = models.ForeignKey(FichaPlaga)

    def __unicode__(self):
        return u"punto 8 y 9"

#------------------------------ fin de ficha de plagas -------------------------------

class FichaPiso(models.Model):
    productor = models.ForeignKey(Persona,
            verbose_name='Nombre de productor o productora',
            related_name='persona_productor_piso')
    tecnico = models.ForeignKey(Persona,
            verbose_name='Nombre de técnico',
            related_name='persona_tecnico_piso')
    fecha_visita = models.DateField()

    def __unicode__(self):
        return self.productor.nombre

    class Meta:
        verbose_name = "Ficha piso"
        verbose_name_plural = "Fichas piso"

CHOICE_PISO1 = (
        ("A", 'Zacates o matas de hoja angosta'),
        ("B", 'Arbustos o plantas de hoja ancha'),
        ("C", 'Coyol o Coyolillo'),
        ("D", 'Bejucos'),
        ("E", 'Tanda'),
        ("F", 'Cobertura de hoja ancha'),
        ("G", 'Cobertura de hoja angosta'),
    )

class PisoPunto1(models.Model):
    punto1 = MultiSelectField(choices=CHOICE_PISO1,
            verbose_name='1.¿Cuáles son las hierbas qué cubren el piso y sube sobre las planta de cacao? ')
    punto2 = MultiSelectField(choices=CHOICE_PISO1,
            verbose_name='2.¿Cuáles son las hierbas qué usted considera dañino? ')

    ficha = models.ForeignKey(FichaPiso)

    def __unicode__(self):
        return u"piso 1 y 2"

CHOICE_PISO3 = (
        (1, 'Recuento de malezas'),
        (2, 'Chapoda tendida'),
        (3, 'Chapoda selectiva'),
        (4, 'Aplicar herbicidas total'),
        (5, 'Aplicar herbicidas en parches'),
        (6, 'Manejo de bejuco'),
        (7, 'Manejo de tanda'),
        (8, 'Regulación de sombra'),
    )

class PisoPunto3(models.Model):
    manejo = models.IntegerField(choices=CHOICE_PISO3,
            verbose_name="Manejo de piso",
            blank=True, null=True)
    realiza = models.IntegerField(choices=CHOICE_SI_NO,
            verbose_name="Realiza en manejo",
            blank=True, null=True)
    veces = models.FloatField("Cuantas veces realizan el manejo")
    meses = MultiSelectField(choices=CHOICES_FECHA_PODA,
            verbose_name='En qué meses vamos a realiza el manejo')

    ficha = models.ForeignKey(FichaPiso)

    def __unicode__(self):
        return u"punto 3"

CHOICE_PISO4 = (
        ("A", 'Técnico'),
        ("B", 'Casa comercial'),
        ("C", 'Cooperativa'),
        ("D", 'Otros productores'),
        ("E", 'Experiencia propia/costumbres'),
        ("F", 'Otros medio de comunicación'),
    )
class PisoPunto4(models.Model):
    manejo = MultiSelectField(choices=CHOICE_PISO4,
            verbose_name='4.¿De dónde viene su orientación de manejo de malas hierbas?')

    ficha = models.ForeignKey(FichaPiso)

    def __unicode__(self):
        return u"punto 4"

CHOICE_PISO5 = (
        (1, 'Zacate anual'),
        (2, 'Zacate perene'),
        (3, 'Hoja ancha anual'),
        (4, 'Hoja ancha perenne'),
        (5, 'Ciperácea o Coyolillo'),
        (6, 'Bejucos en suelo'),
        (7, 'Cobertura hoja ancha'),
        (8, 'Cobertura hoja angosta'),
        (9, 'Hojarasca'),
        (10, 'Mulch de maleza'),
        (11, 'Suelo desnudo')
    )

class PisoPunto5(models.Model):
    estado = models.IntegerField(choices=CHOICE_PISO5,
            verbose_name="Estado de Piso",
            blank=True, null=True)
    conteo = models.FloatField('Conteo (números)')

    ficha = models.ForeignKey(FichaPiso)

    def __unicode__(self):
        return u"punto 5"

CHOICE_PISO6_1 = (
        ("A", 'Sin competencia'),
        ("B", 'Media competencia'),
        ("C", 'Alta competencia'),
    )
CHOICE_PISO6_2 = (
        (1, 'Piso cubierto pero compite'),
        (2, 'Piso medio cubierto y compite'),
        (3, 'Piso no cubierto'),
        (4, 'Piso con mucho bejuco'),
        (5, 'Plantas con bejuco'),
        (6, 'Plantas con tanda'),
    )
CHOICE_PISO6_3 = (
        ("A", 'Zacate anual'),
        ("B", 'Zacate perene'),
        ("C", 'Hoja ancha anual'),
        ("D", 'Hoja ancha perenne'),
        ("E", 'Ciperácea o Coyolillo'),
        ("F", 'Bejucos'),
    )


class PisoPunto6(models.Model):
    manejo = MultiSelectField(choices=CHOICE_PISO6_1,
            verbose_name='La competencia entre malas hierbas y las plantas de cacao?')
    estado = models.IntegerField(choices=CHOICE_PISO6_2,
            verbose_name="La cobertura del piso de cacaotal",
            blank=True, null=True)
    maleza = MultiSelectField(choices=CHOICE_PISO6_3,
            verbose_name='Tipo de malezas que compiten')


    ficha = models.ForeignKey(FichaPiso)

    def __unicode__(self):
        return u"punto 6"

CHOICE_PISO7_1 = (
        ("A", 'Suelo erosionado'),
        ("B", 'Suelo poco fértil'),
        ("C", 'Mal drenaje'),
        ("D", 'Suelo compacto'),
        ("E", 'Suelo con poca MO'),
        ("F", 'No usa abono o fertilizante'),
    )

CHOICE_PISO7_2 = (
        ("A", 'Sombra muy rala'),
        ("B", 'Sombra mal distribuida'),
        ("C", 'Arboles de sombra no adecuada'),
        ("D", 'Poco banano'),
    )

CHOICE_PISO7_3 = (
        ("A", 'Chapoda no adecuada'),
        ("B", 'Chapoda tardía'),
        ("C", 'No hay manejo selectivo'),
        ("D", 'Plantas desnutridas'),
        ("E", 'Plantación vieja'),
        ("F", 'Mala selección de herbicidas'),
    )

class PisoPunto7(models.Model):
    suelo = MultiSelectField(choices=CHOICE_PISO7_1,
            verbose_name='Observaciones de suelo ')
    sombra = MultiSelectField(choices=CHOICE_PISO7_2,
            verbose_name='Observaciones de sombra')
    manejo = MultiSelectField(choices=CHOICE_PISO7_3,
            verbose_name='Observaciones de manejo')


    ficha = models.ForeignKey(FichaPiso)

    def __unicode__(self):
        return u"punto 7"

CHOICE_PISO8 = (
        (1, 'Recuento de malezas'),
        (2, 'Chapoda tendida'),
        (3, 'Chapoda selectiva'),
        (4, 'Aplicar herbicidas total'),
        (5, 'Aplicar herbicidas en parches'),
        (6, 'Manejo de bejuco'),
        (7, 'Manejo de tanda'),
        (8, 'Regulación de sombra'),
    )

class PisoPunto8(models.Model):
    piso = models.IntegerField(choices=CHOICE_PISO8,
            verbose_name="Manejo de piso",
            blank=True, null=True)
    parte = models.IntegerField(choices=CHOICE_ACCIONES_PUNTO7_2,
            verbose_name="En que parte",
            blank=True, null=True)
    meses = MultiSelectField(choices=CHOICES_FECHA_PODA,
            verbose_name='En qué meses vamos a realizar el manejo')


    ficha = models.ForeignKey(FichaPiso)

    def __unicode__(self):
        return u"punto 8"

CHOICE_PISO10 = (
        ("A", 'Machete'),
        ("B", 'Pico'),
        ("C", 'Pala'),
        ("D", 'Bomba de mochila'),
        ("E", 'Barril'),
        ("F", 'Cutacha'),
        ("G", 'No tiene'),
        ("H", 'Coba'),
    )

class PisoPunto10(models.Model):
    equipo = MultiSelectField(choices=CHOICE_PISO10,
            verbose_name='10.¿Tenemos los equipos necesarios para realizar manejo de piso?')
    formacion = models.IntegerField(choices=CHOICE_SI_NO,
            verbose_name="11.¿Tenemos la formación para realizar el manejo de piso?",
            blank=True, null=True)


    ficha = models.ForeignKey(FichaPiso)

    def __unicode__(self):
        return u"punto 10 y 11"

#-------------------------- entradas de suelo ----------------------------------

class FichaSuelo(models.Model):
    productor = models.ForeignKey(Persona,
            verbose_name='Nombre de productor o productora',
            related_name='persona_productor_suelo')
    tecnico = models.ForeignKey(Persona,
            verbose_name='Nombre de técnico',
            related_name='persona_tecnico_suelo')
    fecha_visita = models.DateField()

    def __unicode__(self):
        return self.productor.nombre

    class Meta:
        verbose_name = "Ficha suelo"
        verbose_name_plural = "Fichas suelos"


CHOICE_SUELO_USO_PARCELA = (
                            (1, 'Bosque'),
                            (2, 'Potrero'),
                            (3, 'Granos básicos'),
                            (4, 'Tacotal'),
                            (5, 'Cacaotal viejo'),
                            )
CHOICE_SUELO_LIMITANTES = (
                            ('A', 'Acidez / pH del suelo '),
                            ('B', 'Encharcamiento / Mal Drenaje'),
                            ('C', 'Enfermedades de raíces '),
                            ('D', 'Deficiencia de nutrientes'),
                            ('E', 'Baja materia orgánica'),
                            ('F', 'Baja actividad biológica y presencia de lombrices'),
                            ('G', 'Erosión'),
                            ('H', 'Compactación e infiltración de agua'),
                            )

CHOICE_SUELO_ORIENTACION = (
                            ('A', 'Técnico'),
                            ('B', 'Casa comercial'),
                            ('C', 'Cooperativa'),
                            ('D', 'Otros productores'),
                            ('E', 'Experiencia propia/costumbres'),
                            ('F', 'Otros medio de comunicación'),
                            ('G', 'Análisis de suelo '),
                            ('H', 'Otros '),
                            )

CHOICE_SUELO_ABONOS = (
                            ('A', 'Hecho en finca (compost, estiércol)'),
                            ('B', 'Regalados de otra finca (compost, estiércol)'),
                            ('C', 'Comprados de otra finca (compost, estiércol)'),
                            ('D', 'Comprado de casa comercial'),
                            ('E', 'Con crédito de la cooperativa'),
                            ('F', 'Incentivos/Regalados'),
                            ('G', 'No aplica'),
                            )

class Punto1Suelo(models.Model):
    uso_parcela = models.IntegerField(choices=CHOICE_SUELO_USO_PARCELA,
                  verbose_name="Cuál era el uso de la parcela antes de establecer el cacao?")
    limitante = MultiSelectField(choices=CHOICE_SUELO_LIMITANTES,
          verbose_name='Cuáles son los limitantes productivos del suelo de la parcela?')
    orientacion = MultiSelectField(choices=CHOICE_SUELO_ORIENTACION,
        verbose_name='Quien su orientación de manejo de fertilidad de suelo?')
    abonos = MultiSelectField(choices=CHOICE_SUELO_ABONOS,
        verbose_name='4. De donde consigue los abonos, fertilizantes y enmiendas de suelo?')

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Punto 1"
    class Meta:
        verbose_name = 'Historial de manejo y limitaciones observados'
        verbose_name_plural = 'Historial de manejo y limitaciones observados'

CHOICE_SUELO_EROSION_OPCION = (
                            (1, 'Deslizamientos'),
                            (2, 'Evidencia de erosión'),
                            (3, 'Cárcavas'),
                            (4, 'Área de acumulación de sedimentos'),
                            (5, 'Pedregosidad'),
                            (6, 'Raíces desnudos'),
                        )

CHOICE_SUELO_EROSION_RESPUESTA = (
                            (1, 'No presente'),
                            (2, 'Algo'),
                            (3, 'Severo'),
                        )

class PuntoASuelo(models.Model):
    opcion = models.IntegerField(choices=CHOICE_SUELO_EROSION_OPCION,
                  verbose_name="Indicadores")
    respuesta = models.IntegerField(choices=CHOICE_SUELO_EROSION_RESPUESTA,
                verbose_name="respuesta")

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Indicadores de erosión"

    class Meta:
        verbose_name = 'Indicadores de erosión'
        verbose_name_plural = 'Indicadores de erosión'

CHOICE_SUELO_CONSERVACION_OPCION = (
                            (1, 'Barrera muertas'),
                            (2, 'Barrera Viva'),
                            (3, 'Siembra en Curvas a Nivel'),
                            (4, 'Terrazas'),
                            (5, 'Cobertura de piso'),
                        )

CHOICE_SUELO_CONSERVACION_RESPUESTA = (
                            (1, 'No presente'),
                            (2, 'En mal estado'),
                            (3, 'En buen estado'),
                        )

class PuntoBSuelo(models.Model):
    opcion = models.IntegerField(choices=CHOICE_SUELO_CONSERVACION_OPCION,
                  verbose_name="Obras")
    respuesta = models.IntegerField(choices=CHOICE_SUELO_CONSERVACION_RESPUESTA,
                verbose_name="respuesta")

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Obras de conservación de suelo"

    class Meta:
        verbose_name = 'Obras de conservación de suelo'
        verbose_name_plural = 'Obras de conservación de suelo'


CHOICE_SUELO_DRENAJE_OPCION = (
                            (1, 'Encharcamientos'),
                            (2, 'Amarillamiento/mal crecimiento'),
                            (3, 'Enfermedades (phytophthora)'),
                        )

class Punto2ASuelo(models.Model):
    opcion = models.IntegerField(choices=CHOICE_SUELO_DRENAJE_OPCION,
                  verbose_name="Indicadores")
    respuesta = models.IntegerField(choices=CHOICE_SUELO_EROSION_RESPUESTA,
                verbose_name="respuesta")

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Indicadores de drenaje"

    class Meta:
        verbose_name = 'Indicadores de drenaje'
        verbose_name_plural = 'Indicadores de drenaje'

CHOICE_SUELO_DRENAJE_OPCION2 = (
                            (1, 'Acequias'),
                            (2, 'Canales de drenaje a lo largo y ancho de la parcela'),
                            (3, 'Canales de drenaje alrededor de las plantas'),
                            (4, 'Canales a lado de la parcela'),
                            (5, 'Cobertura de piso'),
                        )
class Punto2BSuelo(models.Model):
    opcion = models.IntegerField(choices=CHOICE_SUELO_DRENAJE_OPCION2,
                  verbose_name="Indicadores")
    respuesta = models.IntegerField(choices=CHOICE_SUELO_CONSERVACION_RESPUESTA,
                verbose_name="respuesta")

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Obras de drenaje"

    class Meta:
        verbose_name = 'Obras de drenaje'
        verbose_name_plural = 'Obras de drenaje'


CHOICE_SUELO_OPCION_PUNTOS = (
                            (1, 'Severidad de daño de nematodos'),
                            (2, 'Severidad de daño de hongos'),
                        )

CHOICE_SUELO_RESPUESTA_PUNTOS = (
                            (1, 'No Afectado'),
                            (2, 'Afectado'),
                            (3, 'Muy Afectados'),
                            (4, 'Severamente afectados'),
                        )


class Punto3SueloPunto1(models.Model):
    opcion = models.IntegerField(choices=CHOICE_SUELO_OPCION_PUNTOS,
                  verbose_name="Indicadores")
    respuesta = models.IntegerField(choices=CHOICE_SUELO_RESPUESTA_PUNTOS,
                verbose_name="respuesta")

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Punto 1"

    class Meta:
        verbose_name = 'Salud de Raíces punto 1'
        verbose_name_plural = 'Salud de Raíces punto 1'

class Punto3SueloPunto2(models.Model):
    opcion = models.IntegerField(choices=CHOICE_SUELO_OPCION_PUNTOS,
                  verbose_name="Indicadores")
    respuesta = models.IntegerField(choices=CHOICE_SUELO_RESPUESTA_PUNTOS,
                verbose_name="respuesta")

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Punto 2"

    class Meta:
        verbose_name = 'Salud de Raíces punto 2'
        verbose_name_plural = 'Salud de Raíces punto 2'

class Punto3SueloPunto3(models.Model):
    opcion = models.IntegerField(choices=CHOICE_SUELO_OPCION_PUNTOS,
                  verbose_name="Indicadores")
    respuesta = models.IntegerField(choices=CHOICE_SUELO_RESPUESTA_PUNTOS,
                verbose_name="respuesta")

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Punto 3"

    class Meta:
        verbose_name = 'Salud de Raíces punto 3'
        verbose_name_plural = 'Salud de Raíces punto 3'


class Punto4Suelo(models.Model):
    area = models.FloatField(verbose_name='Tamaño de Área de Cacao SAF (en manzanas)')
    densidad = models.FloatField(verbose_name='Densidad de Arboles de Cacao en parcela SAF (por manzana)')

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Balance de nutrientes de parcela Cacao SAF"

    class Meta:
        verbose_name = 'Balance de nutrientes de parcela Cacao SAF'
        verbose_name_plural = 'Balance de nutrientes de parcela Cacao SAF'


CHOICE_SUELO_PRODUCTO_COSECHA = (
                            (1, 'Cacao Grano Seco - (qq/mz/año)'),
                            (2, 'Leña - (cargas de 125lb /mz/año)'),
                            (3, 'Cabezas de Banano - (cabezas/mz/año)'),
                        )

class Punto4SueloCosecha(models.Model):
    producto = models.IntegerField(choices=CHOICE_SUELO_PRODUCTO_COSECHA)
    cantidad = models.FloatField()

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Cosechas del Productos SAF"

    class Meta:
        verbose_name = 'Cosechas del Productos SAF'
        verbose_name_plural = 'Cosechas del Productos SAF'



class Punto4SueloSI(models.Model):
    opcion = models.IntegerField(choices=CHOICE_SI_NO)

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Se regresa la cascara a la parcela como abono?"

    class Meta:
        verbose_name = 'Se regresa la cascara a la parcela como abono?'
        verbose_name_plural = 'Se regresa la cascara a la parcela como abono?'


class TipoFertilizantes(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return u'%s' % (self.nombre)

CHOICE_UNIDAD_MEDIDA_ABONO = ((1,'lb/mz'),(2,'lb/planta '),(3,'oz/planta'),(4,'L/mz'),(5, 'qq/mz'))

class Punto5SueloAbonos(models.Model):
    tipo = models.ForeignKey(TipoFertilizantes)
    cantidad = models.FloatField('Cantidad(Valor)')
    unidad = models.IntegerField(choices=CHOICE_UNIDAD_MEDIDA_ABONO)
    humedad = models.FloatField('Humedad (%)')
    frecuencia = models.FloatField('Frecuencia (por año)')
    meses = MultiSelectField(choices=CHOICES_FECHA_PODA, verbose_name='Meses de aplicación')

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Abonos, fertilizantes y Enmiendas aplicadas en la parcela cacao SAF"

    class Meta:
        verbose_name = 'Abonos, fertilizantes y Enmiendas aplicadas en la parcela cacao SAF'
        verbose_name_plural = 'Abonos, fertilizantes y Enmiendas aplicadas en la parcela cacao SAF'


class DatosAnalisis(models.Model):
    variable = models.CharField(max_length=250)
    unidad = models.CharField(max_length=250)
    valor_critico = models.FloatField()

    def __unicode__(self):
        return self.variable


class Punto6AnalisisSuelo(models.Model):
    variable = models.ForeignKey(DatosAnalisis)
    valor = models.FloatField()

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Datos de análisis de suelo"

    class Meta:
        verbose_name = 'Datos de análisis de suelo'
        verbose_name_plural = 'Datos de análisis de suelo'


class Punto7TipoSuelo(models.Model):
    opcion = models.IntegerField(choices=(
                                        (1,'Ultisol (rojo)'),
                                        (2, 'Andisol (volcánico)'),
                                        (3, 'Vertisol'),))

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Tipo de suelo"

    class Meta:
        verbose_name = 'Tipo de suelo'
        verbose_name_plural = 'Tipo de suelo'


class Punto8SueloPropuesta(models.Model):
    tipo = models.ForeignKey(TipoFertilizantes)
    cantidad = models.FloatField('Cantidad(Valor)')
    unidad = models.IntegerField(choices=CHOICE_UNIDAD_MEDIDA_ABONO)
    frecuencia = models.FloatField('Frecuencia (por año)')
    meses = MultiSelectField(choices=CHOICES_FECHA_PODA, verbose_name='Meses de aplicación')

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Nueva Propuesta de Fertilización Generada"

    class Meta:
        verbose_name = 'Nueva Propuesta de Fertilización Generada'
        verbose_name_plural = 'Nueva Propuesta de Fertilización Generada'

CHOICE_PUNTO9_LIMITACION_1 = (
                                (1, 'Erosión de Suelo'),
                            )

CHOICE_PUNTO9_LIMITACION_1_ACCION = (
                                ('A', 'Barrera viva'),
                                ('B', 'Cobertura de suelo'),
                                ('C', 'Barrera Muerta'),
                                ('D', 'Siembra en Curvas a Nivel'),
                                ('E', 'Terrazas'),
                            )

CHOICE_PUNTO9_LIMITACION_2 = (
                                (1, 'Mal drenaje y encharamientos'),
                            )
CHOICE_PUNTO9_LIMITACION_2_ACCION = (
                                ('A', 'Acequias'),
                                ('B', 'Canales de drenaje de larga'),
                                ('C', 'Canales de drenaje alrededor de la parcela'),
                            )

CHOICE_PUNTO9_LIMITACION_3 = (
                                (1, 'Deficiencia de Nutrientes'),
                            )
CHOICE_PUNTO9_LIMITACION_3_ACCION = (
                                ('A', 'Aplicar abonos orgánicos'),
                                ('B', 'Aplicar abonos minerales'),
                            )

CHOICE_PUNTO9_LIMITACION_4 = (
                                (1, 'Exceso de nutrientes'),
                            )
CHOICE_PUNTO9_LIMITACION_4_ACCION = (
                                ('A', 'Bajar nivel de fertilización'),
                            )

CHOICE_PUNTO9_LIMITACION_5 = (
                                (1, 'Desbalance de nutrientes'),
                            )
CHOICE_PUNTO9_LIMITACION_5_ACCION = (
                                ('A', 'Ajustar programa de fertilización '),
                            )
CHOICE_PUNTO9_LIMITACION_6 = (
                                (1, 'Enfermedades y plagas de raíces'),
                            )
CHOICE_PUNTO9_LIMITACION_6_ACCION = (
                                ('A', 'Abonos orgánicos'),
                                ('B', 'Obras de drenaje'),
                                ('C', 'Aplicación de ceniza'),
                            )

CHOICE_PUNTO9_DONDE = (
                                (1, 'En todo parcela'),
                                (2, 'En algunas partes'),
                            )


class Punto9Erosion(models.Model):
    limitaciones = models.IntegerField(choices=CHOICE_PUNTO9_LIMITACION_1)
    acciones = MultiSelectField(choices=CHOICE_PUNTO9_LIMITACION_1_ACCION, verbose_name='Acciones potenciales')
    donde = models.IntegerField(choices=CHOICE_PUNTO9_DONDE)

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Toma de decisión con base en las observaciones de eroción"

    class Meta:
        verbose_name = 'Erosión de Suelo'
        verbose_name_plural = 'Erosión de Suelo'

class Punto9Drenaje(models.Model):
    limitaciones = models.IntegerField(choices=CHOICE_PUNTO9_LIMITACION_2)
    acciones = MultiSelectField(choices=CHOICE_PUNTO9_LIMITACION_2_ACCION, verbose_name='Acciones potenciales')
    donde = models.IntegerField(choices=CHOICE_PUNTO9_DONDE)

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Toma de decisión con base en las observaciones de mal drenaje"

    class Meta:
        verbose_name = 'Mal drenaje y encharamientos'
        verbose_name_plural = 'Mal drenaje y encharamientos'


class Punto9Nutrientes(models.Model):
    limitaciones = models.IntegerField(choices=CHOICE_PUNTO9_LIMITACION_3)
    acciones = MultiSelectField(choices=CHOICE_PUNTO9_LIMITACION_3_ACCION, verbose_name='Acciones potenciales')
    donde = models.IntegerField(choices=CHOICE_PUNTO9_DONDE)

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Toma de decisión con base en las observaciones de deficiencia nutrientes"

    class Meta:
        verbose_name = 'Deficiencia de Nutrientes'
        verbose_name_plural = 'Deficiencia de Nutrientes'

class Punto9Exceso(models.Model):
    limitaciones = models.IntegerField(choices=CHOICE_PUNTO9_LIMITACION_4)
    acciones = MultiSelectField(choices=CHOICE_PUNTO9_LIMITACION_4_ACCION, verbose_name='Acciones potenciales')
    donde = models.IntegerField(choices=CHOICE_PUNTO9_DONDE)

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Toma de decisión con base en las observaciones de exceso de nutrientes"

    class Meta:
        verbose_name = 'Exceso de nutrientes'
        verbose_name_plural = 'Exceso de nutrientes'

class Punto9Desbalance(models.Model):
    limitaciones = models.IntegerField(choices=CHOICE_PUNTO9_LIMITACION_5)
    acciones = MultiSelectField(choices=CHOICE_PUNTO9_LIMITACION_5_ACCION, verbose_name='Acciones potenciales')
    donde = models.IntegerField(choices=CHOICE_PUNTO9_DONDE)

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Toma de decisión con base en las observaciones de desbalance de nutrientes"

    class Meta:
        verbose_name = 'Desbalance de nutrientes'
        verbose_name_plural = 'Desbalance de nutrientes'

class Punto9Enfermedades(models.Model):
    limitaciones = models.IntegerField(choices=CHOICE_PUNTO9_LIMITACION_6)
    acciones = MultiSelectField(choices=CHOICE_PUNTO9_LIMITACION_6_ACCION, verbose_name='Acciones potenciales')
    donde = models.IntegerField(choices=CHOICE_PUNTO9_DONDE)

    ficha = models.ForeignKey(FichaSuelo)

    def __unicode__(self):
        return u"Toma de decisión con base en las observaciones de enfermedades y plagas"

    class Meta:
        verbose_name = 'Enfermedades y plagas de raíces'
        verbose_name_plural = 'Enfermedades y plagas de raíces'

#------------ fin ficha suelo ---------------------------------
#-------------------- comienza ficha viviero ------------------

class FichaVivero(models.Model):
    productor = models.ForeignKey(Persona,
            verbose_name='Nombre de productor o productora',
            related_name='persona_productor_vivero')
    tecnico = models.ForeignKey(Persona,
            verbose_name='Nombre de técnico',
            related_name='persona_tecnico_vivero')
    fecha_visita = models.DateField()

    def __unicode__(self):
        return self.productor.nombre

    class Meta:
        verbose_name = "Ficha vivero"
        verbose_name_plural = "Fichas viveros"


CHOICE_VIVERO_CONVERSACION_1 = (
                                ('A', 'Enero'),
                                ('B', 'Febrero'),
                                ('C', 'Marzo'),
                                ('D', 'Abril'),
                                ('E', 'Mayo'),
                                ('F', 'Junio'),
                                ('G', 'Julio'),
                                ('H', 'Agosto'),
                                ('I', 'Septiembre'),
                                ('J', 'Octubre'),
                                ('K', 'Noviembre'),
                                ('L', 'Diciembre'),
                            )

CHOICE_VIVERO_CONVERSACION_2 = (
                                ('A', 'En este momento hay buena semilla'),
                                ('B', 'En este momento hay suficiente agua'),
                                ('C', 'En este momento hay menos plagas'),
                                ('D', 'Nos permite para tener plantas listas para sembrar en el invierno'),
                            )

CHOICE_VIVERO_CONVERSACION_3 = (
                                ('A', 'Buena altura'),
                                ('B', 'Tallo fuerte'),
                                ('C', 'Buena formación horqueta'),
                                ('D', 'Ramas principales robustas'),
                                ('E', 'Buena producción de frutos (más de 40 frutos por planta)'),
                                ('F', 'Alta tolerancia a plagas y enfermedades'),
                                ('G', 'Más de 40 almendras dentro de la mazorca'),
                            )

CHOICE_VIVERO_CONVERSACION_4 = (
                                ('A', 'Corte de mazorca madura'),
                                ('B', 'Extracción de almendras'),
                                ('C', 'Selección de almendras de mayor tamaño'),
                                ('D', 'Remoción de mucilago o baba'),
                                ('E', 'Empaque en bolsas plásticas con aserrín semi-húmedo'),
                                ('F', 'Toma en cuenta fases de la luna'),
                            )

CHOICE_VIVERO_CONVERSACION_5 = (
                                ('A', 'Soleando la tierra'),
                                ('B', 'Aplicando agua caliente'),
                                ('C', 'Aplicando cal o ceniza'),
                                ('D', 'Aplicando venenos'),
                                ('E', 'No desinfecta'),
                            )

CHOICE_VIVERO_CONVERSACION_6 = (
                                (1, 'Sola tierra'),
                                (2, 'Tierra + Arena'),
                                (3, 'Tierra + Abono orgánico (compost)'),
                                (4, 'Tierra + abono orgánico + Cal o ceniza'),
                                (5, 'Tierra + Arena + Cal o Ceniza + Abono orgánico'),
                            )

CHOICE_VIVERO_CONVERSACION_7 = (
                                (1, 'Bolsa de 6 X 8 pulgadas '),
                                (2, 'Bolsa de 8 X 10 pulgadas'),
                                (3, 'Bolsa de 8 X 10 pulgadas'),
                            )

CHOICE_VIVERO_CONVERSACION_8 = (
                                (1, 'Acostado u horizontal'),
                                (2, 'Parado o Vertical'),
                                (3, 'De cualquier manera'),
                            )

CHOICE_VIVERO_CONVERSACION_9 = (
                                ('A', 'Cerca de fuentes de agua'),
                                ('B', 'Cercado protegido de animales'),
                                ('C', 'Terreno plano'),
                                ('D', 'Con buena orientación de los bancos (Este-Oeste)'),
                                ('E', 'Con sombra natural'),
                                ('F', 'Con ramada'),
                            )

CHOICE_VIVERO_CONVERSACION_10 = (
                                (1, 'Injerto de yema'),
                                (2, 'Injerto de cogollo'),
                                (3, 'Ninguno'),
                            )

CHOICE_VIVERO_CONVERSACION_12 = (
                                (1, 'De la misma finca'),
                                (2, 'De finca vecina'),
                                (3, 'De Jardín Clonal'),
                            )

class VivieroConversacion(models.Model):
    conversacion1 = MultiSelectField(choices=CHOICE_VIVERO_CONVERSACION_1,
                                verbose_name='1.¿En qué meses del año planifica o construye viveros para producción de plantas de cacao?')
    conversacion2 = MultiSelectField(choices=CHOICE_VIVERO_CONVERSACION_2,
                                verbose_name='2.¿Por qué hace vivero en estos meses?')
    conversacion3 = MultiSelectField(choices=CHOICE_VIVERO_CONVERSACION_3,
                                verbose_name='3.¿Cuáles son características más deseables para una planta productiva?')
    conversacion4 = MultiSelectField(choices=CHOICE_VIVERO_CONVERSACION_4,
                                verbose_name='4.¿Qué pasos realiza para la preparación de semillas de cacao?')
    conversacion5 = MultiSelectField(choices=CHOICE_VIVERO_CONVERSACION_5,
                                verbose_name='5.¿Con qué desinfecta el suelo para el vivero?')
    conversacion6 = models.IntegerField(choices=CHOICE_VIVERO_CONVERSACION_6,
                                        verbose_name='¿Cómo prepara el sustrato para la producción de plantas de cacao en vivero?')

    ficha = models.ForeignKey(FichaVivero)

    def __unicode__(self):
        return u"Conversación con el Productor o productora"

    # class Meta:
    #     verbose_name = 'I.Conversación con el Productor o productora'
    #     verbose_name_plural = 'I.Conversación con el Productor o productora'

class ViveroConversacion2(models.Model):
    conversacion7 = models.IntegerField(choices=CHOICE_VIVERO_CONVERSACION_7,
                                        verbose_name='¿Qué tamaño de bolsa de polietileno utiliza para la producción de plantas en vivero?')
    conversacion8 = models.IntegerField(choices=CHOICE_VIVERO_CONVERSACION_8,
                                        verbose_name='¿Cómo coloca la semilla en el sustrato en la bolsa de polietileno?')
    conversacion9 = MultiSelectField(choices=CHOICE_VIVERO_CONVERSACION_9,
                                verbose_name='¿Cómo es el sitio del vivero?')
    conversacion10 = MultiSelectField(choices=CHOICE_VIVERO_CONVERSACION_10,
                                verbose_name=' ¿Qué tipo de injerto ha realizado?')
    conversacion11 = models.FloatField('¿Cuál ha sido el porcentaje de prendimiento?', null=True)
    conversacion12 = MultiSelectField(choices=CHOICE_VIVERO_CONVERSACION_12,
                                verbose_name='¿De dónde obtiene las varetas para realizar los injertos?')

    ficha = models.ForeignKey(FichaVivero)

    def __unicode__(self):
        return u"Conversación con el Productor o productora 2"

#observaciones
CHOICER_VIVIERO_FUENTE_SEMILLA = ((1,'De la misma finca'),(2,'De finca vecina'),(3,'De Jardín Clonal'))

class VivieroObservacion1(models.Model):
    observacion1 = models.FloatField('Cantidad de las plantas')
    observacion2 = models.FloatField('Edad de las plantas en meses')
    observacion3 = models.IntegerField(choices=CHOICER_VIVIERO_FUENTE_SEMILLA,
                                        verbose_name='Fuente de semilla')

    ficha = models.ForeignKey(FichaVivero)

    def __unicode__(self):
        return u"Observación del vivero 1"

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''


CHOICE_VIVERO_PLAGAS_ENFERMEDADES = (
                                (1, 'Zompopo'),
                                (2, 'Barrenador'),
                                (3, 'Minador'),
                                (4, 'Tizón'),
                                (5, 'Antracnosis'),
                                (6, 'Mal de talluelo'),
                                (7, 'Áfidos'),
                                (8, 'Gusanos'),
                                (9, 'Deficiencia nutricional'),
                            )
CHOICE_VIVERO_SI_NO = (
                                (1, 'Si'),
                                (2, 'No'),
                            )

class VivieroObservacion2(models.Model):
    observacion3 = models.IntegerField(choices=CHOICE_VIVERO_PLAGAS_ENFERMEDADES,
                                        verbose_name='Plaga o enfermedad')
    planta_1 = models.IntegerField(choices=CHOICE_VIVERO_SI_NO)
    planta_2 = models.IntegerField(choices=CHOICE_VIVERO_SI_NO)
    planta_3 = models.IntegerField(choices=CHOICE_VIVERO_SI_NO)
    planta_4 = models.IntegerField(choices=CHOICE_VIVERO_SI_NO)
    planta_5 = models.IntegerField(choices=CHOICE_VIVERO_SI_NO)
    planta_6 = models.IntegerField(choices=CHOICE_VIVERO_SI_NO)
    planta_7 = models.IntegerField(choices=CHOICE_VIVERO_SI_NO)
    planta_8 = models.IntegerField(choices=CHOICE_VIVERO_SI_NO)
    planta_9 = models.IntegerField(choices=CHOICE_VIVERO_SI_NO)
    planta_10 = models.IntegerField(choices=CHOICE_VIVERO_SI_NO)

    ficha = models.ForeignKey(FichaVivero)

    def __unicode__(self):
        return u"Observación del vivero 2"

    # class Meta:
    #     verbose_name = 'Presencia de plagas y enfermedades'
    #     verbose_name_plural = 'Presencia de plagas y enfermedades'

class ProductosVivero(models.Model):
    nombre = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nombre

    # class Meta:
    #     verbose_name = 'Productos para el vivero'
    #     verbose_name_plural = 'Productos para el vivero'

CHOICE_VIVERO_UNIDAD_PRODUCTOS = ((1,'Onz/planta'),(2,'Lt/bombada'),)

class VivieroObservacionProductos(models.Model):
    producto = models.ForeignKey(ProductosVivero, verbose_name='Nombre')
    cantidad = models.FloatField()
    unidad = models.IntegerField(choices=CHOICE_VIVERO_UNIDAD_PRODUCTOS)
    frecuencia = models.FloatField()

    ficha = models.ForeignKey(FichaVivero)

    def __unicode__(self):
        return u"Observación del vivero 3"

CHOICE_VIVERO_ANALISIS_1 = (
                                ('A', 'Ningún problema'),
                                ('B', 'Proveniente de plantas con baja productividad'),
                                ('C', 'Posiblemente con alta incompatibilidad'),
                            )

CHOICE_VIVERO_ANALISIS_2 = (
                                ('A', 'Ningún problema'),
                                ('B', 'Planta desuniforme'),
                                ('C', 'Plantas con poco vigor'),
                                ('D', 'Plantas con deficiencia nutricionales'),
                                ('E', 'Mal manejo de riego'),
                                ('F', 'Mal manejo de sombra'),
                            )

CHOICE_VIVERO_ANALISIS_3 = (
                                ('A', 'Zompopo'),
                                ('B', 'Barrenador'),
                                ('C', 'Minador'),
                                ('D', 'Tizón'),
                                ('E', 'Antracnosis'),
                                ('F', 'Mal de talluelo'),
                                ('G', 'Áfidos'),
                                ('H', 'Gusanos'),
                            )

CHOICE_VIVERO_ANALISIS_4 = (
                                ('A', 'Mejorar la fuente de semilla'),
                                ('B', 'Mezclar las 9 fuentes de semilla'),
                                ('C', 'Mejorar el sustrato en las bolsas'),
                                ('D', 'Mejorar el manejo de plagas'),
                                ('E', 'Mejorar el manejo de nutrición'),
                                ('F', 'Mejorar el riego y sombra'),
                            )

class VivieroAnalisisSituacion(models.Model):
    analisis1 = MultiSelectField(choices=CHOICE_VIVERO_ANALISIS_1,
                                verbose_name='¿Cuáles son los problemas de la semilla?')
    analisis2 = MultiSelectField(choices=CHOICE_VIVERO_ANALISIS_2,
                                verbose_name='¿Cuáles son los problemas las plantas?')
    analisis3 = MultiSelectField(choices=CHOICE_VIVERO_ANALISIS_3,
                                verbose_name='¿Cuáles son los problemas de plagas y enfermedades?')
    analisis4 = MultiSelectField(choices=CHOICE_VIVERO_ANALISIS_4,
                                verbose_name='¿Qué acciones vamos a realizar para mejorar el vivero?')

    ficha = models.ForeignKey(FichaVivero)

    def __unicode__(self):
        return u"Análisis de la situación y acciones en el vivero"
