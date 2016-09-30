# -*- coding: utf-8 -*-
from selectable.base import ModelLookup
from selectable.registry import registry
from .models import *

class ProductorLookup(ModelLookup):
    model = Persona
    search_fields = ('nombre__icontains', )
    filters = {'tipo_persona': 1, 'productor__proyecto__corto' : 'Herramienta granos básicos' }

class MonitoreoLookup(ModelLookup):
    model = Monitoreo
    search_fields = ('productor__nombre__icontains', )

registry.register(ProductorLookup)
registry.register(MonitoreoLookup)
