# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ConsultaSombraForm
from .models import *
from mapeo.models import Persona
import json as simplejson
from itertools import chain
from django.db.models import Avg, Sum, F
import numpy as np
from collections import OrderedDict, Counter
from django.db.models import Q
# Create your views here.

def _queryset_filtrado_sombra(request):
    params = {}

    if 'fecha' in request.session:
        params['fecha_visita__year'] = request.session['fecha']

    if 'productor' in request.session:
        params['productor__nombre'] = request.session['productor']

    if 'organizacion' in request.session:
        params['productor__productor__organizacion'] = request.session['organizacion']

    if 'pais' in request.session:
        params['productor__pais'] = request.session['pais']

    if 'departamento' in request.session:
        params['productor__departamento'] = request.session['departamento']

    if 'municipio' in request.session:
        params['productor__municipio'] = request.session['municipio']

    if 'comunidad' in request.session:
        params['productor__comunidad'] = request.session['comunidad']

    if 'sexo' in request.session:
        params['productor__sexo'] = request.session['sexo']

    if 'tipologia' in request.session:
        params['productor__productor__tipologia'] = request.session['tipologia']

    unvalid_keys = []
    for key in params:
    	if not params[key]:
    		unvalid_keys.append(key)

    for key in unvalid_keys:
    	del params[key]

    return FichaSombra.objects.filter(**params)



def index_ficha_sombra(request, template='guiascacao/index.html'):
    if request.method == 'POST':
        form = ConsultaSombraForm(request.POST)
        if form.is_valid():
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['productor'] = form.cleaned_data['productor']
            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['pais'] = form.cleaned_data['pais']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['municipio'] = form.cleaned_data['municipio']
            request.session['comunidad'] = form.cleaned_data['comunidad']
            request.session['sexo'] = form.cleaned_data['sexo']
            request.session['tipologia'] = form.cleaned_data['tipologia']
            centinela = 1
        else:
            centinela = 0
    else:
        form = ConsultaSombraForm()
        centinela = 0

        if 'fecha' in request.session:
            try:
                del request.session['fecha']
                del request.session['productor']
                del request.session['organizacion']
                del request.session['pais']
                del request.session['departamento']
                del request.session['municipio']
                del request.session['comunidad']
                del request.session['sexo']
                del request.session['tipologia']
            except:
                pass

    return render(request, template, {'form': form, 'centinela': centinela})


#---------------- salidas sombra -----------------------------

def analisis_sombra(request, template="guiascacao/sombra/analisis_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    CHOICE_DENSIDAD = ( (1,'Alta'),
                        (2,'Adecuada'),
                        (3,'Baja'),
                      )

    CHOICE_COPA = ((1,'Ancha'),
                   (2,'Adecuada'),
                   (3,'Angosta'),
                )

    CHOICE_ARREGLO = ((1, 'Uniforme'), (2, 'Desuniforme'))
    CHOICE_HOJARASCA = ((1, 'Suficiente'), (2, 'No Suficiente'))
    CHOICE_HOJARASCA_CALIDAD = ((1, 'Rico en nutrientes'), (2, 'Pobre en nutriente'))
    CHOICE_COMPETENCIA = ((1, 'Fuerte'), (2, 'Mediana'), (3, 'Leve'))
    CHOICE_PROBLEMA = (
                        (1,'Cobertura'),
                        (2,'Mal arreglo'),
                        (3,'Competencia'),
                        (4,'Densidad Tipo de árboles'),
                        (5,'Ninguno')
                    )

    dict_densidad = {}
    for densidad in CHOICE_DENSIDAD:
        conteo = filtro.filter(analisissombra__densidad=densidad[0]).count()
        dict_densidad[densidad[1]] = conteo

    dict_copa = {}
    for copa in CHOICE_COPA:
        conteo = filtro.filter(analisissombra__forma_copa=copa[0]).count()
        dict_copa[copa[1]] = conteo

    dict_arreglo = {}
    for arreglo in CHOICE_ARREGLO:
        conteo = filtro.filter(analisissombra__arreglo=arreglo[0]).count()
        dict_arreglo[arreglo[1]] = conteo

    dict_hojarasca = {}
    for hoja in CHOICE_HOJARASCA:
        conteo = filtro.filter(analisissombra__hojarasca=hoja[0]).count()
        dict_hojarasca[hoja[1]] = conteo

    dict_calidad_hojarasca = {}
    for hoja in CHOICE_HOJARASCA_CALIDAD:
        conteo = filtro.filter(analisissombra__calidad_hojarasca=hoja[0]).count()
        dict_calidad_hojarasca[hoja[1]] = conteo

    dict_competencia = {}
    for obj in CHOICE_COMPETENCIA:
        conteo = filtro.filter(analisissombra__competencia=obj[0]).count()
        dict_competencia[obj[1]] = conteo

    dict_problema = {}
    for obj in CHOICE_PROBLEMA:
        conteo = filtro.filter(analisissombra__Problema=obj[0]).count()
        dict_problema[obj[1]] = conteo


    return render(request, template, locals())


def cobertura_sombra(request, template="guiascacao/sombra/cobertura_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)
    numero_parcelas = filtro.count()

    punto1 = Cobertura1.objects.filter(ficha__in=filtro).values_list('cobertura', flat=True)
    punto2 = Cobertura2.objects.filter(ficha__in=filtro).values_list('cobertura', flat=True)
    punto3 = Cobertura3.objects.filter(ficha__in=filtro).values_list('cobertura', flat=True)

    l = list(chain(punto1, punto2, punto3))

    #promedio_todo_puntos = reduce(lambda x, y: x + y, l) / len(l)

    # media arítmetica
    promedio2 = np.mean(l)
    # mediana
    mediana2 = np.median(l)
    # Desviación típica
    desviacion2 = np.std(l)
    #minimo y maximo
    minimo2 = min(l)
    maximo2 = max(l)
    #TODO

    grafo_cobertura = crear_rangos(request, l, minimo2, maximo2, step=10)

    return render(request, template, locals())

def riqueza_sombra(request, template="guiascacao/sombra/sombra_riqueza.html"):
    filtro = _queryset_filtrado_sombra(request)
    numero_parcelas = filtro.count()

    puntos = []
    for obj in filtro:
        cnt1 = Punto1.objects.filter(ficha=obj).values_list('especie__id', flat=True)
        cnt2 = Punto2.objects.filter(ficha=obj).values_list('especie__id', flat=True)
        cnt3 = Punto3.objects.filter(ficha=obj).values_list('especie__id', flat=True)
        lista = list(cnt1) + list(cnt2) + list(cnt3)

        reducida_lista = list(set(lista))
        formula_riqueza = len(reducida_lista) #(len(reducida_lista) * 1000) / float(1890)
        puntos.append(formula_riqueza)

    # media arítmetica
    promedio2 = np.mean(puntos)
    # mediana
    mediana2 = np.median(puntos)
    # Desviación típica
    desviacion2 = np.std(puntos)
    #minimo
    minimo = min(puntos)
    #maximo
    maximo = max(puntos)

    #rangos
    grafo_riqueza = crear_rangos(request, puntos, minimo, maximo, step=2)

    return render(request, template, locals())


def densidad_sombra(request, template="guiascacao/sombra/densidad_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)
    numero_parcelas = filtro.count()

    total_puntos = []
    for obj in filtro:
        total1 = Punto1.objects.exclude(especie__id__in=[11,60]).filter(ficha=obj).aggregate(pi=Sum('pequena'),
                                                                   mi=Sum('mediana'),
                                                                   gi=Sum('grande'), )
        try:
            suma_total1 = sum(total1.itervalues())
        except:
            pass

        total2 = Punto2.objects.exclude(especie__id__in=[11,60]).filter(ficha=obj).aggregate(pi=Sum('pequena'),
                                                                   mi=Sum('mediana'),
                                                                   gi=Sum('grande'), )
        try:
            suma_total2 = sum(total2.itervalues())
        except:
            pass

        total3 = Punto3.objects.exclude(especie__id__in=[11,60]).filter(ficha=obj).aggregate(pi=Sum('pequena'),
                                                                   mi=Sum('mediana'),
                                                                   gi=Sum('grande'), )
        try:
            suma_total3 = sum(total3.itervalues())
        except:
            suma_total3 = 0

        try:
            gran_suma = suma_total1 + suma_total2 + suma_total3
        except:
            gran_suma = 0

        try:
            densidad_total = (gran_suma  * float(10000)) / float(1890)
        except:
            densidad_total = 0
        #print "gran suma: %s - encuesta: %s " % (densidad_total, obj)

        total_puntos.append(densidad_total)
    # media arítmetica
    promedio2 = np.mean(total_puntos)
    # mediana
    mediana2 = np.median(total_puntos)
    # Desviación típica
    desviacion2 = np.std(total_puntos)
    #minimo
    minimo = min(total_puntos)
    #maximo
    maximo = max(total_puntos)
    #rangos
    grafo_densidad = crear_rangos(request, total_puntos, minimo, maximo, step=15)

    return render(request, template, locals())

def acciones_sombra(request, template="guiascacao/sombra/acciones_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    CHOICE_ACCIONES_SOMBRA = (
        (1, 'Reducir la sombra'),
        (2, 'Aumentar la sombra'),
        (3, 'Ninguna'),)

    dict_acciones = {}
    for obj in CHOICE_ACCIONES_SOMBRA:
        cnt = filtro.filter(accionessombra__accion=obj[0]).count()
        dict_acciones[obj[1]] = (cnt/float(len(filtro))) * 100

    CHOICE_PODA = (
        (1, 'Si'),

    )

    CHOICE_HERRAMIENTA = (
        (1, 'Si'),
        (2, 'No'),

    )
    dict_reducir_poda = {}
    dict_reducir_eliminando = {}
    VAR_REDUCIR = filtro.filter(accionessombra__accion=1).count()
    for obj in CHOICE_PODA:
        cnt_poda = filtro.filter(reducirsombra__poda=obj[0]).count()
        cnt_elim = filtro.filter(reducirsombra__eliminando=obj[0]).count()

        dict_reducir_poda[obj[1]] = (cnt_poda/float(VAR_REDUCIR)) * 100
        dict_reducir_eliminando[obj[1]] = (cnt_elim/float(VAR_REDUCIR)) * 100

    CHOICE_TODO = (
        (1, 'En todo la parcela '),
        (2, 'Solo en una parte de la parcela'),
    )
    dict_todo = {}
    for obj in CHOICE_TODO:
        cnt = filtro.filter(reducirsombra__todo=obj[0]).count()

        dict_todo[obj[1]] = (cnt/float(VAR_REDUCIR)) * 100

    dict_aumentar_poda = {}
    dict_aumentar_eliminando = {}
    VAR_AUMENTAR = filtro.filter(accionessombra__accion=2).count()
    for obj in CHOICE_PODA:
        cnt_sembra = filtro.filter(aumentarsombra__sembrando=obj[0]).count()
        cnt_cambia = filtro.filter(aumentarsombra__cambiando=obj[0]).count()

        try:
            dict_aumentar_poda[obj[1]] = (cnt_sembra/float(VAR_AUMENTAR)) * 100
        except:
            dict_aumentar_poda[obj[1]] = 0
        try:
            dict_aumentar_eliminando[obj[1]] = (cnt_cambia/float(VAR_AUMENTAR)) * 100
        except:
            dict_aumentar_eliminando[obj[1]] = 0

    dict_aumentar_todo = {}
    for obj in CHOICE_TODO:
        cnt = filtro.filter(aumentarsombra__todo=obj[0]).count()

        dict_aumentar_todo[obj[1]] = (cnt/float(VAR_REDUCIR)) * 100

    dict_manejo_herramienta = {}
    dict_manejo_formacion = {}
    for obj in CHOICE_HERRAMIENTA:
        cnt_herra = filtro.filter(manejosombra__herramientas=obj[0]).count()
        cnt_forma = filtro.filter(manejosombra__formacion=obj[0]).count()

        dict_manejo_herramienta[obj[1]] = (cnt_herra/float(len(filtro))) * 100
        dict_manejo_formacion[obj[1]] = (cnt_forma/float(len(filtro))) * 100

    return render(request, template, locals())

def change(f):
    if f is None:
        return 0
    else:
        return f

def caracterizacion_sombra(request, template="guiascacao/sombra/caracterizacion_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    #calculos sobre tipo de especies
    dict_todo_tipo = {}
    for obj in CHOICE_TIPO_PUNTO:
        p1_tipo = Punto1.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p2_tipo = Punto2.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p3_tipo = Punto3.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        dict_todo_tipo[obj[1]] = [p1_tipo,p2_tipo,p3_tipo]

    todo_tipo = []
    for k, myLIst in dict_todo_tipo.items():
        pe = [item['pi'] for item in myLIst if item['pi'] is not None]
        me = [item['mi'] for item in myLIst if item['mi'] is not None]
        ga = [item['gi'] for item in myLIst if item['gi'] is not None]
        todo_tipo.append([sum(pe),sum(me),sum(ga)])

    #calculos sobre tipo de copas
    dict_todo_copa = {}
    for obj in CHOICE_TIPO_COPA_PUNTO:
        p1_copa = Punto1.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo_de_copa=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p2_copa = Punto2.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo_de_copa=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p3_copa = Punto3.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, tipo_de_copa=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        dict_todo_copa[obj[1]] = [p1_copa,p2_copa,p3_copa]

    todo_copa = []
    for k, myLIst in dict_todo_copa.items():
        pe = [item['pi'] for item in myLIst if item['pi'] is not None]
        me = [item['mi'] for item in myLIst if item['mi'] is not None]
        ga = [item['gi'] for item in myLIst if item['gi'] is not None]
        todo_copa.append([sum(pe),sum(me),sum(ga)])


    #calculos sobre tipo de uso
    dict_todo_uso = {}
    for obj in CHOICE_TIPO_USO_PUNTO:
        p1_uso = Punto1.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, uso=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p2_uso = Punto2.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, uso=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        p3_uso = Punto3.objects.exclude(especie__id__in=[11,60]).filter(ficha__in=filtro, uso=obj[0]).aggregate(
                                                                                                    pi=Sum('pequena'),
                                                                                                    mi=Sum('mediana'),
                                                                                                    gi=Sum('grande'))
        dict_todo_uso[obj[1]] = [p1_uso,p2_uso,p3_uso]

    todo_uso = []
    for k, myLIst in dict_todo_uso.items():
        pe = [item['pi'] for item in myLIst if item['pi'] is not None]
        me = [item['mi'] for item in myLIst if item['mi'] is not None]
        ga = [item['gi'] for item in myLIst if item['gi'] is not None]
        todo_uso.append([sum(pe),sum(me),sum(ga)])

    return render(request, template, locals())

def dominancia_sombra(request, template="guiascacao/sombra/dominancia_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)

    CUANTO_ESPECIES = Especies.objects.exclude(id__in=[11,60]).count()
    dict_especie_todo = OrderedDict()

    for obj in Especies.objects.exclude(id__in=[11,60]):
        cnt_p1 = filtro.filter(punto1__especie=obj).aggregate(pi=Sum('punto1__pequena'),
                                                               mi=Sum('punto1__mediana'),
                                                               gi=Sum('punto1__grande'))

        cnt_p2 = filtro.filter(punto2__especie=obj).aggregate(pi=Sum('punto2__pequena'),
                                                              mi=Sum('punto2__mediana'),
                                                              gi=Sum('punto2__grande'))

        cnt_p3 = filtro.filter(punto3__especie=obj).aggregate(pi=Sum('punto3__pequena'),
                                                            mi=Sum('punto3__mediana'),
                                                            gi=Sum('punto3__grande'))

        dict_especie_todo[obj] = [cnt_p1,cnt_p2,cnt_p3]

    todo = {}
    SUMA_TOTAL_ESPECIE = 0
    for k, myLIst in dict_especie_todo.items():
        pe = [item['pi'] for item in myLIst if item['pi'] is not None]
        me = [item['mi'] for item in myLIst if item['mi'] is not None]
        ga = [item['gi'] for item in myLIst if item['gi'] is not None]
        suma_total = sum([sum(pe),sum(me),sum(ga)])
        if suma_total > 0:
            todo[k] = suma_total
            SUMA_TOTAL_ESPECIE += suma_total

    dominancia_todo = sorted(todo.iteritems(), key=lambda (k,v): (v,k), reverse=True)

    # for obj in dominancia_todo:
    #     print "%s --> %s" % (obj[0], obj[1])

    return render(request, template, locals())

def dimensiones_sombra(request, template="guiascacao/sombra/dimenciones_especies_sombra.html"):
    filtro = _queryset_filtrado_sombra(request)
    numero_parcelas = filtro.count()

    if request.GET.get('usos'):
        uso = request.GET['usos']
        MODELO_ESPECIES = Especies.objects.exclude(id__in=[11,60]).filter(tipo_uso__contains=uso)
    else:
        MODELO_ESPECIES = Especies.objects.exclude(id__in=[11,60])

    altura_p1 = []
    diametro_p1 = []
    anchura_p1 = []

    for obj in MODELO_ESPECIES:
        conteo = filtro.filter(punto1__especie=obj).count()
        cnt_p1 = filtro.filter(punto1__especie=obj).aggregate(pi=Sum('punto1__pequena'),
                                                               mi=Sum('punto1__mediana'),
                                                               gi=Sum('punto1__grande'))
        if conteo > 0:
            for k,v in cnt_p1.items():
                if v > 0:
                    if k == 'pi':
                        alti = [obj.p_altura] * int(v)
                        diam = [obj.p_diametro] * int(v)
                        anch = [obj.p_ancho] * int(v)
                        altura_p1.append(alti)
                        diametro_p1.append(diam)
                        anchura_p1.append(anch)
                    if k == 'mi':
                        alti = [obj.m_altura] * int(v)
                        diam = [obj.m_diametro] * int(v)
                        anch = [obj.m_ancho] * int(v)
                        altura_p1.append(alti)
                        diametro_p1.append(diam)
                        anchura_p1.append(anch)
                    if k == "gi":
                        alti = [obj.g_altura] * int(v)
                        diam = [obj.g_diametro] * int(v)
                        anch = [obj.g_ancho] * int(v)
                        altura_p1.append(alti)
                        diametro_p1.append(diam)
                        anchura_p1.append(anch)

    altura_p2 = []
    diametro_p2 = []
    anchura_p2 = []

    for obj in MODELO_ESPECIES:
        conteo = filtro.filter(punto2__especie=obj).count()
        cnt_p2 = filtro.filter(punto2__especie=obj).aggregate(pi=Sum('punto2__pequena'),
                                                               mi=Sum('punto2__mediana'),
                                                               gi=Sum('punto2__grande'))
        if conteo > 0:
            for k,v in cnt_p2.items():
                if v > 0:
                    if k == 'pi':
                        alti = [obj.p_altura] * int(v)
                        diam = [obj.p_diametro] * int(v)
                        anch = [obj.p_ancho] * int(v)
                        altura_p2.append(alti)
                        diametro_p2.append(diam)
                        anchura_p2.append(anch)
                    if k == 'mi':
                        alti = [obj.m_altura] * int(v)
                        diam = [obj.m_diametro] * int(v)
                        anch = [obj.m_ancho] * int(v)
                        altura_p2.append(alti)
                        diametro_p2.append(diam)
                        anchura_p2.append(anch)
                    if k == "gi":
                        alti = [obj.g_altura] * int(v)
                        diam = [obj.g_diametro] * int(v)
                        anch = [obj.g_ancho] * int(v)
                        altura_p2.append(alti)
                        diametro_p2.append(diam)
                        anchura_p2.append(anch)

    altura_p3 = []
    diametro_p3 = []
    anchura_p3 = []

    for obj in MODELO_ESPECIES:
        conteo = filtro.filter(punto3__especie=obj).count()
        cnt_p3 = filtro.filter(punto3__especie=obj).aggregate(pi=Sum('punto3__pequena'),
                                                               mi=Sum('punto3__mediana'),
                                                               gi=Sum('punto3__grande'))
        if conteo > 0:
            for k,v in cnt_p3.items():
                if v > 0:
                    if k == 'pi':
                        alti = [obj.p_altura] * int(v)
                        diam = [obj.p_diametro] * int(v)
                        anch = [obj.p_ancho] * int(v)
                        altura_p3.append(alti)
                        diametro_p3.append(diam)
                        anchura_p3.append(anch)
                    if k == 'mi':
                        alti = [obj.m_altura] * int(v)
                        diam = [obj.m_diametro] * int(v)
                        anch = [obj.m_ancho] * int(v)
                        altura_p3.append(alti)
                        diametro_p3.append(diam)
                        anchura_p3.append(anch)
                    if k == "gi":
                        alti = [obj.g_altura] * int(v)
                        diam = [obj.g_diametro] * int(v)
                        anch = [obj.g_ancho] * int(v)
                        altura_p3.append(alti)
                        diametro_p3.append(diam)
                        anchura_p3.append(anch)

    altura_total = altura_p1 + altura_p2 + altura_p3
    diametro_total = diametro_p1 + diametro_p2 + diametro_p3
    anchura_total = anchura_p1 + anchura_p2 + anchura_p3

    #con esto trabajo estan las listas completas
    todas_alturas = list(chain.from_iterable(altura_total))
    todas_diametro = list(chain.from_iterable(diametro_total))
    todas_anchura = list(chain.from_iterable(anchura_total))

    #promedio, rango, desviacion estandar, media de altura
    promedio_altura = np.mean(todas_alturas)
    desviacion_altura = np.std(todas_alturas)
    media_altura = np.median(todas_alturas)
    minimo_altura = min(todas_alturas)
    maximo_altura = max(todas_alturas)

    grafo_altura = crear_rangos(request, todas_alturas, minimo_altura, maximo_altura, step=3)

    #promedio, rango, desviacion estandar, media de diametro
    promedio_diametro = np.mean(todas_diametro)
    desviacion_diametro = np.std(todas_diametro)
    media_diametro = np.median(todas_diametro)
    minimo_diametro = min(todas_diametro)
    maximo_diametro = max(todas_diametro)

    grafo_diametro = crear_rangos(request, todas_diametro, minimo_diametro, maximo_diametro, step=16)

    #promedio, rango, desviacion estandar, media de anchura
    promedio_anchura = np.mean(todas_anchura)
    desviacion_anchura = np.std(todas_anchura)
    media_anchura = np.median(todas_anchura)
    minimo_anchura = min(todas_anchura)
    maximo_anchura = max(todas_anchura)

    grafo_anchura = crear_rangos(request, todas_anchura, minimo_anchura, maximo_anchura, step=2)

    return render(request, template, locals())
#----------------- fin salidas de sombra -------------------------
def _queryset_filtrado_poda(request):
    params = {}

    if 'fecha' in request.session:
        params['fecha_visita__year'] = request.session['fecha']

    if 'productor' in request.session:
        params['productor__nombre'] = request.session['productor']

    if 'organizacion' in request.session:
        params['productor__productor__organizacion'] = request.session['organizacion']

    if 'pais' in request.session:
        params['productor__pais'] = request.session['pais']

    if 'departamento' in request.session:
        params['productor__departamento'] = request.session['departamento']

    if 'municipio' in request.session:
        params['productor__municipio'] = request.session['municipio']

    if 'comunidad' in request.session:
        params['productor__comunidad'] = request.session['comunidad']

    if 'sexo' in request.session:
        params['productor__sexo'] = request.session['sexo']

    if 'tipologia' in request.session:
        params['productor__productor__tipologia'] = request.session['tipologia']

    unvalid_keys = []
    for key in params:
    	if not params[key]:
    		unvalid_keys.append(key)

    for key in unvalid_keys:
    	del params[key]

    print 'poda hermano'

    return FichaPoda.objects.filter(**params)
#----------------- salidas de poda -------------------------

def altura_poda(request, template="guiascacao/poda/altura_poda.html"):
    filtro = _queryset_filtrado_poda(request)
    numero_parcelas = filtro.count()

    altura1 = []
    altura2 = []
    altura3 = []
    for obj in filtro:
        cont1 = Punto1A.objects.filter(ficha=obj,plantas=1).aggregate(uno=Sum('uno'),
                                                               dos=Sum('dos'),
                                                               tres=Sum('tres'),
                                                               cuatro=Sum('cuatro'),
                                                               cinco=Sum('cinco'),
                                                               seis=Sum('seis'),
                                                               siete=Sum('siete'),
                                                               ocho=Sum('ocho'),
                                                               nueve=Sum('nueve'),
                                                               dies=Sum('diez'),
                                                               ).values()
        try:
            suma_cont1 = sum(cont1) / float(10)

        except:
            suma_cont1 = 0

        altura1.append(suma_cont1)
        #altura2
        cont2 = Punto2A.objects.filter(ficha=obj,plantas=1).aggregate(uno=Sum('uno'),
                                                               dos=Sum('dos'),
                                                               tres=Sum('tres'),
                                                               cuatro=Sum('cuatro'),
                                                               cinco=Sum('cinco'),
                                                               seis=Sum('seis'),
                                                               siete=Sum('siete'),
                                                               ocho=Sum('ocho'),
                                                               nueve=Sum('nueve'),
                                                               dies=Sum('diez'),
                                                               ).values()
        try:
            suma_cont2 = sum(cont2) / float(10)

        except:
            suma_cont2 = 0

        altura2.append(suma_cont2)
        #altura 3
        cont3 = Punto3A.objects.filter(ficha=obj,plantas=1).aggregate(uno=Sum('uno'),
                                                               dos=Sum('dos'),
                                                               tres=Sum('tres'),
                                                               cuatro=Sum('cuatro'),
                                                               cinco=Sum('cinco'),
                                                               seis=Sum('seis'),
                                                               siete=Sum('siete'),
                                                               ocho=Sum('ocho'),
                                                               nueve=Sum('nueve'),
                                                               dies=Sum('diez'),
                                                               ).values()
        try:
            suma_cont3 = sum(cont3) / float(10)

        except:
            suma_cont3 = 0

        altura3.append(suma_cont3)

    altura_total = altura1 + altura2 + altura3
    #promedio, rango, desviacion estandar, media de altura
    promedio_altura = np.mean(altura_total)
    desviacion_altura = np.std(altura_total)
    media_altura = np.median(altura_total)
    minimo_altura = min(altura_total)
    maximo_altura = max(altura_total)

    grafo_altura = crear_rangos(request, altura_total, minimo_altura, maximo_altura, step=2)


    return render(request, template, locals())

def ancho_poda(request, template="guiascacao/poda/ancho_poda.html"):
    filtro = _queryset_filtrado_poda(request)
    numero_parcelas = filtro.count()

    altura1 = []
    altura2 = []
    altura3 = []
    for obj in filtro:
        cont1 = Punto1A.objects.filter(ficha=obj,plantas=2).aggregate(uno=Sum('uno'),
                                                               dos=Sum('dos'),
                                                               tres=Sum('tres'),
                                                               cuatro=Sum('cuatro'),
                                                               cinco=Sum('cinco'),
                                                               seis=Sum('seis'),
                                                               siete=Sum('siete'),
                                                               ocho=Sum('ocho'),
                                                               nueve=Sum('nueve'),
                                                               dies=Sum('diez'),
                                                               ).values()
        try:
            suma_cont1 = sum(cont1) / float(10)

        except:
            suma_cont1 = 0

        altura1.append(suma_cont1)
        #altura2
        cont2 = Punto2A.objects.filter(ficha=obj,plantas=2).aggregate(uno=Sum('uno'),
                                                               dos=Sum('dos'),
                                                               tres=Sum('tres'),
                                                               cuatro=Sum('cuatro'),
                                                               cinco=Sum('cinco'),
                                                               seis=Sum('seis'),
                                                               siete=Sum('siete'),
                                                               ocho=Sum('ocho'),
                                                               nueve=Sum('nueve'),
                                                               dies=Sum('diez'),
                                                               ).values()
        try:
            suma_cont2 = sum(cont2) / float(10)

        except:
            suma_cont2 = 0

        altura2.append(suma_cont2)
        #altura 3
        cont3 = Punto3A.objects.filter(ficha=obj,plantas=2).aggregate(uno=Sum('uno'),
                                                               dos=Sum('dos'),
                                                               tres=Sum('tres'),
                                                               cuatro=Sum('cuatro'),
                                                               cinco=Sum('cinco'),
                                                               seis=Sum('seis'),
                                                               siete=Sum('siete'),
                                                               ocho=Sum('ocho'),
                                                               nueve=Sum('nueve'),
                                                               dies=Sum('diez'),
                                                               ).values()
        try:
            suma_cont3 = sum(cont3) / float(10)

        except:
            suma_cont3 = 0

        altura3.append(suma_cont3)

    altura_total = altura1 + altura2 + altura3
    #promedio, rango, desviacion estandar, media de altura
    promedio_altura = np.mean(altura_total)
    desviacion_altura = np.std(altura_total)
    media_altura = np.median(altura_total)
    minimo_altura = min(altura_total)
    maximo_altura = max(altura_total)

    grafo_altura = crear_rangos(request, altura_total, minimo_altura, maximo_altura, step=2)


    return render(request, template, locals())

def produccion_poda(request, template="guiascacao/poda/produccion_poda.html"):
    filtro = _queryset_filtrado_poda(request)
    numero_parcelas = filtro.count()

    CHOICE_PRODUCCION = (
        (1, 'Alta'),
        (2, 'Media'),
        (3, 'Baja'),
    )

    nivel = {}
    for obj in CHOICE_PRODUCCION:
        uno1 = filtro.filter(punto1c__plantas=1,punto1c__uno=obj[0]).count()
        dos1 = filtro.filter(punto1c__plantas=1,punto1c__dos=obj[0]).count()
        tres1 = filtro.filter(punto1c__plantas=1,punto1c__tres=obj[0]).count()
        cuatro1 = filtro.filter(punto1c__plantas=1,punto1c__cuatro=obj[0]).count()
        cinco1 = filtro.filter(punto1c__plantas=1,punto1c__cinco=obj[0]).count()
        seis1 = filtro.filter(punto1c__plantas=1,punto1c__seis=obj[0]).count()
        siete1 = filtro.filter(punto1c__plantas=1,punto1c__siete=obj[0]).count()
        ocho1 = filtro.filter(punto1c__plantas=1,punto1c__ocho=obj[0]).count()
        nueve1 = filtro.filter(punto1c__plantas=1,punto1c__nueve=obj[0]).count()
        diez1 = filtro.filter(punto1c__plantas=1,punto1c__diez=obj[0]).count()
        suma_punto1 = uno1 + dos1 + tres1 + cuatro1 + cinco1 + seis1 + siete1 + ocho1 + nueve1 + diez1

        uno2 = filtro.filter(punto2c__plantas=1,punto2c__uno=obj[0]).count()
        dos2 = filtro.filter(punto2c__plantas=1,punto2c__dos=obj[0]).count()
        tres2 = filtro.filter(punto2c__plantas=1,punto2c__tres=obj[0]).count()
        cuatro2 = filtro.filter(punto2c__plantas=1,punto2c__cuatro=obj[0]).count()
        cinco2 = filtro.filter(punto2c__plantas=1,punto2c__cinco=obj[0]).count()
        seis2 = filtro.filter(punto2c__plantas=1,punto2c__seis=obj[0]).count()
        siete2 = filtro.filter(punto2c__plantas=1,punto2c__siete=obj[0]).count()
        ocho2 = filtro.filter(punto2c__plantas=1,punto2c__ocho=obj[0]).count()
        nueve2 = filtro.filter(punto2c__plantas=1,punto2c__nueve=obj[0]).count()
        diez2 = filtro.filter(punto2c__plantas=1,punto2c__diez=obj[0]).count()
        suma_punto2 = uno2 + dos2 + tres2 + cuatro2 + cinco2 + seis2 + siete2 + ocho2 + nueve2 + diez2

        uno3 = filtro.filter(punto3c__plantas=1,punto3c__uno=obj[0]).count()
        dos3 = filtro.filter(punto3c__plantas=1,punto3c__dos=obj[0]).count()
        tres3 = filtro.filter(punto3c__plantas=1,punto3c__tres=obj[0]).count()
        cuatro3 = filtro.filter(punto3c__plantas=1,punto3c__cuatro=obj[0]).count()
        cinco3 = filtro.filter(punto3c__plantas=1,punto3c__cinco=obj[0]).count()
        seis3 = filtro.filter(punto3c__plantas=1,punto3c__seis=obj[0]).count()
        siete3 = filtro.filter(punto3c__plantas=1,punto3c__siete=obj[0]).count()
        ocho3 = filtro.filter(punto3c__plantas=1,punto3c__ocho=obj[0]).count()
        nueve3 = filtro.filter(punto3c__plantas=1,punto3c__nueve=obj[0]).count()
        diez3 = filtro.filter(punto3c__plantas=1,punto3c__diez=obj[0]).count()
        suma_punto3 = uno3 + dos3 + tres3 + cuatro3 + cinco3 + seis3 + siete3 + ocho3 + nueve3 + diez3

        totales_suma = suma_punto1 + suma_punto2 + suma_punto3

        nivel[obj[1]] = totales_suma


    return render(request, template, locals())

def atributos_poda(request, template="guiascacao/poda/atributos_poda.html"):
    filtro = _queryset_filtrado_poda(request)
    numero_parcelas = filtro.count()

    atributos = {}

    CHOICE_SI_NO = (
        (1, 'Si'),
        (2, 'No'),
    )

    for obj in CHOICE_PLANTAS2:
        atributos[obj[1]] = {}
        for x in CHOICE_SI_NO:
            uno1 = filtro.filter(punto1b__plantas=obj[0],punto1b__uno=x[0]).count()
            dos1 = filtro.filter(punto1b__plantas=obj[0],punto1b__dos=x[0]).count()
            tres1 = filtro.filter(punto1b__plantas=obj[0],punto1b__tres=x[0]).count()
            cuatro1 = filtro.filter(punto1b__plantas=obj[0],punto1b__cuatro=x[0]).count()
            cinco1 = filtro.filter(punto1b__plantas=obj[0],punto1b__cinco=x[0]).count()
            seis1 = filtro.filter(punto1b__plantas=obj[0],punto1b__seis=x[0]).count()
            siete1 = filtro.filter(punto1b__plantas=obj[0],punto1b__siete=x[0]).count()
            ocho1 = filtro.filter(punto1b__plantas=obj[0],punto1b__ocho=x[0]).count()
            nueve1 = filtro.filter(punto1b__plantas=obj[0],punto1b__nueve=x[0]).count()
            diez1 = filtro.filter(punto1b__plantas=obj[0],punto1b__diez=x[0]).count()
            suma_punto1 = uno1 + dos1 + tres1 + cuatro1 + cinco1 + seis1 + siete1 + ocho1 + nueve1 + diez1

            uno2 = filtro.filter(punto2b__plantas=obj[0],punto2b__uno=x[0]).count()
            dos2 = filtro.filter(punto2b__plantas=obj[0],punto2b__dos=x[0]).count()
            tres2 = filtro.filter(punto2b__plantas=obj[0],punto2b__tres=x[0]).count()
            cuatro2 = filtro.filter(punto2b__plantas=obj[0],punto2b__cuatro=x[0]).count()
            cinco2 = filtro.filter(punto2b__plantas=obj[0],punto2b__cinco=x[0]).count()
            seis2 = filtro.filter(punto2b__plantas=obj[0],punto2b__seis=x[0]).count()
            siete2 = filtro.filter(punto2b__plantas=obj[0],punto2b__siete=x[0]).count()
            ocho2 = filtro.filter(punto2b__plantas=obj[0],punto2b__ocho=x[0]).count()
            nueve2 = filtro.filter(punto2b__plantas=obj[0],punto2b__nueve=x[0]).count()
            diez2 = filtro.filter(punto2b__plantas=obj[0],punto2b__diez=x[0]).count()
            suma_punto2 = uno2 + dos2 + tres2 + cuatro2 + cinco2 + seis2 + siete2 + ocho2 + nueve2 + diez2

            uno3 = filtro.filter(punto3b__plantas=obj[0],punto3b__uno=x[0]).count()
            dos3 = filtro.filter(punto3b__plantas=obj[0],punto3b__dos=x[0]).count()
            tres3 = filtro.filter(punto3b__plantas=obj[0],punto3b__tres=x[0]).count()
            cuatro3 = filtro.filter(punto3b__plantas=obj[0],punto3b__cuatro=x[0]).count()
            cinco3 = filtro.filter(punto3b__plantas=obj[0],punto3b__cinco=x[0]).count()
            seis3 = filtro.filter(punto3b__plantas=obj[0],punto3b__seis=x[0]).count()
            siete3 = filtro.filter(punto3b__plantas=obj[0],punto3b__siete=x[0]).count()
            ocho3 = filtro.filter(punto3b__plantas=obj[0],punto3b__ocho=x[0]).count()
            nueve3 = filtro.filter(punto3b__plantas=obj[0],punto3b__nueve=x[0]).count()
            diez3 = filtro.filter(punto3b__plantas=obj[0],punto3b__diez=x[0]).count()
            suma_punto3 = uno3 + dos3 + tres3 + cuatro3 + cinco3 + seis3 + siete3 + ocho3 + nueve3 + diez3

            total = suma_punto1 + suma_punto2 + suma_punto3

            atributos[obj[1]][x[1]] = total

    return render(request, template, locals())

def analisis_poda(request, template="guiascacao/poda/analisis_poda.html"):
    filtro = _queryset_filtrado_poda(request)
    numero_parcelas = filtro.count()

    problema = {}
    for obj in CHOICES_PROBLEMA_PLANTA:
        cont = AnalisisPoda.objects.filter(ficha__in=filtro, campo1__contains=obj[0]).count()
        problema[obj[1]] = cont

    return render(request, template, locals())

def tipo_poda(request, template="guiascacao/poda/tipo_poda.html"):
    filtro = _queryset_filtrado_poda(request)
    numero_parcelas = filtro.count()

    problema = {}
    for obj in CHOICES_TIPO_PODA:
        cont = AnalisisPoda.objects.filter(ficha__in=filtro, campo2__contains=obj[0]).count()
        problema[obj[1]] = cont

    donde = {}
    for obj in CHOICE_REALIZA_PODA:
        cont = AnalisisPoda.objects.filter(ficha__in=filtro, campo3=obj[0]).count()
        donde[obj[1]] = cont

    vigor = {}
    for obj in CHOICE_VIGOR:
        cont = AnalisisPoda.objects.filter(ficha__in=filtro, campo4=obj[0]).count()
        vigor[obj[1]] = cont


    return render(request, template, locals())

def acciones_poda(request, template="guiascacao/poda/acciones_poda.html"):
    filtro = _queryset_filtrado_poda(request)
    numero_parcelas = filtro.count()

    luz = OrderedDict()
    for obj in CHOICE_ENTRADA_LUZ:
        cont = AnalisisPoda.objects.filter(ficha__in=filtro, campo5=obj[0]).count()
        luz[obj[1]] = cont

    meses = OrderedDict()
    for obj in CHOICES_FECHA_PODA:
        cont = AnalisisPoda.objects.filter(ficha__in=filtro, campo6__contains=obj[0]).count()
        meses[obj[1]] = cont

    herramienta = OrderedDict()
    formacion = OrderedDict()
    for obj in CHOICE_PODA:
        cont = ManejoPoda.objects.filter(ficha__in=filtro, herramientas=obj[0]).count()
        herramienta[obj[1]] = cont
        cont1 = ManejoPoda.objects.filter(ficha__in=filtro, formacion=obj[0]).count()
        formacion[obj[1]] = cont1

    return render(request, template, locals())
# ------------------ fin de poda ------------------

#----------------- inicio de plaga ----------------

def _queryset_filtrado_plaga(request):
    params = {}

    if 'fecha' in request.session:
        params['fecha_visita__year'] = request.session['fecha']

    if 'productor' in request.session:
        params['productor__nombre'] = request.session['productor']

    if 'organizacion' in request.session:
        params['productor__productor__organizacion'] = request.session['organizacion']

    if 'pais' in request.session:
        params['productor__pais'] = request.session['pais']

    if 'departamento' in request.session:
        params['productor__departamento'] = request.session['departamento']

    if 'municipio' in request.session:
        params['productor__municipio'] = request.session['municipio']

    if 'comunidad' in request.session:
        params['productor__comunidad'] = request.session['comunidad']

    if 'sexo' in request.session:
        params['productor__sexo'] = request.session['sexo']

    if 'tipologia' in request.session:
        params['productor__productor__tipologia'] = request.session['tipologia']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]

    print 'plaga hermano'

    return FichaPlaga.objects.filter(**params)
#----------------- salidas de plaga -------------------------

def historial_plaga(request, template="guiascacao/plaga/historial_plaga.html"):
    filtro = _queryset_filtrado_plaga(request)
    numero_parcelas = filtro.count()

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
    )

    plagas = OrderedDict()
    for obj in CHOICE_ENFERMEDADES_CACAOTALES:
        cont_visto = filtro.filter(plagasenfermedad__plagas=obj[0],
                                   plagasenfermedad__visto=1).count()
        cont_dano = filtro.filter(plagasenfermedad__plagas=obj[0],
                                  plagasenfermedad__dano=1).count()
        plagas[obj[1]] = [((float(cont_visto)/float(numero_parcelas))*100), ((float(cont_dano)/float(numero_parcelas))*100)]

    promedio_plagas = OrderedDict()
    for obj in CHOICE_ENFERMEDADES_CACAOTALES:
        cont_avg = filtro.filter(plagasenfermedad__plagas=obj[0]).aggregate(promedio=Avg('plagasenfermedad__promedio'))['promedio']
        promedio_plagas[obj[1]] = cont_avg

    mediana_plagas = OrderedDict()
    for obj in CHOICE_ENFERMEDADES_CACAOTALES:
        numeros = filtro.filter(plagasenfermedad__plagas=obj[0]).values_list('plagasenfermedad__promedio', flat=True)
        mediana_plagas[obj[1]] = np.median(numeros)

    return render(request, template, locals())


def acciones_plaga(request, template="guiascacao/plaga/acciones_plaga.html"):
    filtro = _queryset_filtrado_plaga(request)
    numero_parcelas = filtro.count()

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

    acciones_plagas = OrderedDict()
    for obj in CHOICE_ACCIONES_ENFERMEDADES:
        conteo_si = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],accionesenfermedad__realiza_manejo=1).count()
        avg_veces = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],accionesenfermedad__realiza_manejo=1).aggregate(promedio=Avg('accionesenfermedad__cuantas_veces'))['promedio']
        numeros = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],accionesenfermedad__realiza_manejo=1).values_list('accionesenfermedad__cuantas_veces', flat=True)
        acciones_plagas[obj[1]] = [conteo_si,(float(conteo_si)/float(numero_parcelas)*100),avg_veces,np.std(numeros)]

    grafo_momento = OrderedDict()
    for obj in CHOICE_ACCIONES_ENFERMEDADES:
        ene = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='A').count()
        feb = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='B').count()
        mar = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='C').count()
        abr = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='D').count()
        may = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='E').count()
        jun = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='F').count()
        jul = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='G').count()
        ago = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='H').count()
        sep = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='I').count()
        octu = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='J').count()
        nov = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='K').count()
        dic = filtro.filter(accionesenfermedad__plagas_acciones=obj[0],
                                         accionesenfermedad__realiza_manejo=1,
                                         accionesenfermedad__meses__contains='L').count()
        grafo_momento[obj[1]] = [ene,feb,mar,abr,may,jun,jul,ago,sep,octu,nov,dic]

    grafo_fuente = OrderedDict()
    for obj in CHOICE_ORIENTACION:
        conteo = filtro.filter(orientacion__fuentes__contains=obj[0]).count()
        grafo_fuente[obj[1]] = (float(conteo)/float(numero_parcelas)*100)


    return render(request, template, locals())

def fuente_incidencia_plaga(request, template="guiascacao/plaga/fuente_incidencia_plaga.html"):
    filtro = _queryset_filtrado_plaga(request)
    numero_parcelas = filtro.count()

    tabla_incidencia = OrderedDict()

    for obj in CHOICE_OBSERVACION_PUNTO1:
        tabla_incidencia[obj[1]] = {}
        lista_arreglo = []
        contador_si = 0
        for x in filtro:
            punto1 = ObservacionPunto1.objects.filter(ficha=x,planta=obj[0]).aggregate(total=Sum('contador'))['total']

            punto2 = ObservacionPunto2.objects.filter(ficha=x,planta=obj[0]).aggregate(total=Sum('contador'))['total']

            punto3= ObservacionPunto3.objects.filter(ficha=x,planta=obj[0]).aggregate(total=Sum('contador'))['total']

            try:
                suma_total = punto1 + punto2 + punto3
            except:
               pass
            porcentaje_suma_total = (float(suma_total)/30)*100
            if suma_total >=1:
                contador_si += 1
            lista_arreglo.append(porcentaje_suma_total)

            tabla_incidencia[obj[1]] = (contador_si,np.mean(lista_arreglo),np.std(lista_arreglo),np.median(lista_arreglo),min(lista_arreglo),max(lista_arreglo))

    return render(request, template, locals())

def produccion_rendimiento_plaga(request, template="guiascacao/plaga/produccion_rendimiento_plaga.html"):
    filtro = _queryset_filtrado_plaga(request)
    numero_parcelas = filtro.count()

    grafo_nivel_produccion = OrderedDict()
    alto1 = filtro.aggregate(total=Sum('observacionpunto1nivel__alta'))['total'] or 0
    alto2 = filtro.aggregate(total=Sum('observacionpunto2nivel__alta'))['total'] or 0
    alto3 = filtro.aggregate(total=Sum('observacionpunto3nivel__alta'))['total'] or 0

    total_alta = alto1 + alto2 + alto3

    media1 = filtro.aggregate(total=Sum('observacionpunto1nivel__media'))['total'] or 0
    media2 = filtro.aggregate(total=Sum('observacionpunto2nivel__media'))['total'] or 0
    media3 = filtro.aggregate(total=Sum('observacionpunto3nivel__media'))['total'] or 0

    total_media = media1 + media2 + media3

    baja1 = filtro.aggregate(total=Sum('observacionpunto1nivel__baja'))['total'] or 0
    baja2 = filtro.aggregate(total=Sum('observacionpunto2nivel__baja'))['total'] or 0
    baja3 = filtro.aggregate(total=Sum('observacionpunto3nivel__baja'))['total'] or 0

    total_baja = baja1 + baja2 + baja3

    grafo_nivel_produccion['Alta'] = float((total_alta*100))/(float(numero_parcelas)*30)
    grafo_nivel_produccion['Media'] = float((total_media*100))/(float(numero_parcelas)*30)
    grafo_nivel_produccion['Baja'] = float((total_baja*100))/(float(numero_parcelas)*30)

    grafo_monilia = generic_indice_produccion(request, 1)
    grafo_mazorca = generic_indice_produccion(request, 2)
    grafo_ardillas = generic_indice_produccion(request, 10)
    grafo_machete = generic_indice_produccion(request, 3)
    grafo_zompopo = generic_indice_produccion(request, 6)


    return render(request, template, locals())

def generic_indice_produccion(request, tipo=0):
    filtro = _queryset_filtrado_plaga(request)
    numero_parcelas = filtro.count()

    grafo_dispercion = []
    grafo_nivel_produccion2 = OrderedDict()
    for x in filtro:
        alto1 = ObservacionPunto1Nivel.objects.filter(ficha=x).aggregate(total=Sum('alta'))['total'] or 0
        alto2 = ObservacionPunto2Nivel.objects.filter(ficha=x).aggregate(total=Sum('alta'))['total'] or 0
        alto3 = ObservacionPunto3Nivel.objects.filter(ficha=x).aggregate(total=Sum('alta'))['total'] or 0
        total_alta = alto1 + alto2 + alto3

        media1 = ObservacionPunto1Nivel.objects.filter(ficha=x).aggregate(total=Sum('media'))['total'] or 0
        media2 = ObservacionPunto2Nivel.objects.filter(ficha=x).aggregate(total=Sum('media'))['total'] or 0
        media3 = ObservacionPunto3Nivel.objects.filter(ficha=x).aggregate(total=Sum('media'))['total'] or 0

        total_media = media1 + media2 + media3

        baja1 = ObservacionPunto1Nivel.objects.filter(ficha=x).aggregate(total=Sum('baja'))['total'] or 0
        baja2 = ObservacionPunto2Nivel.objects.filter(ficha=x).aggregate(total=Sum('baja'))['total'] or 0
        baja3 = ObservacionPunto3Nivel.objects.filter(ficha=x).aggregate(total=Sum('baja'))['total'] or 0

        total_baja = baja1 + baja2 + baja3

        grafo_nivel_produccion2['Alta'] = total_alta
        grafo_nivel_produccion2['Media'] = total_media
        grafo_nivel_produccion2['Baja'] = total_baja

        #------------------------------------------------------
        formula = float((5*grafo_nivel_produccion2['Baja'])+(20*grafo_nivel_produccion2['Media'])+(40*grafo_nivel_produccion2['Alta'])) / float(30)
        #-----------------------------------------------------------

        punto1 = ObservacionPunto1.objects.filter(ficha=x,planta=tipo).aggregate(total=Sum('contador'))['total'] or 0

        punto2 = ObservacionPunto2.objects.filter(ficha=x,planta=tipo).aggregate(total=Sum('contador'))['total'] or 0

        punto3= ObservacionPunto3.objects.filter(ficha=x,planta=tipo).aggregate(total=Sum('contador'))['total'] or 0


        suma_total = punto1 + punto2 + punto3

        #----------------------------------------
        monilia = (float(suma_total)/float(30))*100
        #-----------------------------------------

        grafo_dispercion.append([monilia,formula])

    return grafo_dispercion


def analisis_plaga(request, template="guiascacao/plaga/analisis_plaga.html"):
    filtro = _queryset_filtrado_plaga(request)
    numero_parcelas = filtro.count()

    grafo_analisis_plaga = OrderedDict()
    for obj in CHOICE_ENFERMEDADES:
        cont_observada = filtro.filter(problemasprincipales__observadas__contains=obj[0]).count()
        cont_principal = filtro.filter(problemasprincipales__principales__contains=obj[0]).count()
        grafo_analisis_plaga[obj[1]] = [cont_observada,cont_principal]

    grafo_situacion_plaga = OrderedDict()
    for obj in CHOICE_SITUACION_PLAGAS:
        cont_situacion = filtro.filter(problemasprincipales__situacion=obj[0]).count()

        grafo_situacion_plaga[obj[1]] = cont_situacion

    return render(request, template, locals())

def observacion_sombra_poda_plaga(request, template="guiascacao/plaga/observacion_sombra_poda_plaga.html"):
    filtro = _queryset_filtrado_plaga(request)
    numero_parcelas = filtro.count()

    grafo_suelo_plaga = OrderedDict()
    for obj in CHOICE_ENFERMEDADES_PUNTO6_1:
        conteo = filtro.filter(punto6plagas__observaciones__contains=obj[0]).count()
        grafo_suelo_plaga[obj[1]] = conteo

    grafo_sombra_plaga = OrderedDict()
    for obj in CHOICE_ENFERMEDADES_PUNTO6_2:
        conteo = filtro.filter(punto6plagas__sombra=obj[0]).count()
        grafo_sombra_plaga[obj[1]] = conteo

    grafo_poda_plaga = OrderedDict()
    for obj in CHOICE_ENFERMEDADES_PUNTO6_3:
        conteo = filtro.filter(punto6plagas__manejo__contains=obj[0]).count()
        grafo_poda_plaga[obj[1]] = conteo

    return render(request, template, locals())

def acciones_manejo_plaga(request, template="guiascacao/plaga/acciones_manejo_plaga.html"):
    filtro = _queryset_filtrado_plaga(request)
    numero_parcelas = filtro.count()

    tabla_acciones = OrderedDict()
    for obj in CHOICE_ACCIONES_PUNTO7_1:
        conteo_si = filtro.filter(punto7plagas__manejo=obj[0]).count()
        conteo_toda = filtro.filter(punto7plagas__manejo=obj[0], punto7plagas__parte=1).count()
        conteo_alguna = filtro.filter(punto7plagas__manejo=obj[0], punto7plagas__parte=2).count()
        tabla_acciones[obj[1]] = [conteo_si, conteo_toda,conteo_alguna]

    grafo_momento = OrderedDict()
    for obj in CHOICE_ACCIONES_PUNTO7_1:
        ene = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='A').count()
        feb = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='B').count()
        mar = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='C').count()
        abr = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='D').count()
        may = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='E').count()
        jun = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='F').count()
        jul = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='G').count()
        ago = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='H').count()
        sep = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='I').count()
        octu = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='J').count()
        nov = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='K').count()
        dic = filtro.filter(punto7plagas__manejo=obj[0],
                                         punto7plagas__meses__contains='L').count()
        grafo_momento[obj[1]] = [ene,feb,mar,abr,may,jun,jul,ago,sep,octu,nov,dic]

    return render(request, template, locals())

def equipos_formacion_plaga(request, template="guiascacao/plaga/equipos_formacion_plaga.html"):
    filtro = _queryset_filtrado_plaga(request)
    numero_parcelas = filtro.count()

    grafo_equipos = OrderedDict()
    for obj in CHOICE_ENFERMEDADES_PUNTO8:
        conteo = filtro.filter(punto8y9plagas__equipos__contains=obj[0]).count()
        grafo_equipos[obj[1]] = conteo

    grafo_formacion = OrderedDict()
    for obj in CHOICE_SI_NO:
        conteo = filtro.filter(punto8y9plagas__opcion=obj[0]).count()
        grafo_formacion[obj[1]] = conteo

    return render(request, template, locals())

#----------  fin salidas plagas  --------------------------
#-----------Inicio de piso -----------------------
def _queryset_filtrado_piso(request):
    params = {}

    if 'fecha' in request.session:
        params['fecha_visita__year'] = request.session['fecha']

    if 'productor' in request.session:
        params['productor__nombre'] = request.session['productor']

    if 'organizacion' in request.session:
        params['productor__productor__organizacion'] = request.session['organizacion']

    if 'pais' in request.session:
        params['productor__pais'] = request.session['pais']

    if 'departamento' in request.session:
        params['productor__departamento'] = request.session['departamento']

    if 'municipio' in request.session:
        params['productor__municipio'] = request.session['municipio']

    if 'comunidad' in request.session:
        params['productor__comunidad'] = request.session['comunidad']

    if 'sexo' in request.session:
        params['productor__sexo'] = request.session['sexo']

    if 'tipologia' in request.session:
        params['productor__productor__tipologia'] = request.session['tipologia']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]

    print 'Piso hermano'

    return FichaPiso.objects.filter(**params)
#----------  SALIDAS DE PISO --------------------------
def estado_piso(request, template="guiascacao/piso/estado_piso.html"):
    filtro = _queryset_filtrado_piso(request)
    numero_parcelas = filtro.count()

    grafo_estado = OrderedDict()
    for obj in CHOICE_PISO1:
        conteo_p1 = filtro.filter(pisopunto1__punto1__contains=obj[0]).count()
        conteo_p2 = filtro.filter(pisopunto1__punto2__contains=obj[0]).count()
        grafo_estado[obj[1]] = (conteo_p1,conteo_p2)

    grafo_manejo_piso = OrderedDict()
    for obj in CHOICE_PISO3:
        conteo_p1 = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1).count()
        grafo_manejo_piso[obj[1]] = conteo_p1

    return render(request, template, locals())

def estado_piso2(request, template="guiascacao/piso/estado_manejo_piso.html"):
    filtro = _queryset_filtrado_piso(request)
    numero_parcelas = filtro.count()

    tabla_manejo_piso = OrderedDict()
    for obj in CHOICE_PISO3:
        conteo = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1).count()
        arreglo_manejo = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1).values_list('pisopunto3__veces', flat=True)
        tabla_manejo_piso[obj[1]] = (conteo,np.mean(arreglo_manejo),
                                                          np.std(arreglo_manejo),np.median(arreglo_manejo),
                                                          min(arreglo_manejo),max(arreglo_manejo))

    grafo_momento = OrderedDict()
    for obj in CHOICE_PISO3:
        ene = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='A').count()
        feb = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='B').count()
        mar = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='C').count()
        abr = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='D').count()
        may = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='E').count()
        jun = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='F').count()
        jul = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='G').count()
        ago = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='H').count()
        sep = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='I').count()
        octu = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='J').count()
        nov = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='K').count()
        dic = filtro.filter(pisopunto3__manejo=obj[0], pisopunto3__realiza=1,pisopunto3__meses__contains='L').count()
        grafo_momento[obj[1]] = [ene,feb,mar,abr,may,jun,jul,ago,sep,octu,nov,dic]

    grafo_orientacion = OrderedDict()
    for obj in CHOICE_PISO4:
        conteo = filtro.filter(pisopunto4__manejo=obj[0]).count()
        grafo_orientacion[obj[1]] = conteo

    return render(request, template, locals())

def orientacion_composicion_piso(request, template="guiascacao/piso/orientacion_composicion_piso.html"):
    filtro = _queryset_filtrado_piso(request)
    numero_parcelas = filtro.count()

    tabla_composicion = OrderedDict()
    for obj in CHOICE_PISO5:
        conteo = filtro.filter(pisopunto5__estado=obj[0]).count()
        suma = filtro.filter(pisopunto5__estado=obj[0]).aggregate(total=Sum('pisopunto5__conteo'))['total']

        tabla_composicion[obj[1]] = suma

    VAR_TOTAL = 0
    for k,v in tabla_composicion.items():
        VAR_TOTAL += v

    return render(request, template, locals())

def analisis_piso(request, template="guiascacao/piso/analisis_piso.html"):
    filtro = _queryset_filtrado_piso(request)
    numero_parcelas = filtro.count()

    grafo_competencia = OrderedDict()
    for obj in CHOICE_PISO6_1:
        conteo = filtro.filter(pisopunto6__manejo__contains=obj[0]).count()
        grafo_competencia[obj[1]] = conteo

    grafo_cobertura = OrderedDict()
    for obj in CHOICE_PISO6_2:
        conteo = filtro.filter(pisopunto6__estado=obj[0]).count()
        grafo_cobertura[obj[1]] = conteo

    grafo_maleza = OrderedDict()
    for obj in CHOICE_PISO6_3:
        conteo = filtro.filter(pisopunto6__maleza__contains=obj[0]).count()
        grafo_maleza[obj[1]] = conteo

    return render(request, template, locals())

def suelo_piso(request, template="guiascacao/piso/suelo_piso.html"):
    filtro = _queryset_filtrado_piso(request)
    numero_parcelas = filtro.count()

    grafo_suelo = OrderedDict()
    for obj in CHOICE_PISO7_1:
        conteo = filtro.filter(pisopunto7__suelo__contains=obj[0]).count()
        grafo_suelo[obj[1]] = conteo

    grafo_sombra = OrderedDict()
    for obj in CHOICE_PISO7_2:
        conteo = filtro.filter(pisopunto7__sombra__contains=obj[0]).count()
        grafo_sombra[obj[1]] = conteo

    grafo_manejo = OrderedDict()
    for obj in CHOICE_PISO7_3:
        conteo = filtro.filter(pisopunto7__manejo__contains=obj[0]).count()
        grafo_manejo[obj[1]] = conteo

    return render(request, template, locals())

def propuesta_piso(request, template="guiascacao/piso/propuesta_piso.html"):
    filtro = _queryset_filtrado_piso(request)
    numero_parcelas = filtro.count()

    tabla_propuesta = OrderedDict()
    for obj in CHOICE_PISO8:
        conteo_piso = filtro.filter(pisopunto8__piso=obj[0]).count()
        conteo_toda = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__parte=1).count()
        conteo_alguna = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__parte=2).count()
        tabla_propuesta[obj[1]] = (conteo_piso,conteo_toda,conteo_alguna)

    grafo_manejo = OrderedDict()
    for obj in CHOICE_PISO8:
        ene = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='A').count()
        feb = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='B').count()
        mar = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='C').count()
        abr = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='D').count()
        may = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='E').count()
        jun = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='F').count()
        jul = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='G').count()
        ago = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='H').count()
        sep = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='I').count()
        octu = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='J').count()
        nov = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='K').count()
        dic = filtro.filter(pisopunto8__piso=obj[0], pisopunto8__meses__contains='L').count()
        grafo_manejo[obj[1]] = [ene,feb,mar,abr,may,jun,jul,ago,sep,octu,nov,dic]


    return render(request, template, locals())


def equipo_piso(request, template="guiascacao/piso/equipo_piso.html"):
    filtro = _queryset_filtrado_piso(request)
    numero_parcelas = filtro.count()

    grafo_equipo = OrderedDict()
    for obj in CHOICE_PISO10:
        conteo = filtro.filter(pisopunto10__equipo__contains=obj[0]).count()
        grafo_equipo[obj[1]] = conteo

    grafo_formacion = OrderedDict()
    for obj in CHOICE_SI_NO:
        conteo = filtro.filter(pisopunto10__formacion=obj[0]).count()
        grafo_formacion[obj[1]] = conteo


    return render(request, template, locals())

#--------- fin de salida de piso  -------------------------
# -------- comienza salidas de cosecha -------------
def _queryset_filtrado_cosecha(request):
    params = {}

    if 'fecha' in request.session:
        params['fecha_visita__year'] = request.session['fecha']

    if 'productor' in request.session:
        params['productor__nombre'] = request.session['productor']

    if 'organizacion' in request.session:
        params['productor__productor__organizacion'] = request.session['organizacion']

    if 'pais' in request.session:
        params['productor__pais'] = request.session['pais']

    if 'departamento' in request.session:
        params['productor__departamento'] = request.session['departamento']

    if 'municipio' in request.session:
        params['productor__municipio'] = request.session['municipio']

    if 'comunidad' in request.session:
        params['productor__comunidad'] = request.session['comunidad']

    if 'sexo' in request.session:
        params['productor__sexo'] = request.session['sexo']

    if 'tipologia' in request.session:
        params['productor__productor__tipologia'] = request.session['tipologia']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]

    print 'Cosecha hermano'

    return FichaCosecha.objects.filter(**params)
#----------  SALIDAS DE COSECHA --------------------------

def conversacion_cosecha(request, template="guiascacao/cosecha/conversaciones_cosecha.html"):
    filtro = _queryset_filtrado_cosecha(request)
    numero_parcelas = filtro.count()

    dict_conversacion1 = OrderedDict()
    for obj in CHOICE_COSECHA_CONVERSACION_1:
        conteo = filtro.filter(cosechaconversacion1__conversacion1__contains=obj[0]).count()
        dict_conversacion1[obj[1]] = conteo

    dict_conversacion2 = OrderedDict()
    for obj in CHOICE_COSECHA_CONVERSACION_2:
        conteo = filtro.filter(cosechaconversacion1__conversacion2__contains=obj[0]).count()
        dict_conversacion2[obj[1]] = conteo

    dict_conversacion3 = OrderedDict()
    for obj in CHOICE_COSECHA_CONVERSACION_3:
        conteo = filtro.filter(cosechaconversacion1__conversacion3__contains=obj[0]).count()
        dict_conversacion3[obj[1]] = conteo

    dict_conversacion4 = OrderedDict()
    for obj in CHOICE_COSECHA_CONVERSACION_4:
        conteo = filtro.filter(cosechaconversacion1__conversacion4__contains=obj[0]).count()
        dict_conversacion4[obj[1]] = conteo

    dict_conversacion5 = OrderedDict()
    for obj in CHOICE_COSECHA_CONVERSACION_5:
        conteo = filtro.filter(cosechaconversacion2__conversacion5__contains=obj[0]).count()
        dict_conversacion5[obj[1]] = conteo

    list_conversacion6 = []
    for obj in filtro:
        lista = CosechaConversacion2.objects.filter(ficha=obj).values_list('conversacion6', flat=True)
        list_conversacion6.append(list(lista))

    promedio = np.mean(list(list_conversacion6))
    desviacion_estandar = np.std(list(list_conversacion6))
    mediano = np.median(list(list_conversacion6))
    minimo = min(list(list_conversacion6))
    maximo = max(list(list_conversacion6))

    dict_conversacion7 = OrderedDict()
    for obj in CHOICE_COSECHA_CONVERSACION_7:
        conteo = filtro.filter(cosechaconversacion2__conversacion7__contains=obj[0]).count()
        dict_conversacion7[obj[1]] = conteo

    dict_conversacion8 = OrderedDict()
    for obj in CHOICE_COSECHA_CONVERSACION_8:
        conteo = filtro.filter(cosechaconversacion2__conversacion8__contains=obj[0]).count()
        dict_conversacion8[obj[1]] = conteo


    return render(request, template, locals())

def datos_sanos_cosecha(request, template="guiascacao/cosecha/datos_sanos_cosecha.html"):
    filtro = _queryset_filtrado_cosecha(request)
    numero_parcelas = filtro.count()

    danadas = generic_datos_cosecha(request,1)

    return render(request, template, locals())

def datos_enfermas_cosecha(request, template="guiascacao/cosecha/datos_enfermas_cosecha.html"):
    filtro = _queryset_filtrado_cosecha(request)
    numero_parcelas = filtro.count()

    danadas = generic_datos_cosecha(request,2)

    return render(request, template, locals())

def datos_danadas_cosecha(request, template="guiascacao/cosecha/datos_danadas_cosecha.html"):
    filtro = _queryset_filtrado_cosecha(request)
    numero_parcelas = filtro.count()

    danadas = generic_datos_cosecha(request,3)

    return render(request, template, locals())

def generic_datos_cosecha(request, tipo=0):
    filtro = _queryset_filtrado_cosecha(request)
    numero_parcelas = filtro.count()

    punto1_plantas = filtro.filter(cosechapunto1__mazorcas=tipo,
                    cosechapunto1__contador__gt=0).aggregate(plantas=Sum('cosechapunto1__contador'))['plantas']
    punto2_plantas = filtro.filter(cosechapunto2__mazorcas=tipo,
                    cosechapunto2__contador__gt=0).aggregate(plantas=Sum('cosechapunto2__contador'))['plantas']
    punto3_plantas = filtro.filter(cosechapunto3__mazorcas=tipo,
                    cosechapunto3__contador__gt=0).aggregate(plantas=Sum('cosechapunto3__contador'))['plantas']

    #Numero 1
    TOTAL_PLANTAS = punto1_plantas + punto2_plantas + punto3_plantas

    punto1_mazorca_sana = filtro.filter(cosechapunto1__mazorcas=tipo).aggregate(sanas=Sum('cosechapunto1__total_platas'))['sanas']
    punto2_mazorca_sana = filtro.filter(cosechapunto2__mazorcas=tipo).aggregate(sanas=Sum('cosechapunto2__total_platas'))['sanas']
    punto3_mazorca_sana = filtro.filter(cosechapunto3__mazorcas=tipo).aggregate(sanas=Sum('cosechapunto3__total_platas'))['sanas']

    #Numero 2
    TOTAL_MAZORCAS_SANAS = punto1_mazorca_sana + punto2_mazorca_sana + punto3_mazorca_sana
    #Numero 3
    MAZORCA_SANA_POR_PLATA = float(TOTAL_MAZORCAS_SANAS)/float(TOTAL_PLANTAS)
    #Numero 4
    PROMEDIO_PLATAS_POR_MANZANA = filtro.aggregate(promedio=Avg('cosechaareaplantas__plantas'))['promedio']
    #Numero 5
    MAZORCAS_SANAS_X_MANZANAS = (MAZORCA_SANA_POR_PLATA * PROMEDIO_PLATAS_POR_MANZANA) * float(1.6)
    #Numero 6
    PESO_BABA = float(MAZORCAS_SANAS_X_MANZANAS) / (float(3.5) * 100)
    #numero 7
    PESO_GRANO_SECO = float(PESO_BABA)/float(3)
    #numero 8
    PESO_GRANO_SECO_KILO_HA = PESO_GRANO_SECO * (1.4 * 0.454 * 100)

    completo = [TOTAL_PLANTAS,TOTAL_MAZORCAS_SANAS,MAZORCA_SANA_POR_PLATA,
                          PROMEDIO_PLATAS_POR_MANZANA,MAZORCAS_SANAS_X_MANZANAS,
                          PESO_BABA,PESO_GRANO_SECO,PESO_GRANO_SECO_KILO_HA]
    return completo

def analisis_cosecha(request, template="guiascacao/cosecha/analisis_cosecha.html"):
    filtro = _queryset_filtrado_cosecha(request)
    numero_parcelas = filtro.count()

    analisis_1 = OrderedDict()
    for obj in CHOICE_COSECHA_ANALISIS_1:
        conteo = filtro.filter(cosechaanalisis__analisis1__contains=obj[0]).count()
        analisis_1[obj[1]] = conteo

    analisis_2 = OrderedDict()
    for obj in CHOICE_COSECHA_ANALISIS_2:
        conteo = filtro.filter(cosechaanalisis__analisis2__contains=obj[0]).count()
        analisis_2[obj[1]] = conteo

    analisis_3 = OrderedDict()
    for obj in CHOICE_COSECHA_ANALISIS_3:
        conteo = filtro.filter(cosechaanalisis__analisis3__contains=obj[0]).count()
        analisis_3[obj[1]] = conteo

    return render(request, template, locals())

#-------------- fin de salidas de cosecha -------------

#-------------- comienza salidas de cierre ------------
def _queryset_filtrado_cierre(request):
    params = {}

    if 'fecha' in request.session:
        params['fecha_visita__year'] = request.session['fecha']

    if 'productor' in request.session:
        params['productor__nombre'] = request.session['productor']

    if 'organizacion' in request.session:
        params['productor__productor__organizacion'] = request.session['organizacion']

    if 'pais' in request.session:
        params['productor__pais'] = request.session['pais']

    if 'departamento' in request.session:
        params['productor__departamento'] = request.session['departamento']

    if 'municipio' in request.session:
        params['productor__municipio'] = request.session['municipio']

    if 'comunidad' in request.session:
        params['productor__comunidad'] = request.session['comunidad']

    if 'sexo' in request.session:
        params['productor__sexo'] = request.session['sexo']

    if 'tipologia' in request.session:
        params['productor__productor__tipologia'] = request.session['tipologia']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]

    print 'Cierre hermano'

    return FichaCierre.objects.filter(**params)

#---------- SALIDAS DE CIERRE --------------------------

def sombra_cierre(request, template="guiascacao/cierre/sombra_cierre.html"):
    filtro = _queryset_filtrado_cierre(request)
    numero_parcelas = filtro.count()

    impacto_sombra = OrderedDict()
    for obj in CHOICE_CIERRE_1_1_IMPACTO:
        conteo = filtro.filter(cierremanejo1__campo1__contains=obj[0]).count()
        impacto_sombra[obj[1]] = conteo

    planificada_sombra = OrderedDict()
    for obj in CHOICE_CIERRE_1_1_PLANIFICADA:
        conteo = filtro.filter(cierremanejo1__campo2__contains=obj[0]).count()
        planificada_sombra[obj[1]] = conteo

    realizada_sombra = OrderedDict()
    for obj in CHOICE_CIERRE_1_1_REALIZADA:
        conteo = filtro.filter(cierremanejo1__campo3__contains=obj[0]).count()
        realizada_sombra[obj[1]] = conteo

    resultado_sombra = OrderedDict()
    for obj in CHOICE_CIERRE_1_1_RESULTADOS:
        conteo = filtro.filter(cierremanejo1__campo4__contains=obj[0]).count()
        resultado_sombra[obj[1]] = conteo

    return render(request, template, locals())


def poda_cierre(request, template="guiascacao/cierre/poda_cierre.html"):
    filtro = _queryset_filtrado_cierre(request)
    numero_parcelas = filtro.count()

    impacto_poda = OrderedDict()
    for obj in CHOICE_CIERRE_1_2_IMPACTO:
        conteo = filtro.filter(cierremanejo2__campo1__contains=obj[0]).count()
        impacto_poda[obj[1]] = conteo

    planificada_poda = OrderedDict()
    for obj in CHOICE_CIERRE_1_2_PLANIFICADA:
        conteo = filtro.filter(cierremanejo2__campo2__contains=obj[0]).count()
        planificada_poda[obj[1]] = conteo

    realizada_poda = OrderedDict()
    for obj in CHOICE_CIERRE_1_2_REALIZADA:
        conteo = filtro.filter(cierremanejo2__campo3__contains=obj[0]).count()
        realizada_poda[obj[1]] = conteo

    resultado_poda = OrderedDict()
    for obj in CHOICE_CIERRE_1_2_RESULTADOS:
        conteo = filtro.filter(cierremanejo2__campo4__contains=obj[0]).count()
        resultado_poda[obj[1]] = conteo

    return render(request, template, locals())


def suelo_cierre(request, template="guiascacao/cierre/suelo_cierre.html"):
    filtro = _queryset_filtrado_cierre(request)
    numero_parcelas = filtro.count()

    impacto_suelo = OrderedDict()
    for obj in CHOICE_CIERRE_1_3_IMPACTO:
        conteo = filtro.filter(cierremanejo3__campo1__contains=obj[0]).count()
        impacto_suelo[obj[1]] = conteo

    planificada_suelo = OrderedDict()
    for obj in CHOICE_CIERRE_1_3_PLANIFICADA:
        conteo = filtro.filter(cierremanejo3__campo2__contains=obj[0]).count()
        planificada_suelo[obj[1]] = conteo

    realizada_suelo = OrderedDict()
    for obj in CHOICE_CIERRE_1_3_REALIZADA:
        conteo = filtro.filter(cierremanejo3__campo3__contains=obj[0]).count()
        realizada_suelo[obj[1]] = conteo

    resultado_suelo = OrderedDict()
    for obj in CHOICE_CIERRE_1_3_RESULTADOS:
        conteo = filtro.filter(cierremanejo3__campo4__contains=obj[0]).count()
        resultado_suelo[obj[1]] = conteo

    return render(request, template, locals())

def plaga_cierre(request, template="guiascacao/cierre/plaga_cierre.html"):
    filtro = _queryset_filtrado_cierre(request)
    numero_parcelas = filtro.count()

    impacto_plaga = OrderedDict()
    for obj in CHOICE_CIERRE_1_4_IMPACTO:
        conteo = filtro.filter(cierremanejo4__campo1__contains=obj[0]).count()
        impacto_plaga[obj[1]] = conteo

    planificada_plaga = OrderedDict()
    for obj in CHOICE_CIERRE_1_4_PLANIFICADA:
        conteo = filtro.filter(cierremanejo4__campo2__contains=obj[0]).count()
        planificada_plaga[obj[1]] = conteo

    realizada_plaga = OrderedDict()
    for obj in CHOICE_CIERRE_1_4_REALIZADA:
        conteo = filtro.filter(cierremanejo4__campo3__contains=obj[0]).count()
        realizada_plaga[obj[1]] = conteo

    resultado_plaga = OrderedDict()
    for obj in CHOICE_CIERRE_1_4_RESULTADOS:
        conteo = filtro.filter(cierremanejo4__campo4__contains=obj[0]).count()
        resultado_plaga[obj[1]] = conteo

    return render(request, template, locals())

def piso_cierre(request, template="guiascacao/cierre/piso_cierre.html"):
    filtro = _queryset_filtrado_cierre(request)
    numero_parcelas = filtro.count()

    impacto_piso = OrderedDict()
    for obj in CHOICE_CIERRE_1_5_IMPACTO:
        conteo = filtro.filter(cierremanejo5__campo1__contains=obj[0]).count()
        impacto_piso[obj[1]] = conteo

    planificada_piso = OrderedDict()
    for obj in CHOICE_CIERRE_1_5_PLANIFICADA:
        conteo = filtro.filter(cierremanejo5__campo2__contains=obj[0]).count()
        planificada_piso[obj[1]] = conteo

    realizada_piso = OrderedDict()
    for obj in CHOICE_CIERRE_1_5_REALIZADA:
        conteo = filtro.filter(cierremanejo5__campo3__contains=obj[0]).count()
        realizada_piso[obj[1]] = conteo

    resultado_piso = OrderedDict()
    for obj in CHOICE_CIERRE_1_5_RESULTADOS:
        conteo = filtro.filter(cierremanejo5__campo4__contains=obj[0]).count()
        resultado_piso[obj[1]] = conteo

    return render(request, template, locals())

def vivero_cierre(request, template="guiascacao/cierre/vivero_cierre.html"):
    filtro = _queryset_filtrado_cierre(request)
    numero_parcelas = filtro.count()

    impacto_viviero = OrderedDict()
    for obj in CHOICE_CIERRE_1_6_IMPACTO:
        conteo = filtro.filter(cierremanejo6__campo1__contains=obj[0]).count()
        impacto_viviero[obj[1]] = conteo

    planificada_viviero = OrderedDict()
    for obj in CHOICE_CIERRE_1_6_PLANIFICADA:
        conteo = filtro.filter(cierremanejo6__campo2__contains=obj[0]).count()
        planificada_viviero[obj[1]] = conteo

    realizada_viviero = OrderedDict()
    for obj in CHOICE_CIERRE_1_6_REALIZADA:
        conteo = filtro.filter(cierremanejo6__campo3__contains=obj[0]).count()
        realizada_viviero[obj[1]] = conteo

    resultado_viviero = OrderedDict()
    for obj in CHOICE_CIERRE_1_6_RESULTADOS:
        conteo = filtro.filter(cierremanejo6__campo4__contains=obj[0]).count()
        resultado_viviero[obj[1]] = conteo

    return render(request, template, locals())

def cosecha_cierre(request, template="guiascacao/cierre/cosecha_cierre.html"):
    filtro = _queryset_filtrado_cierre(request)
    numero_parcelas = filtro.count()

    impacto_cosecha = OrderedDict()
    for obj in CHOICE_CIERRE_1_7_IMPACTO:
        conteo = filtro.filter(cierremanejo7__campo1__contains=obj[0]).count()
        impacto_cosecha[obj[1]] = conteo

    planificada_cosecha = OrderedDict()
    for obj in CHOICE_CIERRE_1_7_PLANIFICADA:
        conteo = filtro.filter(cierremanejo7__campo2__contains=obj[0]).count()
        planificada_cosecha[obj[1]] = conteo

    realizada_cosecha = OrderedDict()
    for obj in CHOICE_CIERRE_1_7_REALIZADA:
        conteo = filtro.filter(cierremanejo7__campo3__contains=obj[0]).count()
        realizada_cosecha[obj[1]] = conteo

    resultado_cosecha = OrderedDict()
    for obj in CHOICE_CIERRE_1_7_RESULTADO:
        conteo = filtro.filter(cierremanejo7__campo4__contains=obj[0]).count()
        resultado_cosecha[obj[1]] = conteo

    return render(request, template, locals())

def calculos_costo_cierre(request, template="guiascacao/cierre/calculos_cierre.html"):
    filtro = _queryset_filtrado_cierre(request)
    numero_parcelas = filtro.count()

    costo_mano_obra = filtro.aggregate(costo=Avg('cierrecosto1__costo'))['costo'] or 0
    area_mz = filtro.aggregate(area=Sum('cierrecosto1__area'))['area'] or 0

    dict_actividades = OrderedDict()
    for obj in ActividadesCierre.objects.all():
        avg_familiar = filtro.filter(cierreactividad__actividad=obj).aggregate(familiar=Sum('cierreactividad__familiar'))['familiar'] or 0
        avg_contratada = filtro.filter(cierreactividad__actividad=obj).aggregate(contra=Sum('cierreactividad__contratada'))['contra'] or 0
        avg_costo = filtro.filter(cierreactividad__actividad=obj).aggregate(costo=Sum('cierreactividad__costo'))['costo'] or 0
        dict_actividades[obj] = [avg_familiar,avg_contratada,avg_costo]

    suma_familiar = sum(v[0] for k,v in dict_actividades.iteritems())
    suma_contradata = sum(v[1] for k,v in dict_actividades.iteritems())
    suma_costo = sum(v[2] for k,v in dict_actividades.iteritems())

    cosecha_baba = filtro.aggregate(valor=Sum('cierrebabaroja__campo1'))['valor'] or 0
    venta_baba = filtro.aggregate(valor=Sum('cierrebabaroja__campo2'))['valor'] or 0
    precio_baba = filtro.aggregate(valor=Avg('cierrebabaroja__campo3'))['valor'] or 0
    cosecha_rojo = filtro.aggregate(valor=Sum('cierrebabaroja__campo4'))['valor'] or 0
    venta_rojo = filtro.aggregate(valor=Sum('cierrebabaroja__campo5'))['valor'] or 0
    consumo_rojo = filtro.aggregate(valor=Sum('cierrebabaroja__campo7'))['valor'] or 0
    precio_rojo = filtro.aggregate(valor=Avg('cierrebabaroja__campo6'))['valor'] or 0

    try:
        gasto_mo_familiar = suma_familiar * costo_mano_obra
    except:
        pass
    try:
        gasto_mo_contratada = suma_contradata * costo_mano_obra
    except:
        pass
    try:
        gasto_efectivo = suma_costo + gasto_mo_contratada
    except:
        pass
    try:
        costo_produccion = gasto_efectivo + gasto_mo_familiar
    except:
        pass
    try:
        ingreso_venta = (venta_baba * precio_baba) + (venta_rojo * precio_rojo)
    except:
       pass
    try:
        consumo_familiar = consumo_rojo * precio_rojo
    except:
        pass
    try:
        ingreso_bruto = ingreso_venta + consumo_familiar
    except:
       pass
    try:
        ingreso_neto_parcial = ingreso_bruto - gasto_efectivo
    except:
       pass
    try:
        retorno_mo_familiar = float(ingreso_neto_parcial) / float(suma_familiar)
    except:
        pass
    try:
        ingreso_neto = ingreso_bruto - costo_produccion
    except:
       pass
    try:
        tasa_retorno_ciclo = (float(ingreso_neto) / float(costo_produccion)) * 100
    except:
        pass
    try:
        inversion_mz = float(costo_produccion) / float(area_mz)
    except:
       pass
    try:
        ingreso_neto_mz = ingreso_neto / area_mz
    except:
        pass
    try:
        costo_qq_baba = costo_produccion / float((cosecha_baba + (cosecha_rojo*3)))
    except:
        pass


    return render(request, template, locals())

def tablas_cierre(request, template="guiascacao/cierre/tablas_cierre.html"):
    filtro = _queryset_filtrado_cierre(request)
    numero_parcelas = filtro.count()

    tabla_cierre_manejo = OrderedDict()
    for obj in ManejosCierre.objects.all():
        cont_reposo = filtro.filter(cierremanejo__manejo=obj, cierremanejo__reposo=1).count()
        cont_crecimiento = filtro.filter(cierremanejo__manejo=obj, cierremanejo__crecimiento=1).count()
        cont_floracion = filtro.filter(cierremanejo__manejo=obj, cierremanejo__floracion=1).count()
        cont_cosecha = filtro.filter(cierremanejo__manejo=obj, cierremanejo__cosecha=1).count()
        tabla_cierre_manejo[obj] = [cont_reposo,cont_crecimiento,cont_floracion,cont_cosecha]

    tabla_variedad = OrderedDict()
    for obj in CHOICE_CIERRE_CONOCIMIENTO_TEMA1:
        cont_criollas = filtro.filter(cierreconocimiento1__tema=obj[0], cierreconocimiento1__criollas=1).count()
        cont_forastero = filtro.filter(cierreconocimiento1__tema=obj[0], cierreconocimiento1__forastero=1).count()
        cont_trinitaria = filtro.filter(cierreconocimiento1__tema=obj[0], cierreconocimiento1__trinitaria=1).count()
        cont_hibridos = filtro.filter(cierreconocimiento1__tema=obj[0], cierreconocimiento1__hibridos=1).count()
        cont_clones = filtro.filter(cierreconocimiento1__tema=obj[0], cierreconocimiento1__clones=1).count()
        tabla_variedad[obj[1]] = [cont_criollas,cont_forastero,cont_trinitaria,cont_hibridos,cont_clones]

    tabla_ventajas = OrderedDict()
    for obj in CHOICE_CIERRE_CONOCIMIENTO_RESPUESTAS:
        cont_criollas = filtro.filter(cierreconocimiento2__tema=1, cierreconocimiento2__criollas__contains=obj[0]).count()
        cont_forastero = filtro.filter(cierreconocimiento2__tema=1, cierreconocimiento2__forastero__contains=obj[0]).count()
        cont_trinitaria = filtro.filter(cierreconocimiento2__tema=1, cierreconocimiento2__trinitaria__contains=obj[0]).count()
        cont_hibridos = filtro.filter(cierreconocimiento2__tema=1, cierreconocimiento2__hibridos__contains=obj[0]).count()
        cont_clones = filtro.filter(cierreconocimiento2__tema=1, cierreconocimiento2__clones__contains=obj[0]).count()
        tabla_ventajas[obj[1]] = [cont_criollas,cont_forastero,cont_trinitaria,cont_hibridos,cont_clones]

    tabla_desventajas = OrderedDict()
    for obj in CHOICE_CIERRE_CONOCIMIENTO_RESPUESTAS3:
        cont_criollas = filtro.filter(cierreconocimiento3__tema=1, cierreconocimiento3__criollas__contains=obj[0]).count()
        cont_forastero = filtro.filter(cierreconocimiento3__tema=1, cierreconocimiento3__forastero__contains=obj[0]).count()
        cont_trinitaria = filtro.filter(cierreconocimiento3__tema=1, cierreconocimiento3__trinitaria__contains=obj[0]).count()
        cont_hibridos = filtro.filter(cierreconocimiento3__tema=1, cierreconocimiento3__hibridos__contains=obj[0]).count()
        cont_clones = filtro.filter(cierreconocimiento3__tema=1, cierreconocimiento3__clones__contains=obj[0]).count()
        tabla_desventajas[obj[1]] = [cont_criollas,cont_forastero,cont_trinitaria,cont_hibridos,cont_clones]

    tabla_suelo1 = OrderedDict()
    for obj in CHOICE_CIERRE_SUELO_RESPUESTAS1:
        cont_abono = filtro.filter(cierresuelo1__tema=1, cierresuelo1__abono__contains=obj[0]).count()
        cont_hojarasca = filtro.filter(cierresuelo1__tema=1, cierresuelo1__hojarasca__contains=obj[0]).count()
        cont_organico = filtro.filter(cierresuelo1__tema=1, cierresuelo1__organico__contains=obj[0]).count()
        tabla_suelo1[obj[1]] = [cont_abono,cont_hojarasca,cont_organico]

    tabla_suelo2 = OrderedDict()
    for obj in CHOICE_CIERRE_SUELO_RESPUESTAS2:
        cont_abono = filtro.filter(cierresuelo2__tema=1, cierresuelo2__abono__contains=obj[0]).count()
        cont_hojarasca = filtro.filter(cierresuelo2__tema=1, cierresuelo2__hojarasca__contains=obj[0]).count()
        cont_organico = filtro.filter(cierresuelo2__tema=1, cierresuelo2__organico__contains=obj[0]).count()
        tabla_suelo2[obj[1]] = [cont_abono,cont_hojarasca,cont_organico]

    tabla_suelo3 = OrderedDict()
    for obj in CHOICE_CIERRE_SUELO_RESPUESTAS3:
        cont_abono = filtro.filter(cierresuelo3__tema=1, cierresuelo3__abono__contains=obj[0]).count()
        cont_hojarasca = filtro.filter(cierresuelo3__tema=1, cierresuelo3__hojarasca__contains=obj[0]).count()
        cont_organico = filtro.filter(cierresuelo3__tema=1, cierresuelo3__organico__contains=obj[0]).count()
        tabla_suelo3[obj[1]] = [cont_abono,cont_hojarasca,cont_organico]

    tabla_plaga2 = OrderedDict()
    for obj in CHOICE_CIERRE_PLAGA_RESPUESTAS2:
        cont_monilla = filtro.filter(cierreplaga2__tema=1, cierreplaga2__monilla__contains=obj[0]).count()
        cont_mazorca = filtro.filter(cierreplaga2__tema=1, cierreplaga2__mazorca__contains=obj[0]).count()
        tabla_plaga2[obj[1]] = [cont_monilla,cont_mazorca]

    tabla_plaga22 = OrderedDict()
    for obj in CHOICE_CIERRE_PLAGA_RESPUESTAS_ZOMPOPO:
        cont_zompopos = filtro.filter(cierreplaga2__tema=1, cierreplaga2__zompopos__contains=obj[0]).count()
        tabla_plaga22[obj[1]] = [cont_zompopos]

    tabla_plaga3 = OrderedDict()
    for obj in CHOICE_CIERRE_PLAGA_RESPUESTAS3:
        cont_monilla = filtro.filter(cierreplaga3__tema=1, cierreplaga3__monilla__contains=obj[0]).count()
        cont_mazorca = filtro.filter(cierreplaga3__tema=1, cierreplaga3__mazorca__contains=obj[0]).count()
        tabla_plaga3[obj[1]] = [cont_monilla,cont_mazorca]

    tabla_plaga33 = OrderedDict()
    for obj in CHOICE_CIERRE_PLAGA_RESPUESTAS_ZOMPOPO3:
        cont_zompopos = filtro.filter(cierreplaga3__tema=1, cierreplaga3__zompopos__contains=obj[0]).count()
        tabla_plaga33[obj[1]] = [cont_zompopos]

    return render(request, template, locals())

def ciclo_trabajo_cierre(request, template="guiascacao/cierre/ciclo_trabajo_cierre.html"):
    filtro = _queryset_filtrado_cierre(request)
    numero_parcelas = filtro.count()

    pie_1 = OrderedDict()
    for obj in CHOICE_CIERRE_CICLO_TRABAJO1_RESPUESTA:
        conteo = filtro.filter(cierreciclotrabajo__pregunta1=obj[0]).count()
        pie_1[obj[1]] = conteo

    pie_2 = OrderedDict()
    for obj in CHOICE_CIERRE_CICLO_TRABAJO1_RESPUESTA:
        conteo = filtro.filter(cierreciclotrabajo__pregunta2=obj[0]).count()
        pie_2[obj[1]] = conteo

    pie_3 = OrderedDict()
    for obj in CHOICE_CIERRE_CICLO_TRABAJO1_RESPUESTA:
        conteo = filtro.filter(cierreciclotrabajo__pregunta3=obj[0]).count()
        pie_3[obj[1]] = conteo

    pie_4 = OrderedDict()
    for obj in CHOICE_CIERRE_CICLO_TRABAJO2_RESPUESTA:
        conteo = filtro.filter(cierreciclotrabajo__pregunta4=obj[0]).count()
        pie_4[obj[1]] = conteo

    pie_5 = OrderedDict()
    for obj in CHOICE_CIERRE_CICLO_TRABAJO3_RESPUESTA:
        conteo = filtro.filter(cierreciclotrabajo__pregunta5=obj[0]).count()
        pie_5[obj[1]] = conteo

    pie_6 = OrderedDict()
    for obj in CHOICE_CIERRE_CICLO_TRABAJO4_RESPUESTA:
        conteo = filtro.filter(cierreciclotrabajo__pregunta6=obj[0]).count()
        pie_6[obj[1]] = conteo

    pie_7 = OrderedDict()
    for obj in CHOICE_CIERRE_CICLO_TRABAJO5_RESPUESTA:
        conteo = filtro.filter(cierreciclotrabajo__pregunta7=obj[0]).count()
        pie_7[obj[1]] = conteo

    pie_8 = OrderedDict()
    for obj in CHOICE_SI_NO:
        conteo = filtro.filter(cierreciclotrabajo__pregunta8=obj[0]).count()
        pie_8[obj[1]] = conteo


    return render(request, template, locals())

#fin de salidas de cierre
#------------------------- entradas de saf --------------------------
def _queryset_filtrado_saf(request):
    params = {}

    if 'fecha' in request.session:
        params['fecha_visita__year'] = request.session['fecha']

    if 'productor' in request.session:
        params['productor__nombre'] = request.session['productor']

    if 'organizacion' in request.session:
        params['productor__productor__organizacion'] = request.session['organizacion']

    if 'pais' in request.session:
        params['productor__pais'] = request.session['pais']

    if 'departamento' in request.session:
        params['productor__departamento'] = request.session['departamento']

    if 'municipio' in request.session:
        params['productor__municipio'] = request.session['municipio']

    if 'comunidad' in request.session:
        params['productor__comunidad'] = request.session['comunidad']

    if 'sexo' in request.session:
        params['productor__sexo'] = request.session['sexo']

    if 'tipologia' in request.session:
        params['productor__productor__tipologia'] = request.session['tipologia']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]

    return FichaSaf.objects.filter(**params)


def objetivos_saf(request, template='guiascacao/saf/objetivos.html'):
    filtro = _queryset_filtrado_saf(request)
    numero_parcelas = filtro.count()

    saf_conversacion1 = OrderedDict()
    for obj in CHOICE_SAF_1_1:
        conteo = filtro.filter(safconversacion1__conversacion1__contains=obj[0]).count()
        saf_conversacion1[obj[1]] = conteo

    safconversacion1_total = sum([v for k,v in saf_conversacion1.items()])

    saf_conversacion2 = OrderedDict()
    for obj in CHOICE_SAF_1_2:
        conteo = filtro.filter(safconversacion1__conversacion2__contains=obj[0]).count()
        saf_conversacion2[obj[1]] = conteo

    safconversacion2_total = sum([v for k,v in saf_conversacion2.items()])


    return render(request, template, locals())

def clima_saf(request, template='guiascacao/saf/clima.html'):
    filtro = _queryset_filtrado_saf(request)
    numero_parcelas = filtro.count()

    saf_conversacion3 = OrderedDict()
    for obj in CHOICE_COSECHA_9_MESES:
        saf_conversacion3[obj[1]] = OrderedDict()
        for x in CHOICE_SAF_1_3:
            conteo = filtro.filter(safconversacion2__conversacion3=obj[0],safconversacion2__conversacion4=x[0]).count()
            saf_conversacion3[obj[1]][x[1]] = conteo

    saf_conversacion4 = OrderedDict()
    for obj in CHOICE_COSECHA_9_MESES:
        saf_conversacion4[obj[1]] = OrderedDict()
        for x in CHOICE_SAF_1_4:
            conteo = filtro.filter(safconversacion3__conversacion3=obj[0],safconversacion3__conversacion4=x[0]).count()
            saf_conversacion4[obj[1]][x[1]] = conteo


    grafo_momento = OrderedDict()
    for obj in CHOICE_SAF_1_5:
        ene = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='A').count()
        feb = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='B').count()
        mar = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='C').count()
        abr = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='D').count()
        may = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='E').count()
        jun = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='F').count()
        jul = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='G').count()
        ago = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='H').count()
        sep = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='I').count()
        octu = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='J').count()
        nov = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='K').count()
        dic = filtro.filter(safconversacion4__conversacion5=obj[0],
                                         safconversacion4__conversacion6__contains='L').count()
        grafo_momento[obj[1]] = [ene,feb,mar,abr,may,jun,jul,ago,sep,octu,nov,dic]

    return render(request, template, locals())

def condiciones_saf(request, template='guiascacao/saf/condiciones.html'):
    filtro = _queryset_filtrado_saf(request)
    numero_parcelas = filtro.count()

    grafo_topografia = OrderedDict()
    for obj in CHOICE_SAF_1_5_TOPOGRAFIA:
        conteo = filtro.filter(safconversacion5__conversacion7=obj[0]).count()
        grafo_topografia[obj[1]] = conteo

    grafo_fertilidad = OrderedDict()
    for obj in CHOICE_SAF_1_5_FERTILIDAD:
        conteo = filtro.filter(safconversacion5__conversacion8=obj[0]).count()
        grafo_fertilidad[obj[1]] = conteo

    tabla_maderable = OrderedDict()
    for obj in CHOICE_SAF_1_6_MADERABLE:
        conteo = filtro.filter(safconversacion6__conversacion9__contains=obj[0]).count()
        tabla_maderable[obj[1]] = conteo

    tabla_frutales = OrderedDict()
    for obj in CHOICE_SAF_1_6_FRUTALES:
        conteo = filtro.filter(safconversacion6__conversacion10__contains=obj[0]).count()
        tabla_frutales[obj[1]] = conteo

    tabla_servicios = OrderedDict()
    for obj in CHOICE_SAF_1_6_SERVICIOS:
        conteo = filtro.filter(safconversacion6__conversacion11__contains=obj[0]).count()
        tabla_servicios[obj[1]] = conteo

    return render(request, template, locals())


def sombra_saf(request, template='guiascacao/saf/sombra.html'):
    filtro = _queryset_filtrado_saf(request)
    numero_parcelas = filtro.count()

    tabla_momento = OrderedDict()
    for obj in CHOICE_SAF_1_6_ETAPA:
        ene = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='A').count()
        feb = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='B').count()
        mar = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='C').count()
        abr = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='D').count()
        may = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='E').count()
        jun = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='F').count()
        jul = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='G').count()
        ago = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='H').count()
        sep = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='I').count()
        octu = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='J').count()
        nov = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='K').count()
        dic = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion13__contains='L').count()
        tabla_momento[obj[1]] = [ene,feb,mar,abr,may,jun,jul,ago,sep,octu,nov,dic]

    tabla_momento2 = OrderedDict()
    for obj in CHOICE_SAF_1_6_ETAPA:
        sin_sombra = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion14=1).count()
        poca_sombra = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion14=2).count()
        media_sombra = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion14=3).count()
        mucha_sombra = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion14=4).count()
        tabla_momento2[obj[1]] = [sin_sombra,poca_sombra,media_sombra,mucha_sombra]

    tabla_momento3 = OrderedDict()
    for obj in CHOICE_SAF_1_6_ETAPA:
        sin_sombra = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion14=1).count()
        poca_sombra = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion14=2).count()
        media_sombra = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion14=3).count()
        mucha_sombra = filtro.filter(safconversacion7__conversacion12=obj[0],
                                         safconversacion7__conversacion14=4).count()
        tabla_momento3[obj[1]] = [sin_sombra,poca_sombra,media_sombra,mucha_sombra]

    tabla_momento4 = OrderedDict()
    for obj in CHOICE_SAF_1_7_PROBLEMAS:
        poca_sombra = filtro.filter(safconversacion8__conversacion15=obj[0],
                                         safconversacion8__conversacion16=1).count()
        mucha_sombra = filtro.filter(safconversacion8__conversacion15=obj[0],
                                         safconversacion8__conversacion16=2).count()
        tabla_momento4[obj[1]] = [poca_sombra,mucha_sombra]

    return render(request, template, locals())

def semilla_saf(request, template='guiascacao/saf/semilla.html'):
    filtro = _queryset_filtrado_saf(request)
    numero_parcelas = filtro.count()

    grafo_fuente_semilla = OrderedDict()
    for obj in CHOICE_SAF_1_8:
        conteo = filtro.filter(safconversacion9__conversacion17=obj[0]).count()
        grafo_fuente_semilla[obj[1]] = conteo

    tabla_semilla_cacao = OrderedDict()
    for obj in CHOICE_SAF_1_9:
        conteo_1 = filtro.filter(safconversacion9__conversacion18__contains=obj[0]).count()
        tabla_semilla_cacao[obj[1]] = conteo_1

    tabla_semilla_cacao2 = OrderedDict()
    for obj in CHOICE_SAF_1_11:
        conteo_2 = filtro.filter(safconversacion9__conversacion19__contains=obj[0]).count()
        conteo_3 = filtro.filter(safconversacion9__conversacion20__contains=obj[0]).count()
        tabla_semilla_cacao2[obj[1]] = [conteo_2,conteo_3]

    return render(request, template, locals())

def calidad_saf(request, template='guiascacao/saf/calidad.html'):
    filtro = _queryset_filtrado_saf(request)
    numero_parcelas = filtro.count()

    grafo_dispercion = []
    for obj in filtro:
        suma_observaciones = SafObservaciones.objects.filter(ficha=obj).values_list('observacion2',
                                                                                                                                            'observacion3',
                                                                                                                                            'observacion4',
                                                                                                                                            'observacion5')
        if len(suma_observaciones) >= 1:
            suma_total = (sum(suma_observaciones[0]) / float(4))
            grafo_dispercion.append(suma_total)

    grafo_barra = OrderedDict()
    for obj in CHOICE_SAF_2_OPCIONES:
        conteo_1 = filtro.filter(safobservaciones2__observacion1=1, safobservaciones2__observacion2=obj[0]).count()
        conteo_2 = filtro.filter(safobservaciones2__observacion1=1, safobservaciones2__observacion3=obj[0]).count()
        conteo_3 = filtro.filter(safobservaciones2__observacion1=1, safobservaciones2__observacion4=obj[0]).count()
        conteo_4 = filtro.filter(safobservaciones2__observacion1=1, safobservaciones2__observacion5=obj[0]).count()
        total = conteo_1 + conteo_2 + conteo_3 + conteo_4
        grafo_barra[obj[1]] = total

    return render(request, template, locals())

def disenio_saf_saf(request, template='guiascacao/saf/disenio.html'):
    filtro = _queryset_filtrado_saf(request)
    numero_parcelas = filtro.count()

    grafo_suelo = OrderedDict()
    for obj in CHOICE_SAF_OBSERVACION_2_2:
        conteo = filtro.filter(safobservaciones3__observacion6=obj[0]).count()
        grafo_suelo[obj[1]] = conteo

    grafo_practicas = OrderedDict()
    for obj in CHOICE_SAF_OBSERVACION_2_3:
        conteo = filtro.filter(safobservaciones3__observacion7__contains=obj[0]).count()
        grafo_practicas[obj[1]] = conteo

    grafo_arreglo = OrderedDict()
    for obj in CHOICE_SAF_OBSERVACION_2_5:
        conteo = filtro.filter(safobservaciones4__observacion8=obj[0]).count()
        grafo_arreglo[obj[1]] = conteo

    grafo_dificultad = OrderedDict()
    for obj in CHOICE_SAF_OBSERVACION_2_6:
        conteo = filtro.filter(safobservaciones4__observacion9=obj[0]).count()
        grafo_dificultad[obj[1]] = conteo

    grafo_mejor = OrderedDict()
    for obj in CHOICE_SAF_OBSERVACION_2_7:
        conteo = filtro.filter(safobservaciones4__observacion10=obj[0]).count()
        grafo_mejor[obj[1]] = conteo


    return render(request, template, locals())
#fin salidas de saf
# ---------------------------- COMIENZA SALIDAS DE VIVERO
def _queryset_filtrado_vivero(request):
    params = {}

    if 'fecha' in request.session:
        params['fecha_visita__year'] = request.session['fecha']

    if 'productor' in request.session:
        params['productor__nombre'] = request.session['productor']

    if 'organizacion' in request.session:
        params['productor__productor__organizacion'] = request.session['organizacion']

    if 'pais' in request.session:
        params['productor__pais'] = request.session['pais']

    if 'departamento' in request.session:
        params['productor__departamento'] = request.session['departamento']

    if 'municipio' in request.session:
        params['productor__municipio'] = request.session['municipio']

    if 'comunidad' in request.session:
        params['productor__comunidad'] = request.session['comunidad']

    if 'sexo' in request.session:
        params['productor__sexo'] = request.session['sexo']

    if 'tipologia' in request.session:
        params['productor__productor__tipologia'] = request.session['tipologia']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]

    return FichaVivero.objects.filter(**params)

#ahora si las salidas

def conversaciones_vivero(request, template='guiascacao/vivero/conversaciones.html'):
    filtro = _queryset_filtrado_vivero(request)
    numero_parcelas = filtro.count()

    grafo_meses = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_1:
        conteo = filtro.filter(vivieroconversacion__conversacion1__contains=obj[0]).count()
        grafo_meses[obj[1]] = conteo

    grafo_razones = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_2:
        conteo = filtro.filter(vivieroconversacion__conversacion2__contains=obj[0]).count()
        grafo_razones[obj[1]] = conteo

    grafo_caracteristicas = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_3:
        conteo = filtro.filter(vivieroconversacion__conversacion3__contains=obj[0]).count()
        grafo_caracteristicas[obj[1]] = conteo

    grafo_preparar = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_4:
        conteo = filtro.filter(vivieroconversacion__conversacion4__contains=obj[0]).count()
        grafo_preparar[obj[1]] = conteo

    grafo_desinfecta = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_5:
        conteo = filtro.filter(vivieroconversacion__conversacion5__contains=obj[0]).count()
        grafo_desinfecta[obj[1]] = conteo

    grafo_sustrato = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_6:
        conteo = filtro.filter(vivieroconversacion__conversacion6=obj[0]).count()
        grafo_sustrato[obj[1]] = conteo


    return render(request, template, locals())

def conversaciones_dos_vivero(request, template='guiascacao/vivero/conversaciones_dos.html'):
    filtro = _queryset_filtrado_vivero(request)
    numero_parcelas = filtro.count()

    grafo_bolsa = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_7:
        conteo = filtro.filter(viveroconversacion2__conversacion7=obj[0]).count()
        grafo_bolsa[obj[1]] = conteo

    grafo_semilla = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_8:
        conteo = filtro.filter(viveroconversacion2__conversacion8=obj[0]).count()
        grafo_semilla[obj[1]] = conteo

    grafo_sitio = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_9:
        conteo = filtro.filter(viveroconversacion2__conversacion9__contains=obj[0]).count()
        grafo_sitio[obj[1]] = conteo

    grafo_injerto = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_10:
        conteo = filtro.filter(viveroconversacion2__conversacion10__contains=obj[0]).count()
        grafo_injerto[obj[1]] = conteo

    lista = filtro.values_list('viveroconversacion2__conversacion11', flat=True)
    grafo_procedimiento = crear_rangos(request, lista, 0, 100, 26)

    dicc_mantiene = {'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
    grafo_mantiene_vivero = OrderedDict()
    for k,v in dicc_mantiene.items():
        conteo = filtro.filter(viveroconversacion2__conversacion13=v).count()
        grafo_mantiene_vivero[k] = conteo

    tabla_vareta = OrderedDict()
    for obj in CHOICE_VIVERO_CONVERSACION_12:
        conteo = filtro.filter(viveroconversacion2__conversacion12__contains=obj[0]).count()
        tabla_vareta[obj[1]] = conteo

    tabla_semilla = OrderedDict()
    for obj in CHOICE_VIVERO_NUEVO_CONVERSACION2:
        conteo = filtro.filter(viveroconversacion2__conversacion14=obj[0]).count()
        tabla_semilla[obj[1]] = conteo

    return render(request, template, locals())

def observacion_vivero(request, template='guiascacao/vivero/observacion.html'):
    filtro = _queryset_filtrado_vivero(request)
    numero_parcelas = filtro.count()

    cantidad_planta = filtro.values_list('vivieroobservacion1__observacion1', flat=True)
    try:
        cantidad_planta_promedio = np.mean(cantidad_planta)
    except:
        pass
    try:
        cantidad_planta_mediano = np.median(cantidad_planta)
    except:
        pass
    try:
        cantidad_planta_minimo = min(cantidad_planta)
    except:
        pass
    try:
        cantidad_planta_maximo = max(cantidad_planta)
    except:
        pass
    try:
        cantidad_planta_desviacion = np.std(cantidad_planta)
    except:
        pass

    edad_planta = filtro.values_list('vivieroobservacion1__observacion2', flat=True)
    try:
        edad_planta_promedio = np.mean(edad_planta)
    except:
        pass
    try:
        edad_planta_medianp = np.median(edad_planta)
    except:
        pass
    try:
        edad_planta_minimo = min(edad_planta)
    except:
        pass
    try:
        edad_planta_maximo = max(edad_planta)
    except:
        pass
    try:
        edad_planta_desviacion = np.std(edad_planta)
    except:
        pass

    fuente_semilla = OrderedDict()
    for obj in CHOICER_VIVIERO_FUENTE_SEMILLA:
        conteo = filtro.filter(vivieroobservacion1__observacion3=obj[0]).count()
        fuente_semilla[obj[1]] = conteo

    dicc_plagas = OrderedDict()
    for obj in CHOICE_VIVERO_PLAGAS_ENFERMEDADES:
        datos = filtro.filter(vivieroobservacion2__observacion3=obj[0]).values_list('vivieroobservacion2__total_si', flat=True)
        try:
            dicc_plagas[obj[1]] = [len(datos),np.mean(datos),np.median(datos),min(datos),max(datos),np.std(datos)]
        except:
            pass

    return render(request, template, locals())

def analisis_vivero(request, template='guiascacao/vivero/analisis.html'):
    filtro = _queryset_filtrado_vivero(request)
    numero_parcelas = filtro.count()

    grafo_semilla = OrderedDict()
    for obj in CHOICE_VIVERO_ANALISIS_1:
        conteo = filtro.filter(vivieroanalisissituacion__analisis1__contains=obj[0]).count()
        grafo_semilla[obj[1]] = conteo

    grafo_plantas = OrderedDict()
    for obj in CHOICE_VIVERO_ANALISIS_2:
        conteo = filtro.filter(vivieroanalisissituacion__analisis2__contains=obj[0]).count()
        grafo_plantas[obj[1]] = conteo

    grafo_plagas = OrderedDict()
    for obj in CHOICE_VIVERO_ANALISIS_3:
        conteo = filtro.filter(vivieroanalisissituacion__analisis3__contains=obj[0]).count()
        grafo_plagas[obj[1]] = conteo

    grafo_acciones = OrderedDict()
    for obj in CHOICE_VIVERO_ANALISIS_4:
        conteo = filtro.filter(vivieroanalisissituacion__analisis4__contains=obj[0]).count()
        grafo_acciones[obj[1]] = conteo

    return render(request, template, locals())

#----------  funciones utilitarias --------------------------

def crear_rangos(request, lista, start=0, stop=0, step=0):
    dict_algo = OrderedDict()
    rangos = []
    contador = 0
    rangos = [(n, n+int(step)-1) for n in range(int(start), int(stop), int(step))]

    for desde, hasta in rangos:
        dict_algo['%s a %s' % (desde,hasta)] = len([x for x in lista if desde <= x <= hasta])

    return dict_algo


def get_productor(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        personas = Persona.objects.filter(nombre__icontains = q, tipo_persona=1 )[:10]
        #print personas
        results = []
        for person in personas:
            personas_json = {}
            personas_json['id'] = person.id
            personas_json['label'] = person.nombre
            personas_json['value'] = person.nombre
            results.append(personas_json)
    else:
        results = 'fail'
    return HttpResponse(simplejson.dumps(results), content_type='application/json')
