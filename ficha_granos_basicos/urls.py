from django.conf.urls import *
from .views import *

urlpatterns = patterns('ficha_granos_basicos.views',
    url(r'^$', 'consulta', name='index-granos-basicos'),

    url(r'^productores/genero-y-produccion/$', 'genero_produccion', name='genero-y-produccion'),
    url(r'^productores/composicion-familiar/$', 'composicion_familiar', name='composicion-familiar'),

    url(r'^monitoreo/georeferencia/$', 'georeferencia', name='georeferencia'),
    url(r'^monitoreo/caracteristicas-parcela/$', 'caracteristicas_parcela', name='caracteristicas-parcela'),
    url(r'^monitoreo/ciclo-productivo/$', 'ciclo_productivo', name='ciclo-productivo'),
    url(r'^monitoreo/uso-suelo/$', 'uso_suelo', name='uso-suelo'),
    url(r'^monitoreo/recursos-economicos/$', 'recursos_economicos', name='recursos-economicos'),
    url(r'^monitoreo/rendimiento/$', 'rendimiento', name='rendimiento'),

    url(r'^ajax/comunies/$', 'get_comunies', name='get-comunies'),
)
