from django.conf.urls import *
from .views import *

urlpatterns = patterns('guias_cacao.views',
    url(r'^$', 'index_ficha_sombra', name='index-cacao'),
    url(r'^sombra/riqueza/$', 'riqueza_sombra', name='riqueza-cacao'),
    url(r'^sombra/analisis/$', 'analisis_sombra', name='analisis-cacao'),
    url(r'^sombra/cobertura/$', 'cobertura_sombra', name='cobertura-cacao'),
    url(r'^sombra/densidad/$', 'densidad_sombra', name='densidad-cacao'),
    url(r'^sombra/acciones/$', 'acciones_sombra', name='acciones-cacao'),
    url(r'^sombra/caracterizacion/$', 'caracterizacion_sombra', name='caracterizacion-cacao'),
    url(r'^sombra/dominancia/$', 'dominancia_sombra', name='dominancia-cacao'),
    url(r'^sombra/dimensiones/$', 'dimensiones_sombra', name='dimensiones-cacao'),

    #urls de poda
    url(r'^poda/altura/$', 'altura_poda', name='altura-poda'),
    url(r'^poda/ancho-copa/$', 'ancho_poda', name='ancho-poda'),
    url(r'^poda/produccion/$', 'produccion_poda', name='produccion-poda'),
    url(r'^poda/atributos/$', 'atributos_poda', name='produccion-poda'),
    url(r'^poda/analisis/$', 'analisis_poda', name='analisis-poda'),
    url(r'^poda/tipos-poda/$', 'tipo_poda', name='tipo-poda'),
    url(r'^poda/acciones/$', 'acciones_poda', name='acciones-poda'),

    #urls de plaga
    url(r'^plaga/historial/$', 'historial_plaga', name='historial-plaga'),
    url(r'^plaga/acciones/$', 'acciones_plaga', name='acciones-plaga'),
    url(r'^plaga/fuente-incidencia/$', 'fuente_incidencia_plaga', name='fuente-incidencia-plaga'),
    url(r'^plaga/produccion/$', 'produccion_rendimiento_plaga', name='produccion-rendimiento-plaga'),
    url(r'^plaga/analisis/$', 'analisis_plaga', name='analisis-plaga'),
    url(r'^plaga/suelo/$', 'observacion_sombra_poda_plaga', name='observacion-sombra-poda-plaga'),
    url(r'^plaga/acciones-manejo/$', 'acciones_manejo_plaga', name='acciones-manejo-plaga'),
    url(r'^plaga/equipos-formacion/$', 'equipos_formacion_plaga', name='equipos-formacion-plaga'),

    #urls de piso
    url(r'^piso/estado/$', 'estado_piso', name='estado-piso'),
    url(r'^piso/manejo/$', 'estado_piso2', name='estado-piso-2'),
    url(r'^piso/orientacion/$', 'orientacion_composicion_piso', name='orientacion-composicion-piso'),
    url(r'^piso/analisis/$', 'analisis_piso', name='analisis-piso'),
    url(r'^piso/suelo/$', 'suelo_piso', name='suelo-piso'),
    url(r'^piso/propuesta/$', 'propuesta_piso', name='propuesta-piso'),
    url(r'^piso/equipo-formacion/$', 'equipo_piso', name='equipo-piso'),

    #urls cosecha
    url(r'^cosecha/conversaciones/$', 'conversacion_cosecha', name='conversacion-cosecha'),
    url(r'^cosecha/mazorcas-sanas/$', 'datos_sanos_cosecha', name='datos-sanos-cosecha'),
    url(r'^cosecha/mazorcas-enfermas/$', 'datos_enfermas_cosecha', name='datos-enfermas-cosecha'),
    url(r'^cosecha/mazorcas-danadas/$', 'datos_danadas_cosecha', name='datos-danadas-cosecha'),
    url(r'^cosecha/analisis/$', 'analisis_cosecha', name='analisis-cosecha'),

    #urls cierre
    url(r'^cierre/sombra/$', 'sombra_cierre', name='sombra-cierre'),
    url(r'^cierre/poda/$', 'poda_cierre', name='poda-cierre'),
    url(r'^cierre/suelo/$', 'suelo_cierre', name='suelo-cierre'),
    url(r'^cierre/plaga/$', 'plaga_cierre', name='plaga-cierre'),
    url(r'^cierre/piso/$', 'piso_cierre', name='piso-cierre'),
    url(r'^cierre/vivero/$', 'vivero_cierre', name='vivero-cierre'),
    url(r'^cierre/cosecha/$', 'cosecha_cierre', name='cosecha-cierre'),
    url(r'^cierre/ciclo-trabajo/$', 'ciclo_trabajo_cierre', name='ciclo-trabajo-cierre'),
    url(r'^cierre/costos/$', 'calculos_costo_cierre', name='calculos-costo-cierre'),
    url(r'^cierre/tablas/$', 'tablas_cierre', name='tablas-cierre'),

    #urls saf
    url(r'^saf/objetivos/$', 'objetivos_saf', name='objetivos-saf'),
    url(r'^saf/clima/$', 'clima_saf', name='clima-saf'),
    url(r'^saf/condiciones/$', 'condiciones_saf', name='condiciones-saf'),
    url(r'^saf/sombra/$', 'sombra_saf', name='sombra-saf'),
    url(r'^saf/semilla/$', 'semilla_saf', name='semilla-saf'),
    url(r'^saf/calidad/$', 'calidad_saf', name='calidad-saf'),
    url(r'^saf/disenio-saf/$', 'disenio_saf_saf', name='disenio-saf'),

    #urls vivero
    url(r'^vivero/conversaciones/$', 'conversaciones_vivero', name='conservaciones-vivero'),
    url(r'^vivero/conversaciones-dos/$', 'conversaciones_dos_vivero', name='conservaciones-dos-vivero'),
    url(r'^vivero/observacion/$', 'observacion_vivero', name='observacion-vivero'),
    url(r'^vivero/analisis/$', 'analisis_vivero', name='analisis-vivero'),

    url(r'^api/productor/$', 'get_productor', name='productor-cacao'),
)
