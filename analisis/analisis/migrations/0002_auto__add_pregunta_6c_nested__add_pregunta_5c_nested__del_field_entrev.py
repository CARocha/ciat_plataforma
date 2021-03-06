# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pregunta_6c_nested'
        db.create_table(u'analisis_pregunta_6c_nested', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Organizaciones'])),
            ('pregunta_6c', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Pregunta_6c'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_6c_nested'])

        # Adding M2M table for field papel on 'Pregunta_6c_nested'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_6c_nested_papel')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_6c_nested', models.ForeignKey(orm[u'analisis.pregunta_6c_nested'], null=False)),
            ('papel', models.ForeignKey(orm[u'configuracion.papel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_6c_nested_id', 'papel_id'])

        # Adding model 'Pregunta_5c_nested'
        db.create_table(u'analisis_pregunta_5c_nested', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapeo.Organizaciones'])),
            ('pregunta_5c', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analisis.Pregunta_5c'])),
        ))
        db.send_create_signal(u'analisis', ['Pregunta_5c_nested'])

        # Adding M2M table for field papel_1 on 'Pregunta_5c_nested'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_5c_nested_papel_1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_5c_nested', models.ForeignKey(orm[u'analisis.pregunta_5c_nested'], null=False)),
            ('papel', models.ForeignKey(orm[u'configuracion.papel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_5c_nested_id', 'papel_id'])

        # Deleting field 'Entrevista.fecha'
        db.delete_column(u'analisis_entrevista', 'fecha')

        # Adding field 'Entrevista.fecha1'
        db.add_column(u'analisis_entrevista', 'fecha1',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)

        # Deleting field 'Pregunta_6c.organizacion'
        db.delete_column(u'analisis_pregunta_6c', 'organizacion_id')

        # Removing M2M table for field papel on 'Pregunta_6c'
        db.delete_table(db.shorten_name(u'analisis_pregunta_6c_papel'))

        # Deleting field 'Pregunta_5c.organizacion'
        db.delete_column(u'analisis_pregunta_5c', 'organizacion_id')

        # Removing M2M table for field papel_1 on 'Pregunta_5c'
        db.delete_table(db.shorten_name(u'analisis_pregunta_5c_papel_1'))


    def backwards(self, orm):
        # Deleting model 'Pregunta_6c_nested'
        db.delete_table(u'analisis_pregunta_6c_nested')

        # Removing M2M table for field papel on 'Pregunta_6c_nested'
        db.delete_table(db.shorten_name(u'analisis_pregunta_6c_nested_papel'))

        # Deleting model 'Pregunta_5c_nested'
        db.delete_table(u'analisis_pregunta_5c_nested')

        # Removing M2M table for field papel_1 on 'Pregunta_5c_nested'
        db.delete_table(db.shorten_name(u'analisis_pregunta_5c_nested_papel_1'))

        # Adding field 'Entrevista.fecha'
        db.add_column(u'analisis_entrevista', 'fecha',
                      self.gf('django.db.models.fields.DateField')(default=2),
                      keep_default=False)

        # Deleting field 'Entrevista.fecha1'
        db.delete_column(u'analisis_entrevista', 'fecha1')

        # Adding field 'Pregunta_6c.organizacion'
        db.add_column(u'analisis_pregunta_6c', 'organizacion',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['mapeo.Organizaciones']),
                      keep_default=False)

        # Adding M2M table for field papel on 'Pregunta_6c'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_6c_papel')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_6c', models.ForeignKey(orm[u'analisis.pregunta_6c'], null=False)),
            ('papel', models.ForeignKey(orm[u'configuracion.papel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_6c_id', 'papel_id'])

        # Adding field 'Pregunta_5c.organizacion'
        db.add_column(u'analisis_pregunta_5c', 'organizacion',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['mapeo.Organizaciones']),
                      keep_default=False)

        # Adding M2M table for field papel_1 on 'Pregunta_5c'
        m2m_table_name = db.shorten_name(u'analisis_pregunta_5c_papel_1')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pregunta_5c', models.ForeignKey(orm[u'analisis.pregunta_5c'], null=False)),
            ('papel', models.ForeignKey(orm[u'configuracion.papel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pregunta_5c_id', 'papel_id'])


    models = {
        u'analisis.entrevista': {
            'Meta': {'object_name': 'Entrevista'},
            'alcance1': ('django.db.models.fields.IntegerField', [], {}),
            'departamento': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lugar.Departamento']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha1': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Organizaciones']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'posicion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_estudio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Tipo_Estudio']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'analisis.pregunta_1': {
            'Meta': {'object_name': 'Pregunta_1'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'estado1': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proyecto': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'socio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.Organizaciones']", 'symmetrical': 'False'}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Tema']", 'symmetrical': 'False'}),
            'ubicacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lugar.Municipio']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_11': {
            'Meta': {'object_name': 'Pregunta_11'},
            'calendario': ('django.db.models.fields.IntegerField', [], {}),
            'disponibilidad1': ('django.db.models.fields.IntegerField', [], {}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sobre': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_estudio1': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analisis.pregunta_2': {
            'Meta': {'object_name': 'Pregunta_2'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'hombre': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujer': ('django.db.models.fields.IntegerField', [], {}),
            'seleccion1': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analisis.pregunta_3': {
            'Meta': {'object_name': 'Pregunta_3'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'grupo': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Grupo']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'analisis.pregunta_4': {
            'Meta': {'object_name': 'Pregunta_4'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'grupo_beneficiario': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Grupo']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impacto': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Tema']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_5a': {
            'Meta': {'object_name': 'Pregunta_5a'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'prioritizado': ('django.db.models.fields.IntegerField', [], {}),
            'socio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mapeo.Organizaciones']", 'symmetrical': 'False'}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Tema']", 'symmetrical': 'False'}),
            'ubicacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lugar.Municipio']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_5c': {
            'Meta': {'object_name': 'Pregunta_5c'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_5a']"})
        },
        u'analisis.pregunta_5c_nested': {
            'Meta': {'object_name': 'Pregunta_5c_nested'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Organizaciones']"}),
            'papel_1': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Papel']", 'symmetrical': 'False'}),
            'pregunta_5c': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_5c']"})
        },
        u'analisis.pregunta_5d': {
            'Meta': {'object_name': 'Pregunta_5d'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Categoria']", 'symmetrical': 'False'}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_5a']"})
        },
        u'analisis.pregunta_5e': {
            'Meta': {'object_name': 'Pregunta_5e'},
            'categoria_fuente': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Categoria_Fuente']", 'symmetrical': 'False'}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'fuente': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_5a']"})
        },
        u'analisis.pregunta_6a': {
            'Meta': {'object_name': 'Pregunta_6a'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prioritizado': ('django.db.models.fields.IntegerField', [], {}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Tema']", 'symmetrical': 'False'}),
            'ubicacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lugar.Municipio']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_6c': {
            'Meta': {'object_name': 'Pregunta_6c'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_6a']"})
        },
        u'analisis.pregunta_6c_nested': {
            'Meta': {'object_name': 'Pregunta_6c_nested'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Organizaciones']"}),
            'papel': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Papel']", 'symmetrical': 'False'}),
            'pregunta_6c': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_6c']"})
        },
        u'analisis.pregunta_6d': {
            'Meta': {'object_name': 'Pregunta_6d'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Categoria']", 'symmetrical': 'False'}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_6a']"})
        },
        u'analisis.pregunta_6e': {
            'Meta': {'object_name': 'Pregunta_6e'},
            'categoria_conocimient': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Categoria_Conocimiento']", 'symmetrical': 'False'}),
            'categoria_innovacio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Categoria_Innovacion']"}),
            'conocimient': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Pregunta_6a']"})
        },
        u'analisis.pregunta_7a': {
            'Meta': {'object_name': 'Pregunta_7a'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seleccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Seleccion_7a']", 'symmetrical': 'False'}),
            'ubicacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lugar.Municipio']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_7b': {
            'Meta': {'object_name': 'Pregunta_7b'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seleccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Seleccion_7b']", 'symmetrical': 'False'})
        },
        u'analisis.pregunta_8': {
            'Meta': {'object_name': 'Pregunta_8'},
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Organizaciones']"}),
            'periodo1': ('django.db.models.fields.IntegerField', [], {}),
            'profundidad1': ('django.db.models.fields.IntegerField', [], {}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['configuracion.Tema_Relacion']", 'symmetrical': 'False'}),
            'territorio1': ('django.db.models.fields.IntegerField', [], {})
        },
        u'analisis.pregunta_9': {
            'Meta': {'object_name': 'Pregunta_9'},
            'conocimiento': ('django.db.models.fields.IntegerField', [], {}),
            'entrevistado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analisis.Entrevista']"}),
            'experiencia': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'papel1': ('django.db.models.fields.IntegerField', [], {}),
            'prioridad1': ('django.db.models.fields.IntegerField', [], {}),
            'tema': ('django.db.models.fields.IntegerField', [], {})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'configuracion.areaaccion': {
            'Meta': {'object_name': 'AreaAccion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'configuracion.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.categoria_conocimiento': {
            'Meta': {'object_name': 'Categoria_Conocimiento'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.categoria_fuente': {
            'Meta': {'object_name': 'Categoria_Fuente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.categoria_innovacion': {
            'Meta': {'object_name': 'Categoria_Innovacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.grupo': {
            'Meta': {'object_name': 'Grupo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.papel': {
            'Meta': {'object_name': 'Papel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.plataforma': {
            'Meta': {'object_name': 'Plataforma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sitio_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.SitioAccion']"})
        },
        u'configuracion.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'configuracion.seleccion_7a': {
            'Meta': {'object_name': 'Seleccion_7a'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.seleccion_7b': {
            'Meta': {'object_name': 'Seleccion_7b'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.sitioaccion': {
            'Meta': {'object_name': 'SitioAccion'},
            'area_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.AreaAccion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'configuracion.tema': {
            'Meta': {'object_name': 'Tema'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tema': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'configuracion.tema_relacion': {
            'Meta': {'object_name': 'Tema_Relacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'configuracion.tipo_estudio': {
            'Meta': {'object_name': 'Tipo_Estudio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'lugar.departamento': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
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
        u'mapeo.organizaciones': {
            'Meta': {'ordering': "[u'nombre']", 'unique_together': "((u'font_color', u'nombre'),)", 'object_name': 'Organizaciones'},
            'area_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.AreaAccion']"}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'correo_electronico': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'departamento': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'font_color': ('mapeo.models.ColorField', [], {'unique': 'True', 'max_length': '10', 'blank': 'True'}),
            'fundacion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'generalidades': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': (u'sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'plataforma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Plataforma']"}),
            'rss': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.Sector']"}),
            'siglas': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sitio_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.SitioAccion']"}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'temas': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['analisis']