# -*- coding: utf-8 -*-
from django import forms
from lookups import ProductorLookup, TecnicoLookup
import selectable.forms as selectable
from .models import FichaSombra, FichaPoda, FichaPlaga, FichaPiso, FichaSuelo, FichaVivero, FichaCosecha, FichaSaf, FichaCierre
from mapeo.models import Persona, Organizaciones
from comunicacion.lugar.models import Pais, Departamento, Municipio, Comunidad

class ProductorSombraAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaSombra
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

class TecnicoAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaSombra
        widgets = {
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }


class ProductorPodaAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaPoda
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

class ProductorPlagaAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaPlaga
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }


class ProductorPisoAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaPiso
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

class ProductorSueloAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaSuelo
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

class ProductorViveroAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaVivero
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

class ProductorCosechaAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaCosecha
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

class ProductorSafAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaSaf
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

class ProductorCierreAdminForm(forms.ModelForm):

    class Meta(object):
        model = FichaCierre
        widgets = {
            'productor': selectable.AutoCompleteSelectWidget(lookup_class=ProductorLookup),
            'tecnico': selectable.AutoCompleteSelectWidget(lookup_class=TecnicoLookup),
        }

def fecha_choice():
    years = []
    for en in FichaSombra.objects.order_by('fecha_visita').values_list('fecha_visita', flat=True):
        years.append((en.year,en.year))
    for en in FichaPoda.objects.order_by('fecha_visita').values_list('fecha_visita', flat=True):
        years.append((en.year,en.year))
    for en in FichaPlaga.objects.order_by('fecha_visita').values_list('fecha_visita', flat=True):
        years.append((en.year,en.year))
    for en in FichaPiso.objects.order_by('fecha_visita').values_list('fecha_visita', flat=True):
        years.append((en.year,en.year))
    for en in FichaCosecha.objects.order_by('fecha_visita').values_list('fecha_visita', flat=True):
        years.append((en.year,en.year))
    for en in FichaCierre.objects.order_by('fecha_visita').values_list('fecha_visita', flat=True):
        years.append((en.year,en.year))
    for en in FichaSaf.objects.order_by('fecha_visita').values_list('fecha_visita', flat=True):
        years.append((en.year,en.year))
    for en in FichaVivero.objects.order_by('fecha_visita').values_list('fecha_visita', flat=True):
        years.append((en.year,en.year))
    return list(sorted(set(years)))

CHOICE_SEXO1 = (
    ('', '-------'),
    (1, 'Hombre'),
    (2, 'Mujer')
)

CHOICE_TIPOLOGIA1 = (('', '-------------------'),
                    (1, 'Pequeño campesino de montaña'),
                    (2, 'Pequeño campesino diversificado'),
                    (3, 'Finquero cacaotero'),
                    (4, 'Finquero ganadero cacaotero'),
                    (5, 'Finquero cafetalero'),
                    (6, 'Finquero ganadero cafetalero'),
                    (7, 'Finquero ganadero'),
                )

class ConsultaSombraForm(forms.Form):
    fecha = forms.ChoiceField(choices=fecha_choice(), label="Años", required=True)
    productor = forms.CharField(max_length=250, required=False)
    organizacion = forms.ModelChoiceField(queryset=Organizaciones.objects.all(), required=False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=False)
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required=False)
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), required=False)
    comunidad = forms.ModelChoiceField(queryset=Comunidad.objects.all(), required=False)
    sexo = forms.ChoiceField(choices=CHOICE_SEXO1, required=False)
    tipologia = forms.ChoiceField(choices=CHOICE_TIPOLOGIA1, required=False)
