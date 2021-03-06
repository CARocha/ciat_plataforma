# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrgGremiales'
        db.create_table(u'indicador02_orggremiales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador02', ['OrgGremiales'])

        # Adding model 'BeneficiosObtenido'
        db.create_table(u'indicador02_beneficiosobtenido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador02', ['BeneficiosObtenido'])

        # Adding model 'SerMiembro'
        db.create_table(u'indicador02_sermiembro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador02', ['SerMiembro'])

        # Adding model 'OrganizacionGremial'
        db.create_table(u'indicador02_organizaciongremial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desde_socio', self.gf('django.db.models.fields.IntegerField')()),
            ('miembro_gremial', self.gf('django.db.models.fields.IntegerField')()),
            ('desde_miembro', self.gf('django.db.models.fields.IntegerField')()),
            ('capacitacion', self.gf('django.db.models.fields.IntegerField')()),
            ('desde_capacitacion', self.gf('django.db.models.fields.IntegerField')()),
            ('asumir_cargo', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador02', ['OrganizacionGremial'])

        # Adding M2M table for field socio on 'OrganizacionGremial'
        m2m_table_name = db.shorten_name(u'indicador02_organizaciongremial_socio')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizaciongremial', models.ForeignKey(orm[u'indicador02.organizaciongremial'], null=False)),
            ('orggremiales', models.ForeignKey(orm[u'indicador02.orggremiales'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organizaciongremial_id', 'orggremiales_id'])

        # Adding M2M table for field beneficio on 'OrganizacionGremial'
        m2m_table_name = db.shorten_name(u'indicador02_organizaciongremial_beneficio')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizaciongremial', models.ForeignKey(orm[u'indicador02.organizaciongremial'], null=False)),
            ('beneficiosobtenido', models.ForeignKey(orm[u'indicador02.beneficiosobtenido'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organizaciongremial_id', 'beneficiosobtenido_id'])

        # Adding M2M table for field miembro_junta on 'OrganizacionGremial'
        m2m_table_name = db.shorten_name(u'indicador02_organizaciongremial_miembro_junta')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizaciongremial', models.ForeignKey(orm[u'indicador02.organizaciongremial'], null=False)),
            ('sermiembro', models.ForeignKey(orm[u'indicador02.sermiembro'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organizaciongremial_id', 'sermiembro_id'])

        # Adding model 'OrgComunitarias'
        db.create_table(u'indicador02_orgcomunitarias', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador02', ['OrgComunitarias'])

        # Adding model 'BeneficioOrgComunitaria'
        db.create_table(u'indicador02_beneficioorgcomunitaria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador02', ['BeneficioOrgComunitaria'])

        # Adding model 'NoOrganizado'
        db.create_table(u'indicador02_noorganizado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'indicador02', ['NoOrganizado'])

        # Adding model 'OrganizacionComunitaria'
        db.create_table(u'indicador02_organizacioncomunitaria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('pertence', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador02', ['OrganizacionComunitaria'])

        # Adding M2M table for field cual_organizacion on 'OrganizacionComunitaria'
        m2m_table_name = db.shorten_name(u'indicador02_organizacioncomunitaria_cual_organizacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm[u'indicador02.organizacioncomunitaria'], null=False)),
            ('orgcomunitarias', models.ForeignKey(orm[u'indicador02.orgcomunitarias'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organizacioncomunitaria_id', 'orgcomunitarias_id'])

        # Adding M2M table for field cual_beneficio on 'OrganizacionComunitaria'
        m2m_table_name = db.shorten_name(u'indicador02_organizacioncomunitaria_cual_beneficio')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm[u'indicador02.organizacioncomunitaria'], null=False)),
            ('beneficioorgcomunitaria', models.ForeignKey(orm[u'indicador02.beneficioorgcomunitaria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organizacioncomunitaria_id', 'beneficioorgcomunitaria_id'])

        # Adding M2M table for field no_organizado on 'OrganizacionComunitaria'
        m2m_table_name = db.shorten_name(u'indicador02_organizacioncomunitaria_no_organizado')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacioncomunitaria', models.ForeignKey(orm[u'indicador02.organizacioncomunitaria'], null=False)),
            ('noorganizado', models.ForeignKey(orm[u'indicador02.noorganizado'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organizacioncomunitaria_id', 'noorganizado_id'])

        # Adding model 'OngLocales'
        db.create_table(u'indicador02_onglocales', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'indicador02', ['OngLocales'])

        # Adding model 'OrganizacionOng'
        db.create_table(u'indicador02_organizacionong', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitoreo.Encuesta'])),
        ))
        db.send_create_signal(u'indicador02', ['OrganizacionOng'])

        # Adding M2M table for field cuales on 'OrganizacionOng'
        m2m_table_name = db.shorten_name(u'indicador02_organizacionong_cuales')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacionong', models.ForeignKey(orm[u'indicador02.organizacionong'], null=False)),
            ('onglocales', models.ForeignKey(orm[u'indicador02.onglocales'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organizacionong_id', 'onglocales_id'])

        # Adding M2M table for field cual_organizacion on 'OrganizacionOng'
        m2m_table_name = db.shorten_name(u'indicador02_organizacionong_cual_organizacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organizacionong', models.ForeignKey(orm[u'indicador02.organizacionong'], null=False)),
            ('onglocales', models.ForeignKey(orm[u'indicador02.onglocales'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organizacionong_id', 'onglocales_id'])


    def backwards(self, orm):
        # Deleting model 'OrgGremiales'
        db.delete_table(u'indicador02_orggremiales')

        # Deleting model 'BeneficiosObtenido'
        db.delete_table(u'indicador02_beneficiosobtenido')

        # Deleting model 'SerMiembro'
        db.delete_table(u'indicador02_sermiembro')

        # Deleting model 'OrganizacionGremial'
        db.delete_table(u'indicador02_organizaciongremial')

        # Removing M2M table for field socio on 'OrganizacionGremial'
        db.delete_table(db.shorten_name(u'indicador02_organizaciongremial_socio'))

        # Removing M2M table for field beneficio on 'OrganizacionGremial'
        db.delete_table(db.shorten_name(u'indicador02_organizaciongremial_beneficio'))

        # Removing M2M table for field miembro_junta on 'OrganizacionGremial'
        db.delete_table(db.shorten_name(u'indicador02_organizaciongremial_miembro_junta'))

        # Deleting model 'OrgComunitarias'
        db.delete_table(u'indicador02_orgcomunitarias')

        # Deleting model 'BeneficioOrgComunitaria'
        db.delete_table(u'indicador02_beneficioorgcomunitaria')

        # Deleting model 'NoOrganizado'
        db.delete_table(u'indicador02_noorganizado')

        # Deleting model 'OrganizacionComunitaria'
        db.delete_table(u'indicador02_organizacioncomunitaria')

        # Removing M2M table for field cual_organizacion on 'OrganizacionComunitaria'
        db.delete_table(db.shorten_name(u'indicador02_organizacioncomunitaria_cual_organizacion'))

        # Removing M2M table for field cual_beneficio on 'OrganizacionComunitaria'
        db.delete_table(db.shorten_name(u'indicador02_organizacioncomunitaria_cual_beneficio'))

        # Removing M2M table for field no_organizado on 'OrganizacionComunitaria'
        db.delete_table(db.shorten_name(u'indicador02_organizacioncomunitaria_no_organizado'))

        # Deleting model 'OngLocales'
        db.delete_table(u'indicador02_onglocales')

        # Deleting model 'OrganizacionOng'
        db.delete_table(u'indicador02_organizacionong')

        # Removing M2M table for field cuales on 'OrganizacionOng'
        db.delete_table(db.shorten_name(u'indicador02_organizacionong_cuales'))

        # Removing M2M table for field cual_organizacion on 'OrganizacionOng'
        db.delete_table(db.shorten_name(u'indicador02_organizacionong_cual_organizacion'))


    models = {
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
        u'configuracion.plataforma': {
            'Meta': {'object_name': 'Plataforma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'configuracion.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'configuracion.sitioaccion': {
            'Meta': {'object_name': 'SitioAccion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'indicador02.beneficioorgcomunitaria': {
            'Meta': {'object_name': 'BeneficioOrgComunitaria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador02.beneficiosobtenido': {
            'Meta': {'object_name': 'BeneficiosObtenido'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador02.noorganizado': {
            'Meta': {'object_name': 'NoOrganizado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador02.onglocales': {
            'Meta': {'object_name': 'OngLocales'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'indicador02.organizacioncomunitaria': {
            'Meta': {'object_name': 'OrganizacionComunitaria'},
            'cual_beneficio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador02.BeneficioOrgComunitaria']", 'symmetrical': 'False'}),
            'cual_organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador02.OrgComunitarias']", 'symmetrical': 'False'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_organizado': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador02.NoOrganizado']", 'symmetrical': 'False'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'pertence': ('django.db.models.fields.IntegerField', [], {})
        },
        u'indicador02.organizaciongremial': {
            'Meta': {'object_name': 'OrganizacionGremial'},
            'asumir_cargo': ('django.db.models.fields.IntegerField', [], {}),
            'beneficio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador02.BeneficiosObtenido']", 'symmetrical': 'False'}),
            'capacitacion': ('django.db.models.fields.IntegerField', [], {}),
            'desde_capacitacion': ('django.db.models.fields.IntegerField', [], {}),
            'desde_miembro': ('django.db.models.fields.IntegerField', [], {}),
            'desde_socio': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'miembro_gremial': ('django.db.models.fields.IntegerField', [], {}),
            'miembro_junta': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador02.SerMiembro']", 'symmetrical': 'False'}),
            'socio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['indicador02.OrgGremiales']", 'symmetrical': 'False'})
        },
        u'indicador02.organizacionong': {
            'Meta': {'object_name': 'OrganizacionOng'},
            'cual_organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'organizacion'", 'symmetrical': 'False', 'to': u"orm['indicador02.OngLocales']"}),
            'cuales': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'cuales'", 'symmetrical': 'False', 'to': u"orm['indicador02.OngLocales']"}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        u'indicador02.orgcomunitarias': {
            'Meta': {'object_name': 'OrgComunitarias'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador02.orggremiales': {
            'Meta': {'object_name': 'OrgGremiales'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'indicador02.sermiembro': {
            'Meta': {'object_name': 'SerMiembro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'lugar.comunidad': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Comunidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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
            'siglas': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'sitio_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['configuracion.SitioAccion']"}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'temas': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'mapeo.persona': {
            'Meta': {'object_name': 'Persona'},
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Comunidad']"}),
            'departamento': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Departamento']"}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'finca': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['lugar.Municipio']"}),
            'nivel_educacion': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'org'", 'symmetrical': 'False', 'to': u"orm['mapeo.Organizaciones']"}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lugar.Pais']"}),
            'sexo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'monitoreo.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jefe': ('django.db.models.fields.IntegerField', [], {}),
            'productor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mapeo.Persona']"}),
            'recolector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitoreo.Recolector']"}),
            'tipo_encuesta': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'monitoreo.recolector': {
            'Meta': {'object_name': 'Recolector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['indicador02']