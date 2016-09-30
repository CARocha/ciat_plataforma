# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from .forms import *
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

# ficha registro de gastos ------------------------------------------------
class InlineTablaGastos(admin.TabularInline):
    model = TablaGastos
    extra = 1

class GastosAdmin(admin.ModelAdmin):
    list_display = ('productor', 'fecha_siembra')

    # form = ProductorMonitoreoAdminForm

    inlines = [InlineTablaGastos]

    class Media:
        js = ('granos_basicos/js/jquery-2.2.1.min.js','granos_basicos/js/select2.min.js',
                'granos_basicos/js/global.js',)
        css = {
            'all': ('granos_basicos/css/select2.min.css',)
            }

admin.site.register(Gastos,GastosAdmin)

class InlineLiga_Nested(NestedTabularInline):
    model = Liga_Nested
    extra = 1

class InlineTablaInsumos(NestedTabularInline):
    model = TablaInsumos
    extra = 1
    inlines = [InlineLiga_Nested]

class InsumosAdmin(NestedModelAdmin):
    list_display = ('productor', 'fecha_siembra',)

    inlines = [InlineTablaInsumos]

    class Media:
        js = ('granos_basicos/js/jquery-2.2.1.min.js','granos_basicos/js/select2.min.js',
                'granos_basicos/js/global.js',)
        css = {
            'all': ('granos_basicos/css/select2.min.css',)
            }

    # form = InsumosAdminForm

admin.site.register(Insumos,InsumosAdmin)

#ficha Toma de decisiones --------------------------------------------------
class InlineTablaDecisiones(admin.TabularInline):
    model = TablaDecisiones
    extra = 1

class TomaDecisionesAdmin(admin.ModelAdmin):
    list_display = ('productor',)

    # form = ProductorMonitoreoAdminForm

    inlines = [InlineTablaDecisiones]

    class Media:
        js = ('granos_basicos/js/jquery-2.2.1.min.js','granos_basicos/js/select2.min.js',
                'granos_basicos/js/global.js',)
        css = {
            'all': ('granos_basicos/css/select2.min.css',)
            }

admin.site.register(TomaDecisiones,TomaDecisionesAdmin)

#ficha monitoreo #1 ---------------------------------------------------------
class InlineDatosMonitoreo(admin.TabularInline):
    model = DatosMonitoreo
    extra = 1

# class InlineDatosParcela(admin.StackedInline):
#     model = DatosParcela
#     max_num = 1
#     can_delete = False
#
#     fields = (
#             ('nombre', 'edad_parcela'),
#             ('latitud', 'longitud', 'direccion_viento'),
#             ('percepcion_fertilidad','tamano_parcela','profundidad_capa'),
#             ('acceso_agua', 'fuente_agua', 'distancia'),
#         )

class InlineDistribucionPendiente(admin.TabularInline):
    model = DistribucionPendiente
    max_num = 2
    extra = 1

class InlineRecursosSiembra(admin.TabularInline):
    model = RecursosSiembra
    extra = 1
    max_num = 2

class InlineHistorialRendimiento(admin.TabularInline):
    model = HistorialRendimiento
    extra = 1

class InlineSemillas(admin.TabularInline):
    model = Semillas
    extra = 1

class InlineProcedenciaSemilla(admin.TabularInline):
    model = ProcedenciaSemilla
    extra = 1
    max_num = 2

class InlinePruebaGerminacion(admin.TabularInline):
    model = PruebaGerminacion
    extra = 1
    max_num = 2

class InlineSuelo(admin.TabularInline):
    model = Suelo
    extra = 1
    max_num = 21

class InlineMacrofauna(admin.TabularInline):
    model = Macrofauna
    extra = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        kwargs['queryset'] = Especies.objects.filter(tipo=3)
        return super(InlineMacrofauna, self).formfield_for_foreignkey(db_field, request, **kwargs)

class InlineMonitoreoMalezas(admin.TabularInline):
    model = MonitoreoMalezas
    extra = 1
    max_num = 5

class InlineTablaMalezas(admin.TabularInline):
    model = TablaMalezas
    extra = 1
    max_num = 3

class InlineVigorFrijol(admin.TabularInline):
    model = VigorFrijol
    extra = 1
    max_num = 3

class InlineVigorMaiz(admin.TabularInline):
    model = VigorMaiz
    extra = 1
    max_num = 3

class InlinePoblacionFrijol(admin.TabularInline):
    model = PoblacionFrijol
    max_num = 1
    can_delete = False

class InlinePoblacionMaiz(admin.TabularInline):
    model = PoblacionMaiz
    max_num = 1
    can_delete = False

class InlinePlagasFrijol(admin.TabularInline):
    model = PlagasFrijol
    extra = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        kwargs['queryset'] = Especies.objects.filter(tipo=1,rubro__in=[2,3])
        return super(InlinePlagasFrijol, self).formfield_for_foreignkey(db_field, request, **kwargs)

class InlinePlagasMaiz(admin.TabularInline):
    model = PlagasMaiz
    extra = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        kwargs['queryset'] = Especies.objects.filter(tipo=1,rubro__in=[1,3])
        return super(InlinePlagasMaiz, self).formfield_for_foreignkey(db_field, request, **kwargs)

class InlineEnfermedadesFrijol(admin.TabularInline):
    model = EnfermedadesFrijol
    extra = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        kwargs['queryset'] = Especies.objects.filter(tipo=2,rubro__in=[2,3])
        return super(InlineEnfermedadesFrijol, self).formfield_for_foreignkey(db_field, request, **kwargs)

class InlineEnfermedadesMaiz(admin.TabularInline):
    model = EnfermedadesMaiz
    extra = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        kwargs['queryset'] = Especies.objects.filter(tipo=2,rubro__in=[1,3])
        return super(InlineEnfermedadesMaiz, self).formfield_for_foreignkey(db_field, request, **kwargs)

class InlineEstimadoCosechaFrijol(admin.TabularInline):
    model = EstimadoCosechaFrijol
    extra = 1
    max_num = 5

class InlineGranosPlanta(admin.TabularInline):
    model = GranosPlanta
    max_num = 1
    can_delete = False

class InlineEstimadoCosechaMaiz(admin.TabularInline):
    model = EstimadoCosechaMaiz
    extra = 1
    max_num = 3

class InlineEstimadoCosechaMaiz2(admin.TabularInline):
    model = EstimadoCosechaMaiz2
    extra = 1
    max_num = 3

class InlineSobreCosecha(admin.TabularInline):
    model = SobreCosecha
    extra = 1
    max_num = 2

class InlineCuradoSemilla(admin.TabularInline):
    model = CuradoSemilla
    max_num = 1
    can_delete = False

class VisitasAdmin(admin.ModelAdmin):
    list_display = ('productor','visita','fecha')
    list_filter = ('visita',)
    search_fields = ('productor',)
    date_hierarchy = 'fecha'

    # form = VisitasAdminForm

    inlines = [
                InlineSemillas,
                InlineProcedenciaSemilla,InlinePruebaGerminacion,InlineSuelo,
                InlineMacrofauna,InlineMonitoreoMalezas,InlineTablaMalezas,
                InlineVigorFrijol,InlineVigorMaiz,InlinePlagasFrijol,InlinePlagasMaiz,
                InlineEnfermedadesFrijol,InlineEnfermedadesMaiz,InlinePoblacionFrijol,
                InlinePoblacionMaiz,InlineEstimadoCosechaFrijol,
                InlineGranosPlanta,InlineEstimadoCosechaMaiz,InlineEstimadoCosechaMaiz2,
                InlineSobreCosecha,InlineCuradoSemilla
                ]
    class Media:
        js = ('granos_basicos/js/jquery-2.2.1.min.js','granos_basicos/js/select2.min.js',
                'granos_basicos/js/admin_visita.js',)
        css = {
            'all': ('granos_basicos/css/select2.min.css','granos_basicos/css/admin.css',)
            }

admin.site.register(Visitas,VisitasAdmin)

class MonitoreoAdmin(admin.ModelAdmin):
    list_display = ('productor','cultivo','ciclo_productivo','annio','nombre_parcela')
    search_fields = ('productor',)
    # date_hierarchy = 'fecha_monitoreo'

    form = MonitoreoAdminForm

    inlines = [InlineDatosMonitoreo,InlineDistribucionPendiente,
                InlineRecursosSiembra,InlineHistorialRendimiento,
                ]

    fieldsets = (
            (None, {'fields' : (('productor','cultivo','ciclo_productivo','annio'),)}),
            ('DATOS DE LA PARCELA', {'fields' : (('nombre_parcela','edad_parcela'),
                                                ('latitud','longitud','direccion_viento'),
                                                ('percepcion_fertilidad','tamano_parcela','profundidad_capa'),
                                                ('acceso_agua','fuente_agua','distancia'),
            )}),
    )

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        kwargs['queryset'] = Persona.objects.filter(tipo_persona=1,productor__proyecto__corto='Herramienta granos básicos')
        return super(MonitoreoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = ('granos_basicos/js/admin_monitoreo.js',)
        css = {
            'all': ('granos_basicos/css/admin.css',)
            }

admin.site.register(Monitoreo,MonitoreoAdmin)
admin.site.register(ParametrosSuelo)
admin.site.register(TiposMalezas)
admin.site.register(TratamientoSemilla)
admin.site.register(Productos)

class InlineFotosEspecies(admin.TabularInline):
    model = FotosEspecies
    extra = 1

class EspeciesAdmin(admin.ModelAdmin):
    list_display = ('nombre_popular','nombre_cientifico','tipo','rubro')
    inlines = [InlineFotosEspecies]

    class Media:
        js = ('granos_basicos/js/especies.js',)

admin.site.register(Especies,EspeciesAdmin)
