# -*- coding: utf-8 -*-
from django import forms
from lookups import *
import selectable.forms as selectable
from .models import *

class MonitoreoAdminForm(forms.ModelForm):

    class Meta(object):
        model = Monitoreo
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
        }

class VisitasAdminForm(forms.ModelForm):

    class Meta(object):
        model = Visitas
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=VisitaLookup),
        }

class ProductorMonitoreoAdminForm(forms.ModelForm):

    class Meta(object):
        model = Gastos
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=MonitoreoLookup),
        }
