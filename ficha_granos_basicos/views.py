# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *
from .forms import *
from comunicacion.lugar.models import *
from mapeo.models import *
from django.http import HttpResponse
from django.db.models import Sum, Count, Avg
import collections
import numpy as np

# Create your views here.
def _queryset_filtrado(request):
	params = {}

	if request.session['year']:
		params['annio'] = request.session['year']

	if request.session['municipio']:
			params['productor__comunidad__municipio__in'] = request.session['municipio']
	else:
		if request.session['comunidad']:
			params['productor__comunidad__in'] = request.session['comunidad']

	if request.session['ciclo']:
		params['ciclo_productivo'] = request.session['ciclo']

	if request.session['rubro']:
		params['cultivo'] = request.session['rubro']

	if request.session['organizacion']:
		params['productor__productor__organizacion'] = request.session['organizacion']

	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)

	for key in unvalid_keys:
		del params[key]

	return Monitoreo.objects.filter(**params)

def consulta(request,template="granos_basicos/consulta.html"):
	if request.method == 'POST':
		mensaje = None
		form = Consulta(request.POST)
		if form.is_valid():
			request.session['year'] = form.cleaned_data['year']
			request.session['municipio'] = form.cleaned_data['municipio']
			request.session['comunidad'] = form.cleaned_data['comunidad']
			request.session['ciclo'] = form.cleaned_data['ciclo']
			request.session['rubro'] = form.cleaned_data['rubro']
			request.session['organizacion'] = form.cleaned_data['organizacion']

			mensaje = "Todas las variables estan correctamente :)"
			request.session['activo'] = True
			centinela = 1


		else:
			centinela = 0

	else:
		form = Consulta()
		mensaje = "Existen alguno errores"
		centinela = 0
		try:
			del request.session['year']
			del request.session['municipio']
			del request.session['comunidad']
			del request.session['ciclo']
			del request.session['rubro']
			del request.session['organizacion']
		except:
			pass

	return render(request, template, locals())

def genero_produccion(request,template="granos_basicos/productores/genero_produccion.html"):
	filtro = _queryset_filtrado(request)
	productores = filtro.distinct('productor').count()

	CHOICE_SEXO = ((1,'Hombre'),(2,'Mujer'))

	choice = ((1,'Hombre'),(2,'Mujer'),(3,'Compartida'))
	sexo_productor = {}
	for obj in choice:
		conteo = filtro.filter(productor__productor__jefe = obj[0]).distinct('productor').count()
		sexo_productor[obj[1]] = conteo

	if request.GET.get('jefe'):
		jefe = request.GET['jefe']
		if jefe == '1':
			CHOICE_SEXO_JEFE = ((1,'Hombre'),)
		elif jefe == '2':
			CHOICE_SEXO_JEFE = ((2,'Mujer'),)
		elif jefe == '3':
			CHOICE_SEXO_JEFE = ((3,'Compartida'),)
	else:
		CHOICE_SEXO_JEFE = ((1,'Hombre'),(2,'Mujer'),(3,'Compartida'))

	RELACION_CHOICES = ((1,'Jefe/Jefa de familia'),(2,'Cónyuge'),
	    				(3,'Hijo/Hija'),(4,'Otro familiar'),
	    				(5,'Administrador'),)

	prod_gb = {}
	prod = {}
	dic_relacion = {}
	for obj in CHOICE_SEXO_JEFE:
		for x in CHOICE_SEXO:
			#relacion entre responsables de familia
			jefe_familia = filtro.filter(productor__sexo = x[0],productor__productor__jefe = obj[0]).distinct('productor').count()
			prod[x[1]] = jefe_familia

		for relacion in RELACION_CHOICES:
			conteo = filtro.filter(productor__productorgranosbasicos__relacion = relacion[0],productor__productor__jefe = obj[0]).distinct('productor').count()
			dic_relacion[relacion[1]] = conteo

	for x in CHOICE_SEXO:
		conteo = filtro.filter(productor__sexo = x[0]).distinct('productor').count()
		prod_gb[x[1]] = conteo

	return render(request, template, locals())

def composicion_familiar(request,template="granos_basicos/productores/composicion_familiar.html"):
	filtro = _queryset_filtrado(request)
	productores = filtro.distinct('productor').count()

	#nuevas salidas
	lista_hijos = []
	lista_hijas = []
	lista_sumatoria = []
	for obj in filtro:
		hijos = ComposicionFamiliar.objects.filter(persona = obj.productor,familia = '3').count()
		lista_hijos.append(hijos)

		hijas = ComposicionFamiliar.objects.filter(persona = obj.productor,familia = '4').count()
		lista_hijas.append(hijas)

		sumatoria = hijos + hijas
		lista_sumatoria.append(sumatoria)

	result = []
	#promedio,mediana,desviacion standard, minimo y maximo
	promedios = [np.mean(lista_hijos),np.mean(lista_hijas),np.mean(lista_sumatoria)]
	mediana = [np.median(lista_hijos),np.median(lista_hijas),np.median(lista_sumatoria)]
	desviacion = [np.std(lista_hijos),np.std(lista_hijas),np.std(lista_sumatoria)]
	minimo = [min(lista_hijos),min(lista_hijas),min(lista_sumatoria)]
	maximo = [max(lista_hijos),max(lista_hijas),max(lista_sumatoria)]
	# agregando a la lista
	result.append(promedios)
	result.append(mediana)
	result.append(desviacion)
	result.append(minimo)
	result.append(maximo)

	#grafico nivel educativo de los padres en las familias
	ESCOLARIDAD_CHOICES = (
		(1,'Ninguno'),(2,'Primaria Incompleta'),(3,'Primaria'),
		(4,'Secundaria Incompleta'),(5,'Secundaria'),(6,'Técnico'),
		(7,'Universitario'),(8,'Profesional'))

	escolaridad = collections.OrderedDict()
	for obj in ESCOLARIDAD_CHOICES:
		madre = filtro.filter(productor__composicionfamiliar__familia = '2',
		                    productor__composicionfamiliar__escolaridad = obj[0]).distinct('productor__composicionfamiliar').count()
		padre = filtro.filter(productor__composicionfamiliar__familia = '1',
		                    productor__composicionfamiliar__escolaridad = obj[0]).distinct('productor__composicionfamiliar').count()

		#hijos--------------------
		hijos_5_12 = filtro.filter(productor__composicionfamiliar__familia = '3',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (5,12)).distinct('productor__composicionfamiliar').count()

		hijos_13_18 = filtro.filter(productor__composicionfamiliar__familia = '3',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (13,18)).distinct('productor__composicionfamiliar').count()

		hijos_19 = filtro.filter(productor__composicionfamiliar__familia = '3',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (19,100)).distinct('productor__composicionfamiliar').count()

		#hijas--------------------
		hijas_5_12 = filtro.filter(productor__composicionfamiliar__familia = '4',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (5,12)).distinct('productor__composicionfamiliar').count()

		hijas_13_18 = filtro.filter(productor__composicionfamiliar__familia = '4',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (13,18)).distinct('productor__composicionfamiliar').count()

		hijas_19 = filtro.filter(productor__composicionfamiliar__familia = '4',
									productor__composicionfamiliar__escolaridad = obj[0],
									productor__composicionfamiliar__edad__range = (19,100)).distinct('productor__composicionfamiliar').count()


		escolaridad[obj[1]] = (madre,padre,
								hijos_5_12,hijos_13_18,hijos_19,
								hijas_5_12,hijas_13_18,hijas_19)
	#--------------------------------------------------------------------------------

	SI_NO_CHOICES = ((1,'Si'),(2,'No'))
	FAMILIA_CHOICES = ((1,'Padre'),(2,'Madre'),(3,'Hijo'),(4,'Hija'),(5,'Hermano'),
	    				(6,'Hermana'),(7,'Sobrino'),(8,'Sobrina'),(9,'Abuelo'),
	    				(10,'Abuela'),(11,'Cuñado'),(12,'Cuñada'),(13,'Yerno'),
						(14,'Nuera'),(15,'Otro'),)

	list_participacion = []

	for obj in FAMILIA_CHOICES:
		total = filtro.filter(productor__composicionfamiliar__familia = obj[0]).distinct(
									'productor__composicionfamiliar').count()

		si_participa = filtro.filter(productor__composicionfamiliar__familia = obj[0],
									productor__composicionfamiliar__participacion = '1').distinct(
									'productor__composicionfamiliar').count()

		promedio = total / float(productores)
		promedio = round(promedio, 2)

		list_participacion.append((obj[1],saca_porcentajes(si_participa,total,False),promedio))

	return render(request, template, locals())

def georeferencia(request,template="granos_basicos/monitoreos/georeferencia.html"):
	filtro = _queryset_filtrado(request)
	productores = filtro.distinct('productor').count()

	mapa = filtro.values('nombre_parcela','latitud','longitud')

	return render(request, template, locals())

def caracteristicas_parcela(request,template="granos_basicos/monitoreos/caracteristicas_parcela.html"):
	filtro = _queryset_filtrado(request)
	productores = filtro.distinct('productor').count()

	lista_parcela = []
	lista_inclinado = []
	lista_plano = []

	#edad parcela y profundidad capa arable
	parcela = filtro.values_list('edad_parcela','profundidad_capa')
	for obj in parcela:
		lista_parcela.append(parcela)

	#edad de las parcelas
	menor_5 = filtro.filter(edad_parcela__range = (0,5)).count()
	edad_6_20 = filtro.filter(edad_parcela__range = (5.1,20)).count()
	mayor_20 = filtro.filter(edad_parcela__range = (20.1,100)).count()

	for obj in filtro:
		# % area inclinado > 60%
		area = DistribucionPendiente.objects.filter(monitoreo = obj,seleccion = '1').values_list('inclinado',flat = True)
		for x in area:
			if x >= 60:
				inclinado = DistribucionPendiente.objects.filter(monitoreo = obj,seleccion = '2').values_list('inclinado','monitoreo__profundidad_capa')
				lista_inclinado.append(inclinado)

		# % area plano > 60%
		area1 = DistribucionPendiente.objects.filter(monitoreo = obj,seleccion = '1').values_list('plano',flat = True)
		for y in area1:
			if y >= 60:
				plano = DistribucionPendiente.objects.filter(monitoreo = obj,seleccion = '2').values_list('plano','monitoreo__profundidad_capa')
				lista_plano.append(plano)

	#acceso agua
	SI_NO_CHOICES = ((1,'Si'),(2,'No'))

	acceso_agua = {}
	conteo_si = 0
	for obj in SI_NO_CHOICES:
		conteo = filtro.filter(acceso_agua = obj[0]).count()
		acceso_agua[obj[1]] = conteo

	#fuente agua
	fuente_agua = {}
	conteo_si = filtro.filter(acceso_agua = 1).count()
	for obj in ACCESO_AGUA_CHOICES:
		conteo = filtro.filter(fuente_agua__icontains = obj[0]).count()
		fuente_agua[obj[1]] = saca_porcentajes(conteo,conteo_si,False)

	return render(request, template, locals())

def ciclo_productivo(request,template="granos_basicos/monitoreos/ciclo_productivo.html"):
	filtro = _queryset_filtrado(request)
	productores = filtro.distinct('productor').count()

	#siembra
	fecha_siembra = filtro.values_list('datosmonitoreo__fecha_siembra',flat = True)
	lista_siembra = []
	for obj in fecha_siembra:
		if obj != None:
			x = obj.isocalendar()[1]
			lista_siembra.append(x)
	l_siembra = sorted(lista_siembra)

	dic_siembra = collections.OrderedDict()
	for v in l_siembra:
		count = l_siembra.count(v)
		dic_siembra[v] = count

	#cosecha
	fecha_cosecha = filtro.values_list('datosmonitoreo__fecha_cosecha',flat = True)
	lista_cosecha = []
	for obj in fecha_cosecha:
		if obj != None:
			x = obj.isocalendar()[1]
			lista_cosecha.append(x)
	l_cosecha = sorted(lista_cosecha)

	dic_cosecha = collections.OrderedDict()
	for v in l_cosecha:
		count = l_cosecha.count(v)
		dic_cosecha[v] = count

	return render(request, template, locals())

def uso_suelo(request,template="granos_basicos/monitoreos/uso_suelo.html"):
	filtro = _queryset_filtrado(request)
	productores = filtro.distinct('productor').count()

	USO_SUELO_CHOICES = ((1,'Área Total'),(2,'Cultivos Anuales (GB)'),(3,'Cultivos perennes'),
	    (4,'Tacotales'),(5,'Potreros'),(6,'Pasto de Corte'))

	total = filtro.filter(productor__usosuelo__uso = '1').aggregate(total = Sum('productor__usosuelo__cantidad'))['total']
	uso_suelo = collections.OrderedDict()
	for obj in USO_SUELO_CHOICES:
		#tabla 1
		familias = filtro.filter(productor__usosuelo__uso = obj[0]).count()
		mz = filtro.filter(productor__usosuelo__uso = obj[0]).aggregate(total = Sum('productor__usosuelo__cantidad'))['total']
		porcentaje = saca_porcentajes(mz,total,False)
		try:
			promedio = mz / float(familias)
		except:
			promedio = 0

		uso_suelo[obj[1]] = (familias,mz,porcentaje,promedio)

	#tabla 2
	tamano_finca = filtro.filter(productor__usosuelo__uso = '1').values_list('productor__usosuelo__cantidad',flat = True)
	granos_basicos = filtro.filter(productor__usosuelo__uso = '2').values_list('productor__usosuelo__cantidad',flat = True)
	area_siembra = filtro.values_list('datosmonitoreo__area_siembra',flat = True)

	result = []
	#promedio,mediana,desviacion standard, minimo y maximo
	promedios = [np.mean(tamano_finca),np.mean(granos_basicos),np.mean(area_siembra)]
	mediana = [np.median(tamano_finca),np.median(granos_basicos),np.median(area_siembra)]
	desviacion = [np.std(tamano_finca),np.std(granos_basicos),np.std(area_siembra)]
	minimo = [min(tamano_finca),min(granos_basicos),min(area_siembra)]
	maximo = [max(tamano_finca),max(granos_basicos),max(area_siembra)]
	# agregando a la lista
	result.append(promedios)
	result.append(mediana)
	result.append(desviacion)
	result.append(minimo)
	result.append(maximo)

	#distribucion area de siembra
	menor_1 = filtro.filter(datosmonitoreo__area_siembra__range = (0,0.99)).count()
	entre_1_2 = filtro.filter(datosmonitoreo__area_siembra__range = (1,2)).count()
	entre_2_3 = filtro.filter(datosmonitoreo__area_siembra__range = (2.1,3)).count()
	entre_3_4 = filtro.filter(datosmonitoreo__area_siembra__range = (3.1,4)).count()
	entre_4_5 = filtro.filter(datosmonitoreo__area_siembra__range = (4.1,5)).count()

	#promedio area de siembra
	area_siembra = filtro.values_list('datosmonitoreo__area_siembra',flat = True)
	promedio_area = np.mean(area_siembra)
	desviacion_area = np.std(area_siembra)
	mediana_area = np.median(area_siembra)
	minimo_area = min(area_siembra)
	maximo_area = max(area_siembra)

	return render(request, template, locals())

def recursos_economicos(request,template="granos_basicos/monitoreos/recursos_economicos.html"):
	filtro = _queryset_filtrado(request)
	productores = filtro.distinct('productor').count()

	dic = {}
	for obj in RESPUESTA_CHOICES:
		conteo = filtro.filter(recursossiembra__respuesta = obj[0]).count()
		dic[obj[1]] = conteo

	return render(request, template, locals())

def rendimiento(request,template="granos_basicos/monitoreos/rendimiento.html"):
	filtro = _queryset_filtrado(request)
	productores = filtro.distinct('productor').count()

	ANIO_CHOICES = ((2014,'2014'),(2015,'2015'),(2016,'2016'),(2017,'2017'),
	    			(2018,'2018'),(2019,'2019'),(2020,'2020'),)

	#maiz
	rend_maiz = collections.OrderedDict()
	for obj in ANIO_CHOICES:
		primera_maiz = HistorialRendimiento.objects.filter(ciclo_productivo = '1',rubro = '1',
														anio = obj[1]).aggregate(avg = Avg('rendimiento'))['avg']

		postrera_maiz = HistorialRendimiento.objects.filter(ciclo_productivo = '2',rubro = '1',
														anio = obj[1]).aggregate(avg = Avg('rendimiento'))['avg']

		apante_maiz = HistorialRendimiento.objects.filter(ciclo_productivo = '3',rubro = '1',
														anio = obj[1]).aggregate(avg = Avg('rendimiento'))['avg']

		if primera_maiz != None or postrera_maiz != None or apante_maiz != None:
			rend_maiz[obj[1]] = (primera_maiz,postrera_maiz,apante_maiz)

	#frijol
	rend_frijol = collections.OrderedDict()
	for obj in ANIO_CHOICES:
		primera_frijol = HistorialRendimiento.objects.filter(ciclo_productivo = '1',rubro = '2',
														anio = obj[1]).aggregate(avg = Avg('rendimiento'))['avg']

		postrera_frijol = HistorialRendimiento.objects.filter(ciclo_productivo = '2',rubro = '3',
														anio = obj[1]).aggregate(avg = Avg('rendimiento'))['avg']

		apante_frijol = HistorialRendimiento.objects.filter(ciclo_productivo = '3',rubro = '4',
														anio = obj[1]).aggregate(avg = Avg('rendimiento'))['avg']

		if primera_frijol != None or postrera_frijol != None or apante_frijol != None:
			rend_frijol[obj[1]] = (primera_frijol,postrera_frijol,apante_frijol)

	return render(request, template, locals())

def get_comunies(request):
	ids = request.GET.get('ids', '')
	results = []
	dicc = {}
	if ids:
		lista = ids.split(',')

		for id in lista:
			monitoreos = Monitoreo.objects.filter(productor__municipio__id = id).distinct().values_list('productor__comunidad__id', flat=True)
			municipios = Municipio.objects.get(pk = id)
			comunies = Comunidad.objects.filter(municipio__id = municipios.pk,id__in = monitoreos).order_by('nombre')
			lista1 = []
			for c in comunies:
				comu = {}
				comu['id'] = c.id
				comu['nombre'] = c.nombre
				lista1.append(comu)
				dicc[municipios.nombre] = lista1

	return HttpResponse(simplejson.dumps(dicc), content_type = 'application/json')

def saca_porcentajes(dato, total, formato=True):
	if dato != None:
		try:
			porcentaje = (dato/float(total)) * 100 if total != None or total != 0 else 0
		except:
			return 0
		if formato:
			return porcentaje
		else:
			return '%.2f' % porcentaje
	else:
		return 0
