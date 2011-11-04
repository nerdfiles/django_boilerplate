# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PageTaggit'
        db.create_table('cms_taggit_pagetaggit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Page'], unique=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('cms_taggit', ['PageTaggit'])


    def backwards(self, orm):
        
        # Deleting model 'PageTaggit'
        db.delete_table('cms_taggit_pagetaggit')


    models = {
        'cms.page': {
            'Meta': {'ordering': "('site', 'tree_id', 'lft')", 'object_name': 'Page'},
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderator_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cms_taggit.pagetaggit': {
            'Meta': {'object_name': 'PageTaggit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['cms_taggit']
