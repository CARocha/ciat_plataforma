# -*- coding: UTF-8 -*-
from django.forms import ModelForm
from models import *
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from comunicacion.contrapartes.widgets import ColorPickerWidget
from mapeo.models import Organizaciones
from analisis.configuracion.models import AreaAccion, SitioAccion, Plataforma

class ContraparteForms(forms.ModelForm):
    temas = forms.CharField(widget=CKEditorWidget())
    siglas = forms.CharField(widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Siglas o nombre corto"}))
    generalidades = forms.CharField(widget=CKEditorWidget())
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'span7','rel':"tooltip", 'title':"Nombre completo de la contraparte"}))
    fundacion = forms.CharField(widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Año en que fue fundada la organización"}))
    contacto = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Nombre completo de la persona de contacto"}))
    telefono = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Formato ### - ######## "}))
    sitio_web = forms.URLField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Con este formato http://www.dominio.com "}))
    rss = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Dirección rss de contenido sindicado"}))
    font_color = forms.CharField(required=False, widget=ColorPickerWidget, label="Color")
    area_accion = forms.ModelChoiceField(queryset=AreaAccion.objects.all())
    sitio_accion = forms.ModelChoiceField(queryset=SitioAccion.objects.all())
    plataforma= forms.ModelChoiceField(queryset=Plataforma.objects.all())


    class Meta:
        model = Organizaciones
        exclude = ('user',)

class UserForm(ModelForm):
    class Meta:
	model = User
	fields = ('username', 'first_name', 'last_name', 'email')

class UserProfileForm(ModelForm):
    class Meta:
	model = UserProfile
	fields = ('avatar',)

class MensajeForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(queryset = User.objects.order_by('username'),
                                          widget = forms.CheckboxSelectMultiple())
    class Meta:
        #widgets = {'user': forms.CheckboxSelectMultiple}
    	model = Mensajero
        exclude = ('usuario','fecha')
