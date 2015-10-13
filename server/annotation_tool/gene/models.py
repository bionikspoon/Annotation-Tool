import ipdb
from django.contrib.postgres import fields as postgres
from django.db import models
from django.db.models import Lookup

from ..utils.models import LookupTable, LookupMixin

RELATED_GENE = 'gene_set'


class CcdsIdLookup(LookupTable):
    pass


class AliasNameLookup(LookupTable):
    pass


class AliasSymbolLookup(LookupTable):
    pass


class GeneFamilyLookup(LookupTable):
    pass


class GeneFamilyIdLookup(LookupMixin, models.Model):
    choice = models.PositiveIntegerField(unique=True, db_index=True)


class RefseqAccessionLookup(LookupTable):
    pass


class EnaLookup(LookupTable):
    pass


class PubmedIdLookup(LookupTable):
    pass


class RgdIdLookup(LookupTable):
    pass


class UniprotIdsLookup(LookupTable):
    pass


class MgdIdLookup(LookupTable):
    pass


class OmimIdLookup(LookupTable):
    pass


class EnzymeIdLookup(LookupTable):
    pass


class LsdbLookup(LookupMixin, models.Model):
    choice = models.CharField(max_length=512, unique=True, db_index=True)


class PrevNameLookup(LookupMixin, models.Model):
    choice = models.CharField(max_length=256, unique=True, db_index=True)


class PrevSymbolLookup(LookupTable):
    pass


class Gene(models.Model):
    uuid = models.UUIDField(primary_key=True)
    version = models.BigIntegerField()
    hgnc_id = models.CharField(max_length=128, unique=True, db_index=True)
    ccds_id = models.ManyToManyField(CcdsIdLookup, blank=True)
    cosmic = models.CharField(max_length=128)
    date_modified = models.DateTimeField(null=True)
    date_approved_reserved = models.DateTimeField(null=True)
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=128, db_index=True)
    alias_name = models.ManyToManyField(AliasNameLookup, blank=True)
    alias_symbol = models.ManyToManyField(AliasSymbolLookup, blank=True)
    location = models.CharField(max_length=128)
    location_sortable = models.CharField(max_length=128)
    locus_type = models.CharField(max_length=128)
    locus_group = models.CharField(max_length=128)
    gene_family = models.ManyToManyField(GeneFamilyLookup, blank=True)
    gene_family_id = models.ManyToManyField(GeneFamilyIdLookup, blank=True)

    status = models.CharField(max_length=128)
    entrez_id = models.BigIntegerField(null=True)
    ensembl_gene_id = models.CharField(max_length=128)
    refseq_accession = models.ManyToManyField(RefseqAccessionLookup, blank=True)

    ena = models.ManyToManyField(EnaLookup, blank=True)
    pubmed_id = models.ManyToManyField(PubmedIdLookup, blank=True)
    rgd_id = models.ManyToManyField(RgdIdLookup, blank=True)
    snornabase = models.CharField(max_length=128, null=True)
    ucsc_id = models.CharField(max_length=128, null=True)
    uniprot_ids = models.ManyToManyField(UniprotIdsLookup, blank=True)
    vega_id = models.CharField(max_length=128, null=True)
    mgd_id = models.ManyToManyField(MgdIdLookup, blank=True)
    omim_id = models.ManyToManyField(OmimIdLookup, blank=True)
    enzyme_id = models.ManyToManyField(EnzymeIdLookup, blank=True)
    homeodb = models.BigIntegerField(null=True)
    horde_id = models.CharField(max_length=128, null=True)
    lsdb = models.ManyToManyField(LsdbLookup, blank=True)
    kznf_gene_catalog = models.BigIntegerField(null=True)
    lncrnadb = models.CharField(max_length=32, null=True)
    bioparadigms_slc = models.CharField(max_length=128, null=True)
    cd = models.CharField(max_length=128, null=True)
    date_name_changed = models.DateTimeField(null=True)
    date_symbol_changed = models.DateTimeField(null=True)
    imgt = models.CharField(max_length=128, null=True)
    intermediate_filament_db = models.CharField(max_length=128, null=True)
    iuphar = models.CharField(max_length=128, null=True)
    merops = models.CharField(max_length=128, null=True)
    mirbase = models.CharField(max_length=128, null=True)
    orphanet = models.CharField(max_length=128, null=True)
    prev_name = models.ManyToManyField(PrevNameLookup, blank=True)
    prev_symbol = models.ManyToManyField(PrevSymbolLookup, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        ipdb.set_trace()
        super().save(force_insert, force_update, using, update_fields)

    def __repr__(self):
        return '<Gene: %s>' % self.symbol
