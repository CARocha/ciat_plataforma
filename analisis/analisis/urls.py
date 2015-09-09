from django.conf.urls import *

urlpatterns = patterns('analisis.analisis.views',
    #######################################################
    url(r'^inicio/$', 'indexnuevo', name='indexnuevo'),
    url(r'^consulta/$', 'consulta', name='consulta'),
    #######################################################
	url(r'^$', 'inicio', name="inicio"),
    #url(r'^salidas/$', 'post', name='salidas'),
    url(r'^organizaciones/$', 'salida1', name='organizaciones'),
    url(r'^proyectos-por-sector/$', 'salida2', name='proyectos-por-sector'),
    url(r'^proyectos-por-tema/$', 'salida3', name='proyectos-por-tema'),
    url(r'^impactos-por-sector/$', 'salida4', name='impactos-por-sector'),
    url(r'^impactos-por-tema/$', 'salida5', name='impactos-por-tema'),
    url(r'^impactos-por-beneficiarios/$', 'salida5b', name='impactos-por-beneficiarios'),
    url(r'^innovaciones-por-sector/$', 'salida6', name='innovaciones-por-sector'),
    url(r'^innovaciones-por-tema/$', 'salida7', name='innovaciones-por-tema'),
    url(r'^temas-por-sector/$', 'salida13', name='temas-por-sector'),
    url(r'^aliados-roles/$', 'salida8', name='aliados-roles'),
    url(r'^sectores-aliados/$', 'salida9', name='sectores-aliados'),
    url(r'^relaciones-sectores/$', 'salida10', name='relaciones-sectores'),
    #url(r'^salida11/$', 'salida11', name='salida11'),
    #url(r'^salida12/$', 'salida12', name='salida12'),
    url(r'^innovaciones-futuras-por-sector/$', 'salida14', name='innovaciones-por-futuras-sector'),
    url(r'^innovaciones-futuras-por-tema/$', 'salida15', name='innovaciones-por-futuras-tema'),
    url(r'^socio-potenciales-por-sector/$', 'salida16', name='socio-potenciales-por-sector'),
    url(r'^socios-tiempo/$', 'salida17', name='socios-tiempo'),
    url(r'^fuentes-aprendizaje/$', 'salida18', name='fuentes-aprendizaje'),
    url(r'^informacion-necesaria/$', 'salida19', name='informacion-necesaria'),
    url(r'^limitaciones/$', 'salida20', name='limitaciones'),

    url(r'^ajax/fechas/$', 'get_fecha', name='get_fecha'),
    url(r'^ajax/sitioaccion/$', 'get_sitio_accion', name='get_sitio_accion'),
    url(r'^ajax/plataforma/$', 'get_plataforma', name='get_plataforma'),
    url(r'^mapa/$', 'obtener_lista', name='obtener-lista'),
    )