# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CierreBabaRoja'
        db.create_table(u'guias_cacao_cierrebabaroja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campo1', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('campo2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('campo3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('campo4', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('campo5', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('campo6', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('campo7', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ficha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['guias_cacao.FichaCierre'])),
        ))
        db.send_create_signal(u'guias_cacao', ['CierreBabaRoja'])

        # Adding field 'ViveroConversacion2.conversacion13'
        db.add_column(u'guias_cacao_viveroconversacion2', 'conversacion13',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ViveroConversacion2.conversacion14'
        db.add_column(u'guias_cacao_viveroconversacion2', 'conversacion14',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'CierreManejo2.campo4'
        db.add_column(u'guias_cacao_cierremanejo2', 'campo4',
                      self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=7, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CierreManejo3.campo4'
        db.add_column(u'guias_cacao_cierremanejo3', 'campo4',
                      self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CierreManejo1.campo4'
        db.add_column(u'guias_cacao_cierremanejo1', 'campo4',
                      self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CierreManejo6.campo4'
        db.add_column(u'guias_cacao_cierremanejo6', 'campo4',
                      self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=7, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CierreManejo7.campo4'
        db.add_column(u'guias_cacao_cierremanejo7', 'campo4',
                      self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9, null=True, blank=True),
                      keep_default=False)


        # Changing field 'CierreManejo7.campo1'
        db.alter_column(u'guias_cacao_cierremanejo7', 'campo1', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=13))
        # Adding field 'CierreManejo4.campo4'
        db.add_column(u'guias_cacao_cierremanejo4', 'campo4',
                      self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=7, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CierreManejo5.campo4'
        db.add_column(u'guias_cacao_cierremanejo5', 'campo4',
                      self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9, null=True, blank=True),
                      keep_default=False)


        # Changing field 'CierreManejo5.campo1'
        db.alter_column(u'guias_cacao_cierremanejo5', 'campo1', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=13))

        # Changing field 'CierreManejo5.campo2'
        db.alter_column(u'guias_cacao_cierremanejo5', 'campo2', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=15))

        # Changing field 'CierreManejo5.campo3'
        db.alter_column(u'guias_cacao_cierremanejo5', 'campo3', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=15))

        # Changing field 'CierreConocimiento3.trinitaria'
        db.alter_column(u'guias_cacao_cierreconocimiento3', 'trinitaria', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreConocimiento3.criollas'
        db.alter_column(u'guias_cacao_cierreconocimiento3', 'criollas', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreConocimiento3.forastero'
        db.alter_column(u'guias_cacao_cierreconocimiento3', 'forastero', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreConocimiento3.hibridos'
        db.alter_column(u'guias_cacao_cierreconocimiento3', 'hibridos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreConocimiento3.clones'
        db.alter_column(u'guias_cacao_cierreconocimiento3', 'clones', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreConocimiento2.trinitaria'
        db.alter_column(u'guias_cacao_cierreconocimiento2', 'trinitaria', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreConocimiento2.criollas'
        db.alter_column(u'guias_cacao_cierreconocimiento2', 'criollas', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreConocimiento2.forastero'
        db.alter_column(u'guias_cacao_cierreconocimiento2', 'forastero', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreConocimiento2.hibridos'
        db.alter_column(u'guias_cacao_cierreconocimiento2', 'hibridos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreConocimiento2.clones'
        db.alter_column(u'guias_cacao_cierreconocimiento2', 'clones', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierrePlaga3.monilla'
        db.alter_column(u'guias_cacao_cierreplaga3', 'monilla', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=5))

        # Changing field 'CierrePlaga3.mazorca'
        db.alter_column(u'guias_cacao_cierreplaga3', 'mazorca', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=5))

        # Changing field 'CierrePlaga3.zompopos'
        db.alter_column(u'guias_cacao_cierreplaga3', 'zompopos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=5))

        # Changing field 'CierreSuelo2.organico'
        db.alter_column(u'guias_cacao_cierresuelo2', 'organico', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreSuelo2.hojarasca'
        db.alter_column(u'guias_cacao_cierresuelo2', 'hojarasca', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreSuelo2.abono'
        db.alter_column(u'guias_cacao_cierresuelo2', 'abono', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreSuelo1.organico'
        db.alter_column(u'guias_cacao_cierresuelo1', 'organico', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreSuelo1.hojarasca'
        db.alter_column(u'guias_cacao_cierresuelo1', 'hojarasca', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreSuelo1.abono'
        db.alter_column(u'guias_cacao_cierresuelo1', 'abono', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreSuelo3.organico'
        db.alter_column(u'guias_cacao_cierresuelo3', 'organico', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreSuelo3.hojarasca'
        db.alter_column(u'guias_cacao_cierresuelo3', 'hojarasca', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreSuelo3.abono'
        db.alter_column(u'guias_cacao_cierresuelo3', 'abono', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierrePlaga2.monilla'
        db.alter_column(u'guias_cacao_cierreplaga2', 'monilla', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierrePlaga2.mazorca'
        db.alter_column(u'guias_cacao_cierreplaga2', 'mazorca', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierrePlaga2.zompopos'
        db.alter_column(u'guias_cacao_cierreplaga2', 'zompopos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

    def backwards(self, orm):
        # Deleting model 'CierreBabaRoja'
        db.delete_table(u'guias_cacao_cierrebabaroja')

        # Deleting field 'ViveroConversacion2.conversacion13'
        db.delete_column(u'guias_cacao_viveroconversacion2', 'conversacion13')

        # Deleting field 'ViveroConversacion2.conversacion14'
        db.delete_column(u'guias_cacao_viveroconversacion2', 'conversacion14')

        # Deleting field 'CierreManejo2.campo4'
        db.delete_column(u'guias_cacao_cierremanejo2', 'campo4')

        # Deleting field 'CierreManejo3.campo4'
        db.delete_column(u'guias_cacao_cierremanejo3', 'campo4')

        # Deleting field 'CierreManejo1.campo4'
        db.delete_column(u'guias_cacao_cierremanejo1', 'campo4')

        # Deleting field 'CierreManejo6.campo4'
        db.delete_column(u'guias_cacao_cierremanejo6', 'campo4')

        # Deleting field 'CierreManejo7.campo4'
        db.delete_column(u'guias_cacao_cierremanejo7', 'campo4')


        # Changing field 'CierreManejo7.campo1'
        db.alter_column(u'guias_cacao_cierremanejo7', 'campo1', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))
        # Deleting field 'CierreManejo4.campo4'
        db.delete_column(u'guias_cacao_cierremanejo4', 'campo4')

        # Deleting field 'CierreManejo5.campo4'
        db.delete_column(u'guias_cacao_cierremanejo5', 'campo4')


        # Changing field 'CierreManejo5.campo1'
        db.alter_column(u'guias_cacao_cierremanejo5', 'campo1', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=11))

        # Changing field 'CierreManejo5.campo2'
        db.alter_column(u'guias_cacao_cierremanejo5', 'campo2', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=13))

        # Changing field 'CierreManejo5.campo3'
        db.alter_column(u'guias_cacao_cierremanejo5', 'campo3', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=13))

        # Changing field 'CierreConocimiento3.trinitaria'
        db.alter_column(u'guias_cacao_cierreconocimiento3', 'trinitaria', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreConocimiento3.criollas'
        db.alter_column(u'guias_cacao_cierreconocimiento3', 'criollas', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreConocimiento3.forastero'
        db.alter_column(u'guias_cacao_cierreconocimiento3', 'forastero', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreConocimiento3.hibridos'
        db.alter_column(u'guias_cacao_cierreconocimiento3', 'hibridos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreConocimiento3.clones'
        db.alter_column(u'guias_cacao_cierreconocimiento3', 'clones', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreConocimiento2.trinitaria'
        db.alter_column(u'guias_cacao_cierreconocimiento2', 'trinitaria', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreConocimiento2.criollas'
        db.alter_column(u'guias_cacao_cierreconocimiento2', 'criollas', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreConocimiento2.forastero'
        db.alter_column(u'guias_cacao_cierreconocimiento2', 'forastero', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreConocimiento2.hibridos'
        db.alter_column(u'guias_cacao_cierreconocimiento2', 'hibridos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreConocimiento2.clones'
        db.alter_column(u'guias_cacao_cierreconocimiento2', 'clones', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierrePlaga3.monilla'
        db.alter_column(u'guias_cacao_cierreplaga3', 'monilla', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=3))

        # Changing field 'CierrePlaga3.mazorca'
        db.alter_column(u'guias_cacao_cierreplaga3', 'mazorca', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=3))

        # Changing field 'CierrePlaga3.zompopos'
        db.alter_column(u'guias_cacao_cierreplaga3', 'zompopos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=3))

        # Changing field 'CierreSuelo2.organico'
        db.alter_column(u'guias_cacao_cierresuelo2', 'organico', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreSuelo2.hojarasca'
        db.alter_column(u'guias_cacao_cierresuelo2', 'hojarasca', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreSuelo2.abono'
        db.alter_column(u'guias_cacao_cierresuelo2', 'abono', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreSuelo1.organico'
        db.alter_column(u'guias_cacao_cierresuelo1', 'organico', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreSuelo1.hojarasca'
        db.alter_column(u'guias_cacao_cierresuelo1', 'hojarasca', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreSuelo1.abono'
        db.alter_column(u'guias_cacao_cierresuelo1', 'abono', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreSuelo3.organico'
        db.alter_column(u'guias_cacao_cierresuelo3', 'organico', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreSuelo3.hojarasca'
        db.alter_column(u'guias_cacao_cierresuelo3', 'hojarasca', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierreSuelo3.abono'
        db.alter_column(u'guias_cacao_cierresuelo3', 'abono', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierrePlaga2.monilla'
        db.alter_column(u'guias_cacao_cierreplaga2', 'monilla', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierrePlaga2.mazorca'
        db.alter_column(u'guias_cacao_cierreplaga2', 'mazorca', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

        # Changing field 'CierrePlaga2.zompopos'
        db.alter_column(u'guias_cacao_cierreplaga2', 'zompopos', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=9))

    models = {
        u'guias_cacao.accionesenfermedad': {
            'Meta': {'object_name': 'AccionesEnfermedad'},
            'cuantas_veces': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'plagas_acciones': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'realiza_manejo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.accionessombra': {
            'Meta': {'object_name': 'AccionesSombra'},
            'accion': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.actividadescierre': {
            'Meta': {'object_name': 'ActividadesCierre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'guias_cacao.analisispoda': {
            'Meta': {'object_name': 'AnalisisPoda'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'campo3': ('django.db.models.fields.IntegerField', [], {}),
            'campo4': ('django.db.models.fields.IntegerField', [], {}),
            'campo5': ('django.db.models.fields.IntegerField', [], {}),
            'campo6': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.analisissombra': {
            'Meta': {'object_name': 'AnalisisSombra'},
            'Problema': ('django.db.models.fields.IntegerField', [], {}),
            'arreglo': ('django.db.models.fields.IntegerField', [], {}),
            'calidad_hojarasca': ('django.db.models.fields.IntegerField', [], {}),
            'competencia': ('django.db.models.fields.IntegerField', [], {}),
            'densidad': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'forma_copa': ('django.db.models.fields.IntegerField', [], {}),
            'hojarasca': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.aumentarsombra': {
            'Meta': {'object_name': 'AumentarSombra'},
            'cambiando': ('django.db.models.fields.IntegerField', [], {}),
            'cambiando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'que_parte': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sembrando': ('django.db.models.fields.IntegerField', [], {}),
            'sembrando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'todo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.cierreactividad': {
            'Meta': {'object_name': 'CierreActividad'},
            'actividad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.ActividadesCierre']"}),
            'contratada': ('django.db.models.fields.FloatField', [], {}),
            'costo': ('django.db.models.fields.FloatField', [], {}),
            'familiar': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insumo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'})
        },
        u'guias_cacao.cierrebabaroja': {
            'Meta': {'object_name': 'CierreBabaRoja'},
            'campo1': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'campo2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'campo3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'campo4': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'campo5': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'campo6': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'campo7': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cierreciclotrabajo': {
            'Meta': {'object_name': 'CierreCicloTrabajo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta1': ('django.db.models.fields.IntegerField', [], {}),
            'pregunta2': ('django.db.models.fields.IntegerField', [], {}),
            'pregunta3': ('django.db.models.fields.IntegerField', [], {}),
            'pregunta4': ('django.db.models.fields.IntegerField', [], {}),
            'pregunta5': ('django.db.models.fields.IntegerField', [], {}),
            'pregunta6': ('django.db.models.fields.IntegerField', [], {}),
            'pregunta7': ('django.db.models.fields.IntegerField', [], {}),
            'pregunta8': ('django.db.models.fields.IntegerField', [], {}),
            'pregunta9': ('django.db.models.fields.TextField', [], {})
        },
        u'guias_cacao.cierreconocimiento1': {
            'Meta': {'object_name': 'CierreConocimiento1'},
            'clones': ('django.db.models.fields.IntegerField', [], {}),
            'criollas': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            'forastero': ('django.db.models.fields.IntegerField', [], {}),
            'hibridos': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tema': ('django.db.models.fields.IntegerField', [], {}),
            'trinitaria': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.cierreconocimiento2': {
            'Meta': {'object_name': 'CierreConocimiento2'},
            'clones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'criollas': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            'forastero': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'hibridos': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tema': ('django.db.models.fields.IntegerField', [], {}),
            'trinitaria': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'})
        },
        u'guias_cacao.cierreconocimiento3': {
            'Meta': {'object_name': 'CierreConocimiento3'},
            'clones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'criollas': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            'forastero': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'hibridos': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tema': ('django.db.models.fields.IntegerField', [], {}),
            'trinitaria': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'})
        },
        u'guias_cacao.cierrecosto1': {
            'Meta': {'object_name': 'CierreCosto1'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'costo': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9'})
        },
        u'guias_cacao.cierremanejo': {
            'Meta': {'object_name': 'CierreManejo'},
            'cosecha': ('django.db.models.fields.IntegerField', [], {}),
            'crecimiento': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            'floracion': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.ManejosCierre']"}),
            'reposo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.cierremanejo1': {
            'Meta': {'object_name': 'CierreManejo1'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo4': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cierremanejo2': {
            'Meta': {'object_name': 'CierreManejo2'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo4': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cierremanejo3': {
            'Meta': {'object_name': 'CierreManejo3'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo4': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cierremanejo4': {
            'Meta': {'object_name': 'CierreManejo4'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'campo3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'campo4': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cierremanejo5': {
            'Meta': {'object_name': 'CierreManejo5'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'campo3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'campo4': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cierremanejo6': {
            'Meta': {'object_name': 'CierreManejo6'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo4': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cierremanejo7': {
            'Meta': {'object_name': 'CierreManejo7'},
            'campo1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'campo4': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cierreplaga1': {
            'Meta': {'object_name': 'CierrePlaga1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mazorca': ('django.db.models.fields.FloatField', [], {}),
            'monilla': ('django.db.models.fields.FloatField', [], {}),
            'tema': ('django.db.models.fields.IntegerField', [], {}),
            'zompopos': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.cierreplaga2': {
            'Meta': {'object_name': 'CierrePlaga2'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mazorca': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'monilla': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'tema': ('django.db.models.fields.IntegerField', [], {}),
            'zompopos': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'})
        },
        u'guias_cacao.cierreplaga3': {
            'Meta': {'object_name': 'CierrePlaga3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mazorca': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'monilla': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'tema': ('django.db.models.fields.IntegerField', [], {}),
            'zompopos': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'})
        },
        u'guias_cacao.cierresuelo1': {
            'Meta': {'object_name': 'CierreSuelo1'},
            'abono': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            'hojarasca': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organico': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'tema': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.cierresuelo2': {
            'Meta': {'object_name': 'CierreSuelo2'},
            'abono': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            'hojarasca': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organico': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'tema': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.cierresuelo3': {
            'Meta': {'object_name': 'CierreSuelo3'},
            'abono': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCierre']"}),
            'hojarasca': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organico': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'tema': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.cobertura1': {
            'Meta': {'object_name': 'Cobertura1'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cobertura2': {
            'Meta': {'object_name': 'Cobertura2'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cobertura3': {
            'Meta': {'object_name': 'Cobertura3'},
            'cobertura': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cosechaanalisis': {
            'Meta': {'object_name': 'CosechaAnalisis'},
            'analisis1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'analisis2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'analisis3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCosecha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cosechaareaplantas': {
            'Meta': {'object_name': 'CosechaAreaPlantas'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCosecha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plantas': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.cosechaconversacion1': {
            'Meta': {'object_name': 'CosechaConversacion1'},
            'conversacion1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7'}),
            'conversacion2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7'}),
            'conversacion3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'conversacion4': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCosecha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cosechaconversacion2': {
            'Meta': {'object_name': 'CosechaConversacion2'},
            'conversacion5': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9'}),
            'conversacion6': ('django.db.models.fields.FloatField', [], {}),
            'conversacion7': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'conversacion8': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCosecha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.cosechamesescosecha': {
            'Meta': {'object_name': 'CosechaMesesCosecha'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCosecha']"}),
            'floracion': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.cosechamesesfloracion': {
            'Meta': {'object_name': 'CosechaMesesFloracion'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCosecha']"}),
            'floracion': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.cosechapunto1': {
            'Meta': {'object_name': 'CosechaPunto1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCosecha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mazorcas': ('django.db.models.fields.IntegerField', [], {}),
            'planta_1': ('django.db.models.fields.FloatField', [], {}),
            'planta_10': ('django.db.models.fields.FloatField', [], {}),
            'planta_2': ('django.db.models.fields.FloatField', [], {}),
            'planta_3': ('django.db.models.fields.FloatField', [], {}),
            'planta_4': ('django.db.models.fields.FloatField', [], {}),
            'planta_5': ('django.db.models.fields.FloatField', [], {}),
            'planta_6': ('django.db.models.fields.FloatField', [], {}),
            'planta_7': ('django.db.models.fields.FloatField', [], {}),
            'planta_8': ('django.db.models.fields.FloatField', [], {}),
            'planta_9': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.cosechapunto2': {
            'Meta': {'object_name': 'CosechaPunto2'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCosecha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mazorcas': ('django.db.models.fields.IntegerField', [], {}),
            'planta_1': ('django.db.models.fields.FloatField', [], {}),
            'planta_10': ('django.db.models.fields.FloatField', [], {}),
            'planta_2': ('django.db.models.fields.FloatField', [], {}),
            'planta_3': ('django.db.models.fields.FloatField', [], {}),
            'planta_4': ('django.db.models.fields.FloatField', [], {}),
            'planta_5': ('django.db.models.fields.FloatField', [], {}),
            'planta_6': ('django.db.models.fields.FloatField', [], {}),
            'planta_7': ('django.db.models.fields.FloatField', [], {}),
            'planta_8': ('django.db.models.fields.FloatField', [], {}),
            'planta_9': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.cosechapunto3': {
            'Meta': {'object_name': 'CosechaPunto3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaCosecha']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mazorcas': ('django.db.models.fields.IntegerField', [], {}),
            'planta_1': ('django.db.models.fields.FloatField', [], {}),
            'planta_10': ('django.db.models.fields.FloatField', [], {}),
            'planta_2': ('django.db.models.fields.FloatField', [], {}),
            'planta_3': ('django.db.models.fields.FloatField', [], {}),
            'planta_4': ('django.db.models.fields.FloatField', [], {}),
            'planta_5': ('django.db.models.fields.FloatField', [], {}),
            'planta_6': ('django.db.models.fields.FloatField', [], {}),
            'planta_7': ('django.db.models.fields.FloatField', [], {}),
            'planta_8': ('django.db.models.fields.FloatField', [], {}),
            'planta_9': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.datosanalisis': {
            'Meta': {'object_name': 'DatosAnalisis'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'valor_critico': ('django.db.models.fields.FloatField', [], {}),
            'variable': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'guias_cacao.especies': {
            'Meta': {'object_name': 'Especies'},
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'g_altura': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'g_ancho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'g_diametro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_altura': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'm_ancho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'm_diametro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_cientifico': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'p_altura': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p_ancho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p_diametro': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_uso': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.fichacierre': {
            'Meta': {'object_name': 'FichaCierre'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_cierre'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_cierre'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichacosecha': {
            'Meta': {'object_name': 'FichaCosecha'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_cosecha'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_cosecha'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichapiso': {
            'Meta': {'object_name': 'FichaPiso'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_piso'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_piso'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichaplaga': {
            'Meta': {'object_name': 'FichaPlaga'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_plaga'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_plaga'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichapoda': {
            'Meta': {'object_name': 'FichaPoda'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'setproductor'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'settecnico'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichasaf': {
            'Meta': {'object_name': 'FichaSaf'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_saf'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_saf'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichasombra': {
            'Meta': {'object_name': 'FichaSombra'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichasuelo': {
            'Meta': {'object_name': 'FichaSuelo'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_suelo'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_suelo'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.fichavivero': {
            'Meta': {'object_name': 'FichaVivero'},
            'fecha_visita': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_productor_vivero'", 'to': u"orm['mapeo.Persona']"}),
            'tecnico': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_tecnico_vivero'", 'to': u"orm['mapeo.Persona']"})
        },
        u'guias_cacao.foto1': {
            'Meta': {'object_name': 'Foto1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.foto2': {
            'Meta': {'object_name': 'Foto2'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.foto3': {
            'Meta': {'object_name': 'Foto3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'foto': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.manejopoda': {
            'Meta': {'object_name': 'ManejoPoda'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            'formacion': ('django.db.models.fields.IntegerField', [], {}),
            'herramientas': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.manejoscierre': {
            'Meta': {'object_name': 'ManejosCierre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'guias_cacao.manejosombra': {
            'Meta': {'object_name': 'ManejoSombra'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'formacion': ('django.db.models.fields.IntegerField', [], {}),
            'herramientas': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.observacionpunto1': {
            'Meta': {'object_name': 'ObservacionPunto1'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto1nivel': {
            'Meta': {'object_name': 'ObservacionPunto1Nivel'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto2': {
            'Meta': {'object_name': 'ObservacionPunto2'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto2nivel': {
            'Meta': {'object_name': 'ObservacionPunto2Nivel'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto3': {
            'Meta': {'object_name': 'ObservacionPunto3'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.observacionpunto3nivel': {
            'Meta': {'object_name': 'ObservacionPunto3Nivel'},
            'cinco': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ocho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'planta': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'siete': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tres': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uno': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.orientacion': {
            'Meta': {'object_name': 'Orientacion'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            'fuentes': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.pisopunto1': {
            'Meta': {'object_name': 'PisoPunto1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'punto1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'punto2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'})
        },
        u'guias_cacao.pisopunto10': {
            'Meta': {'object_name': 'PisoPunto10'},
            'equipo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            'formacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.pisopunto3': {
            'Meta': {'object_name': 'PisoPunto3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'realiza': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'veces': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.pisopunto4': {
            'Meta': {'object_name': 'PisoPunto4'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'})
        },
        u'guias_cacao.pisopunto5': {
            'Meta': {'object_name': 'PisoPunto5'},
            'conteo': ('django.db.models.fields.FloatField', [], {}),
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.pisopunto6': {
            'Meta': {'object_name': 'PisoPunto6'},
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maleza': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'})
        },
        u'guias_cacao.pisopunto7': {
            'Meta': {'object_name': 'PisoPunto7'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'sombra': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7'}),
            'suelo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'})
        },
        u'guias_cacao.pisopunto8': {
            'Meta': {'object_name': 'PisoPunto8'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPiso']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'parte': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'piso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.plagasenfermedad': {
            'Meta': {'object_name': 'PlagasEnfermedad'},
            'dano': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plagas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'visto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.problemasprincipales': {
            'Meta': {'object_name': 'ProblemasPrincipales'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observadas': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '27'}),
            'principales': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '27'}),
            'situacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.productosvivero': {
            'Meta': {'object_name': 'ProductosVivero'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'guias_cacao.punto1': {
            'Meta': {'object_name': 'Punto1'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto1a': {
            'Meta': {'object_name': 'Punto1A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.punto1b': {
            'Meta': {'object_name': 'Punto1B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto1c': {
            'Meta': {'object_name': 'Punto1C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto1suelo': {
            'Meta': {'object_name': 'Punto1Suelo'},
            'abonos': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitante': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'orientacion': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'uso_parcela': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2': {
            'Meta': {'object_name': 'Punto2'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2a': {
            'Meta': {'object_name': 'Punto2A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.punto2asuelo': {
            'Meta': {'object_name': 'Punto2ASuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2b': {
            'Meta': {'object_name': 'Punto2B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2bsuelo': {
            'Meta': {'object_name': 'Punto2BSuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto2c': {
            'Meta': {'object_name': 'Punto2C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3': {
            'Meta': {'object_name': 'Punto3'},
            'especie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            'grande': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediana': ('django.db.models.fields.FloatField', [], {}),
            'pequena': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_de_copa': ('django.db.models.fields.IntegerField', [], {}),
            'uso': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3a': {
            'Meta': {'object_name': 'Punto3A'},
            'cinco': ('django.db.models.fields.FloatField', [], {}),
            'cuatro': ('django.db.models.fields.FloatField', [], {}),
            'diez': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.FloatField', [], {}),
            'ocho': ('django.db.models.fields.FloatField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.FloatField', [], {}),
            'siete': ('django.db.models.fields.FloatField', [], {}),
            'tres': ('django.db.models.fields.FloatField', [], {}),
            'uno': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.punto3b': {
            'Meta': {'object_name': 'Punto3B'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3c': {
            'Meta': {'object_name': 'Punto3C'},
            'cinco': ('django.db.models.fields.IntegerField', [], {}),
            'cuatro': ('django.db.models.fields.IntegerField', [], {}),
            'diez': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dos': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPoda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nueve': ('django.db.models.fields.IntegerField', [], {}),
            'ocho': ('django.db.models.fields.IntegerField', [], {}),
            'plantas': ('django.db.models.fields.IntegerField', [], {}),
            'seis': ('django.db.models.fields.IntegerField', [], {}),
            'siete': ('django.db.models.fields.IntegerField', [], {}),
            'tres': ('django.db.models.fields.IntegerField', [], {}),
            'uno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3suelopunto1': {
            'Meta': {'object_name': 'Punto3SueloPunto1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3suelopunto2': {
            'Meta': {'object_name': 'Punto3SueloPunto2'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto3suelopunto3': {
            'Meta': {'object_name': 'Punto3SueloPunto3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto4suelo': {
            'Meta': {'object_name': 'Punto4Suelo'},
            'area': ('django.db.models.fields.FloatField', [], {}),
            'densidad': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.punto4suelocosecha': {
            'Meta': {'object_name': 'Punto4SueloCosecha'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto4suelosi': {
            'Meta': {'object_name': 'Punto4SueloSI'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto5sueloabonos': {
            'Meta': {'object_name': 'Punto5SueloAbonos'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            'frecuencia': ('django.db.models.fields.FloatField', [], {}),
            'humedad': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.TipoFertilizantes']"}),
            'unidad': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto6analisissuelo': {
            'Meta': {'object_name': 'Punto6AnalisisSuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.FloatField', [], {}),
            'variable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.DatosAnalisis']"})
        },
        u'guias_cacao.punto6plagas': {
            'Meta': {'object_name': 'Punto6Plagas'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'observaciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'sombra': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.punto7plagas': {
            'Meta': {'object_name': 'Punto7Plagas'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manejo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'parte': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.punto7tiposuelo': {
            'Meta': {'object_name': 'Punto7TipoSuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto8suelopropuesta': {
            'Meta': {'object_name': 'Punto8SueloPropuesta'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            'frecuencia': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meses': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.TipoFertilizantes']"}),
            'unidad': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto8y9plagas': {
            'Meta': {'object_name': 'Punto8y9Plagas'},
            'equipos': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaPlaga']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'guias_cacao.punto9desbalance': {
            'Meta': {'object_name': 'Punto9Desbalance'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '1'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto9drenaje': {
            'Meta': {'object_name': 'Punto9Drenaje'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto9enfermedades': {
            'Meta': {'object_name': 'Punto9Enfermedades'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto9erosion': {
            'Meta': {'object_name': 'Punto9Erosion'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto9exceso': {
            'Meta': {'object_name': 'Punto9Exceso'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '1'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.punto9nutrientes': {
            'Meta': {'object_name': 'Punto9Nutrientes'},
            'acciones': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '3'}),
            'donde': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limitaciones': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.puntoasuelo': {
            'Meta': {'object_name': 'PuntoASuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.puntobsuelo': {
            'Meta': {'object_name': 'PuntoBSuelo'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSuelo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opcion': ('django.db.models.fields.IntegerField', [], {}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.reducirsombra': {
            'Meta': {'object_name': 'ReducirSombra'},
            'eliminando': ('django.db.models.fields.IntegerField', [], {}),
            'eliminando_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSombra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poda': ('django.db.models.fields.IntegerField', [], {}),
            'poda_cuales': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'que_parte': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'todo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.safconversacion1': {
            'Meta': {'object_name': 'SafConversacion1'},
            'conversacion1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7'}),
            'conversacion2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.safconversacion2': {
            'Meta': {'object_name': 'SafConversacion2'},
            'conversacion3': ('django.db.models.fields.IntegerField', [], {}),
            'conversacion4': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.safconversacion3': {
            'Meta': {'object_name': 'SafConversacion3'},
            'conversacion3': ('django.db.models.fields.IntegerField', [], {}),
            'conversacion4': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.safconversacion4': {
            'Meta': {'object_name': 'SafConversacion4'},
            'conversacion5': ('django.db.models.fields.IntegerField', [], {}),
            'conversacion6': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.safconversacion5': {
            'Meta': {'object_name': 'SafConversacion5'},
            'conversacion7': ('django.db.models.fields.IntegerField', [], {}),
            'conversacion8': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.safconversacion6': {
            'Meta': {'object_name': 'SafConversacion6'},
            'conversacion10': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'conversacion11': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'conversacion9': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.safconversacion7': {
            'Meta': {'object_name': 'SafConversacion7'},
            'conversacion12': ('django.db.models.fields.IntegerField', [], {}),
            'conversacion13': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'conversacion14': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.safconversacion8': {
            'Meta': {'object_name': 'SafConversacion8'},
            'conversacion15': ('django.db.models.fields.IntegerField', [], {}),
            'conversacion16': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.safconversacion9': {
            'Meta': {'object_name': 'SafConversacion9'},
            'conversacion17': ('django.db.models.fields.IntegerField', [], {}),
            'conversacion18': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'conversacion19': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'conversacion20': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.safobservaciones': {
            'Meta': {'object_name': 'SafObservaciones'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion1': ('django.db.models.fields.IntegerField', [], {}),
            'observacion2': ('django.db.models.fields.FloatField', [], {}),
            'observacion3': ('django.db.models.fields.FloatField', [], {}),
            'observacion4': ('django.db.models.fields.FloatField', [], {}),
            'observacion5': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.safobservaciones2': {
            'Meta': {'object_name': 'SafObservaciones2'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion1': ('django.db.models.fields.IntegerField', [], {}),
            'observacion2': ('django.db.models.fields.IntegerField', [], {}),
            'observacion3': ('django.db.models.fields.IntegerField', [], {}),
            'observacion4': ('django.db.models.fields.IntegerField', [], {}),
            'observacion5': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.safobservaciones3': {
            'Meta': {'object_name': 'SafObservaciones3'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion6': ('django.db.models.fields.IntegerField', [], {}),
            'observacion7': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'})
        },
        u'guias_cacao.safobservaciones4': {
            'Meta': {'object_name': 'SafObservaciones4'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion10': ('django.db.models.fields.IntegerField', [], {}),
            'observacion11': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'observacion8': ('django.db.models.fields.IntegerField', [], {}),
            'observacion9': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.safobservacionpunto1': {
            'Meta': {'object_name': 'SafObservacionPunto1'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'especies': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            'frutas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lena': ('django.db.models.fields.FloatField', [], {}),
            'madera': ('django.db.models.fields.FloatField', [], {}),
            'nutrientes': ('django.db.models.fields.FloatField', [], {}),
            'sombra': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.safobservacionpunto2': {
            'Meta': {'object_name': 'SafObservacionPunto2'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'especies': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            'frutas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lena': ('django.db.models.fields.FloatField', [], {}),
            'madera': ('django.db.models.fields.FloatField', [], {}),
            'nutrientes': ('django.db.models.fields.FloatField', [], {}),
            'sombra': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.safobservacionpunto3': {
            'Meta': {'object_name': 'SafObservacionPunto3'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'especies': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.Especies']"}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaSaf']"}),
            'frutas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lena': ('django.db.models.fields.FloatField', [], {}),
            'madera': ('django.db.models.fields.FloatField', [], {}),
            'nutrientes': ('django.db.models.fields.FloatField', [], {}),
            'sombra': ('django.db.models.fields.FloatField', [], {})
        },
        u'guias_cacao.tipofertilizantes': {
            'Meta': {'object_name': 'TipoFertilizantes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'guias_cacao.viveroconversacion2': {
            'Meta': {'object_name': 'ViveroConversacion2'},
            'conversacion10': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'conversacion11': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'conversacion12': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'conversacion13': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'conversacion14': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'conversacion7': ('django.db.models.fields.IntegerField', [], {}),
            'conversacion8': ('django.db.models.fields.IntegerField', [], {}),
            'conversacion9': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaVivero']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.vivieroanalisissituacion': {
            'Meta': {'object_name': 'VivieroAnalisisSituacion'},
            'analisis1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '5'}),
            'analisis2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'analisis3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '15'}),
            'analisis4': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaVivero']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.vivieroconversacion': {
            'Meta': {'object_name': 'VivieroConversacion'},
            'conversacion1': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '23'}),
            'conversacion2': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '7'}),
            'conversacion3': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '13'}),
            'conversacion4': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '11'}),
            'conversacion5': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '9'}),
            'conversacion6': ('django.db.models.fields.IntegerField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaVivero']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'guias_cacao.vivieroobservacion1': {
            'Meta': {'object_name': 'VivieroObservacion1'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaVivero']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion1': ('django.db.models.fields.FloatField', [], {}),
            'observacion2': ('django.db.models.fields.FloatField', [], {}),
            'observacion3': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.vivieroobservacion2': {
            'Meta': {'object_name': 'VivieroObservacion2'},
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaVivero']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion3': ('django.db.models.fields.IntegerField', [], {}),
            'planta_1': ('django.db.models.fields.IntegerField', [], {}),
            'planta_10': ('django.db.models.fields.IntegerField', [], {}),
            'planta_2': ('django.db.models.fields.IntegerField', [], {}),
            'planta_3': ('django.db.models.fields.IntegerField', [], {}),
            'planta_4': ('django.db.models.fields.IntegerField', [], {}),
            'planta_5': ('django.db.models.fields.IntegerField', [], {}),
            'planta_6': ('django.db.models.fields.IntegerField', [], {}),
            'planta_7': ('django.db.models.fields.IntegerField', [], {}),
            'planta_8': ('django.db.models.fields.IntegerField', [], {}),
            'planta_9': ('django.db.models.fields.IntegerField', [], {})
        },
        u'guias_cacao.vivieroobservacionproductos': {
            'Meta': {'object_name': 'VivieroObservacionProductos'},
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'ficha': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.FichaVivero']"}),
            'frecuencia': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['guias_cacao.ProductosVivero']"}),
            'unidad': ('django.db.models.fields.IntegerField', [], {})
        },
        u'lugar.comunidad': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Comunidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'lugar.departamento': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        u'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre', 'nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        u'lugar.pais': {
            'Meta': {'object_name': 'Pais'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'mapeo.persona': {
            'Meta': {'object_name': 'Persona'},
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Comunidad']"}),
            'departamento': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_persona': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['guias_cacao']