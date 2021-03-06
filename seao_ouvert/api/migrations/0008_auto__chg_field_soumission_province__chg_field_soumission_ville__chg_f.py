# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Soumission.province'
        db.alter_column(u'api_soumission', 'province_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['api.Province']))

        # Changing field 'Soumission.ville'
        db.alter_column(u'api_soumission', 'ville', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Soumission.montant_soumis_unite'
        db.alter_column(u'api_soumission', 'montant_soumis_unite_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['api.UniteMontant']))

        # Changing field 'Soumission.code_postal'
        db.alter_column(u'api_soumission', 'code_postal', self.gf('django.db.models.fields.CharField')(max_length=7, null=True))

        # Changing field 'Soumission.pays'
        db.alter_column(u'api_soumission', 'pays_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['api.Pays']))

        # Changing field 'Soumission.montant_soumis'
        db.alter_column(u'api_soumission', 'montant_soumis', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2))

        # Changing field 'Soumission.adresse1'
        db.alter_column(u'api_soumission', 'adresse1', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Soumission.adresse2'
        db.alter_column(u'api_soumission', 'adresse2', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Soumission.montant_contrat'
        db.alter_column(u'api_soumission', 'montant_contrat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2))

        # Changing field 'Avis.province'
        db.alter_column(u'api_avis', 'province_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['api.Province']))

        # Changing field 'Avis.ville'
        db.alter_column(u'api_avis', 'ville', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Avis.code_postal'
        db.alter_column(u'api_avis', 'code_postal', self.gf('django.db.models.fields.CharField')(max_length=7, null=True))

        # Changing field 'Avis.nature'
        db.alter_column(u'api_avis', 'nature_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['api.Nature']))

        # Changing field 'Avis.pays'
        db.alter_column(u'api_avis', 'pays_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['api.Pays']))

        # Changing field 'Avis.date_saisie_adjudication'
        db.alter_column(u'api_avis', 'date_saisie_adjudication', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Avis.precision'
        db.alter_column(u'api_avis', 'precision', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Avis.orgamisme'
        db.alter_column(u'api_avis', 'orgamisme', self.gf('django.db.models.fields.CharField')(max_length=150, null=True))

        # Changing field 'Avis.date_publication'
        db.alter_column(u'api_avis', 'date_publication', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Avis.adresse1'
        db.alter_column(u'api_avis', 'adresse1', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Avis.date_fermeture'
        db.alter_column(u'api_avis', 'date_fermeture', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Avis.adresse2'
        db.alter_column(u'api_avis', 'adresse2', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

        # Changing field 'Avis.type'
        db.alter_column(u'api_avis', 'type_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['api.Type']))

        # Changing field 'Avis.date_adjudication'
        db.alter_column(u'api_avis', 'date_adjudication', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Soumission.province'
        raise RuntimeError("Cannot reverse this migration. 'Soumission.province' and its values cannot be restored.")

        # Changing field 'Soumission.ville'
        db.alter_column(u'api_soumission', 'ville', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # User chose to not deal with backwards NULL issues for 'Soumission.montant_soumis_unite'
        raise RuntimeError("Cannot reverse this migration. 'Soumission.montant_soumis_unite' and its values cannot be restored.")

        # Changing field 'Soumission.code_postal'
        db.alter_column(u'api_soumission', 'code_postal', self.gf('django.db.models.fields.CharField')(default='', max_length=7))

        # User chose to not deal with backwards NULL issues for 'Soumission.pays'
        raise RuntimeError("Cannot reverse this migration. 'Soumission.pays' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Soumission.montant_soumis'
        raise RuntimeError("Cannot reverse this migration. 'Soumission.montant_soumis' and its values cannot be restored.")

        # Changing field 'Soumission.adresse1'
        db.alter_column(u'api_soumission', 'adresse1', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # Changing field 'Soumission.adresse2'
        db.alter_column(u'api_soumission', 'adresse2', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # User chose to not deal with backwards NULL issues for 'Soumission.montant_contrat'
        raise RuntimeError("Cannot reverse this migration. 'Soumission.montant_contrat' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Avis.province'
        raise RuntimeError("Cannot reverse this migration. 'Avis.province' and its values cannot be restored.")

        # Changing field 'Avis.ville'
        db.alter_column(u'api_avis', 'ville', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Avis.code_postal'
        db.alter_column(u'api_avis', 'code_postal', self.gf('django.db.models.fields.CharField')(default='', max_length=7))

        # User chose to not deal with backwards NULL issues for 'Avis.nature'
        raise RuntimeError("Cannot reverse this migration. 'Avis.nature' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Avis.pays'
        raise RuntimeError("Cannot reverse this migration. 'Avis.pays' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Avis.date_saisie_adjudication'
        raise RuntimeError("Cannot reverse this migration. 'Avis.date_saisie_adjudication' and its values cannot be restored.")

        # Changing field 'Avis.precision'
        db.alter_column(u'api_avis', 'precision', self.gf('django.db.models.fields.CharField')(default='', max_length=150))

        # Changing field 'Avis.orgamisme'
        db.alter_column(u'api_avis', 'orgamisme', self.gf('django.db.models.fields.CharField')(default='', max_length=150))

        # User chose to not deal with backwards NULL issues for 'Avis.date_publication'
        raise RuntimeError("Cannot reverse this migration. 'Avis.date_publication' and its values cannot be restored.")

        # Changing field 'Avis.adresse1'
        db.alter_column(u'api_avis', 'adresse1', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # User chose to not deal with backwards NULL issues for 'Avis.date_fermeture'
        raise RuntimeError("Cannot reverse this migration. 'Avis.date_fermeture' and its values cannot be restored.")

        # Changing field 'Avis.adresse2'
        db.alter_column(u'api_avis', 'adresse2', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

        # User chose to not deal with backwards NULL issues for 'Avis.type'
        raise RuntimeError("Cannot reverse this migration. 'Avis.type' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Avis.date_adjudication'
        raise RuntimeError("Cannot reverse this migration. 'Avis.date_adjudication' and its values cannot be restored.")

    models = {
        u'api.avis': {
            'Meta': {'object_name': 'Avis'},
            'adresse1': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'adresse2': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'date_adjudication': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_fermeture': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_publication': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_saisie_adjudication': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'disposition_municipale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.DispositionMunicipale']"}),
            'disposition_non_municipale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.DispositionNonMunicipale']"}),
            'municipal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nature': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.Nature']"}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'numero_seao': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'orgamisme': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.Pays']"}),
            'precision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.Province']"}),
            'regions_livraison': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['api.Region']"}),
            'titre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'avis'", 'null': 'True', 'to': u"orm['api.Type']"}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        u'api.dispositionmunicipale': {
            'Meta': {'object_name': 'DispositionMunicipale'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.dispositionnonmunicipale': {
            'Meta': {'object_name': 'DispositionNonMunicipale'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.nature': {
            'Meta': {'object_name': 'Nature'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.pays': {
            'Meta': {'object_name': 'Pays'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.province': {
            'Meta': {'object_name': 'Province'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.region': {
            'Meta': {'object_name': 'Region'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.soumission': {
            'Meta': {'object_name': 'Soumission'},
            'adjudicataire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admissible': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'adresse1': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'adresse2': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'appel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'soumissions'", 'to': u"orm['api.Avis']"}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'conforme': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'montant_contrat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'montant_soumis': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'montant_soumis_unite': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'soumissions'", 'null': 'True', 'to': u"orm['api.UniteMontant']"}),
            'nom_organisation': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'soumissions'", 'null': 'True', 'to': u"orm['api.Pays']"}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'soumissions'", 'null': 'True', 'to': u"orm['api.Province']"}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        u'api.type': {
            'Meta': {'object_name': 'Type'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.unitemontant': {
            'Meta': {'object_name': 'UniteMontant'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'api.unspsc': {
            'Meta': {'object_name': 'UNSPSC'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['api']