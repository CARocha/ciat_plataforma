from django.contrib import admin
from .models import *


class OrganizacionesAdmin(admin.ModelAdmin):
    list_display = ('id','siglas','nombre','area_accion','sitio_accion','plataforma','sector')
    list_display_links = ('id','siglas','nombre')

class InlineTimeLineProyecto(admin.TabularInline):
    model = TimeLineProyecto
    extra = 1


class ProyectosAdmin(admin.ModelAdmin):
    filter_horizontal = ("alianza","influencia","socias","temas")
    list_display = ('nombre', 'corto', 'codigo', 'inicio', 'finalizacion')
    inlines = [InlineTimeLineProyecto]

class InlineProductor(admin.TabularInline):
    model = Productor
    extra = 1
    max_num = 1

class InlineLideres(admin.TabularInline):
    model = Lideres
    extra = 1
    max_num = 1

class InlineTecnicoEspInvestigador(admin.TabularInline):
    model = TecnicoEspInvestigador
    extra = 1
    max_num = 1

class InlineDecisor(admin.TabularInline):
    model = Decisor
    extra = 1
    max_num = 1

class InlineProductorGranosBasicos(admin.TabularInline):
    model = ProductorGranosBasicos
    extra = 1
    max_num = 1

class InlineUsoSuelo(admin.TabularInline):
    model = UsoSuelo
    extra = 1
    max_num = 6

class InlineComposicionFamiliar(admin.TabularInline):
    model = ComposicionFamiliar
    extra = 1
    max_num = 15

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('tipo_persona', 'nombre', 'sexo', 'pais')

    inlines = [InlineProductor, InlineLideres, InlineTecnicoEspInvestigador,
                InlineDecisor,InlineProductorGranosBasicos,InlineUsoSuelo,
                InlineComposicionFamiliar]

    class Media:
        js = ('/static/general/js/personaAdmin.js',
                '/static/mapeo/js/granos_basicos.js'
                )


# Register your models here.
admin.site.register(Organizaciones, OrganizacionesAdmin)
admin.site.register(Persona, PersonaAdmin)
#modelos utilitarios
admin.site.register(Proyectos, ProyectosAdmin)
admin.site.register(RubrosAgropecuarios)
admin.site.register(RubrosNoAgropecuarios)
admin.site.register(FuenteManoObra)
admin.site.register(FormaAtencion)
admin.site.register(Especialidades)
admin.site.register(Accionar)
admin.site.register(CampoAccion)
admin.site.register(Temas)
admin.site.register(TiposProyectos)
