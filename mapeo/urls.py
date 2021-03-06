from django.conf.urls import *
from .views import *

urlpatterns = patterns('mapeo.views',
    url(r'^$', 'indexview', name='index-mapeo'),
    url(r'^proyectos/$', 'proyectos', name='proyectos'),
    url(r'^proyecto/mapa/(?P<id_proyecto>\d+)/$', 'mapa_actores', name='mapa-proyecto'),
    url(r'^jsonmapa/(?P<id_proyecto>\d+)/$', 'obtener_mapa', name='obtener-mapa'),
    url(r'^timelinejson/(?P<id_proyecto>\d+)/$', 'timelinejson', name='timelinejson'),
)

