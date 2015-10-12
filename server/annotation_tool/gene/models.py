from django.contrib.postgres import fields as postgres
from django.db import models

from ..utils.models import LookupTable


class Gene(models.Model):
    uuid = models.UUIDField(primary_key=True)
    version = models.BigIntegerField()
    hgnc_id = models.CharField(max_length=128, unique=True, db_index=True)
    ccds_id = postgres.ArrayField(models.CharField(max_length=128), null=True)
    cosmic = models.CharField(max_length=128)
    date_modified = models.DateTimeField(null=True)
    date_approved_reserved = models.DateTimeField(null=True)
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=128, db_index=True)
    alias_name = postgres.ArrayField(models.CharField(max_length=128), null=True)  # 2
    alias_symbol = postgres.ArrayField(models.CharField(max_length=128), null=True)  # 2
    location = models.CharField(max_length=128)
    location_sortable = models.CharField(max_length=128)
    locus_type = models.CharField(max_length=128)
    locus_group = models.CharField(max_length=128)
    gene_family = postgres.ArrayField(models.CharField(max_length=128, null=True), default=[])
    gene_family_id = postgres.ArrayField(models.BigIntegerField(null=True), default=[])

    status = models.CharField(max_length=128)
    entrez_id = models.BigIntegerField(null=True)
    ensembl_gene_id = models.CharField(max_length=128)
    refseq_accession = postgres.ArrayField(models.CharField(max_length=128), null=True)

    ena = postgres.ArrayField(models.CharField(max_length=128), null=True)
    pubmed_id = postgres.ArrayField(models.BigIntegerField(), null=True)
    rgd_id = postgres.ArrayField(models.CharField(max_length=128), null=True)
    snornabase = models.CharField(max_length=128, null=True)
    ucsc_id = models.CharField(max_length=128, null=True)
    uniprot_ids = postgres.ArrayField(models.CharField(max_length=128), null=True)
    vega_id = models.CharField(max_length=128, null=True)
    mgd_id = postgres.ArrayField(models.CharField(max_length=128), null=True)
    omim_id = postgres.ArrayField(models.BigIntegerField(), null=True)
    enzyme_id = postgres.ArrayField(models.CharField(max_length=128), null=True)
    homeodb = models.BigIntegerField(null=True)
    horde_id = models.CharField(max_length=128, null=True)
    lsdb = postgres.ArrayField(models.CharField(max_length=128), null=True)
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
    prev_name = postgres.ArrayField(models.CharField(max_length=128), null=True)
    prev_symbol = postgres.ArrayField(models.CharField(max_length=128), null=True)

    def __repr__(self):
        return '<Gene: %s>' % self.symbol

    class CcdsIdLookup(LookupTable):
        pass

    class AliasNameLookup(LookupTable):
        pass

    class AliasSymbolLookup(LookupTable):
        pass

    class GeneFamilyLookup(LookupTable):
        pass

    class GeneFamilyIdLookup(LookupTable):
        pass

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

    class LsdbLookup(LookupTable):
        pass

    class PrevNameLookup(LookupTable):
        pass

    class PrevSymbolLookup(LookupTable):
        pass
