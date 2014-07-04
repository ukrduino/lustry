# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lustra'
        db.create_table('lustra', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('product_slug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('product_text', self.gf('django.db.models.fields.TextField')()),
            ('product_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('product_date_change', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('product_likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('product_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, default='')),
            ('product_sold', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('product_start_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('product_current_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('product_present', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('product_order', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('product_lusta_h', self.gf('django.db.models.fields.IntegerField')()),
            ('product_lusta_w', self.gf('django.db.models.fields.IntegerField')()),
            ('product_lusta_patr', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('product_lusta_lamps', self.gf('django.db.models.fields.IntegerField')()),
            ('product_lusta_l_power', self.gf('django.db.models.fields.IntegerField')()),
            ('product_lusta_arm_col', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('product_lusta_arm_mat', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('product_lusta_plaf_col', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('product_lusta_plaf_mat', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('product_lusta_prod', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('product_lusta_country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('product_lusta_compl', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('shop', ['Lustra'])

        # Adding model 'Comment'
        db.create_table('comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment_text', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('comment_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comment_product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Lustra'])),
        ))
        db.send_create_signal('shop', ['Comment'])

        # Adding model 'Order'
        db.create_table('order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_person', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('order_person_phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('order_person_address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('order_person_email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('order_pay_option', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('order_delivery_option', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('order_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('order_delivered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order_products', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('order_code', self.gf('django.db.models.fields.CharField')(max_length=4, default=3252)),
            ('order_password', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('order_summ', self.gf('django.db.models.fields.IntegerField')(max_length=4, default=0)),
        ))
        db.send_create_signal('shop', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Lustra'
        db.delete_table('lustra')

        # Deleting model 'Comment'
        db.delete_table('comment')

        # Deleting model 'Order'
        db.delete_table('order')


    models = {
        'shop.comment': {
            'Meta': {'db_table': "'comment'", 'object_name': 'Comment'},
            'comment_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'comment_product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Lustra']"}),
            'comment_text': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shop.lustra': {
            'Meta': {'db_table': "'lustra'", 'object_name': 'Lustra'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_current_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product_date': ('django.db.models.fields.DateTimeField', [], {}),
            'product_date_change': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "''"}),
            'product_likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product_lusta_arm_col': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product_lusta_arm_mat': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product_lusta_compl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'product_lusta_country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product_lusta_h': ('django.db.models.fields.IntegerField', [], {}),
            'product_lusta_l_power': ('django.db.models.fields.IntegerField', [], {}),
            'product_lusta_lamps': ('django.db.models.fields.IntegerField', [], {}),
            'product_lusta_patr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'product_lusta_plaf_col': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product_lusta_plaf_mat': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product_lusta_prod': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product_lusta_w': ('django.db.models.fields.IntegerField', [], {}),
            'product_order': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'product_present': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'product_slug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'product_sold': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product_start_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product_text': ('django.db.models.fields.TextField', [], {}),
            'product_title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'shop.order': {
            'Meta': {'db_table': "'order'", 'object_name': 'Order'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'default': '3252'}),
            'order_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'order_delivered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order_delivery_option': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order_password': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'order_pay_option': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order_person': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order_person_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order_person_email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'order_person_phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order_products': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'order_summ': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'default': '0'})
        }
    }

    complete_apps = ['shop']