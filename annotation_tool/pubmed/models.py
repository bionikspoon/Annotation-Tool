from django.db import models


class Pubmed(models.Model):
    pubmed_id = models.PositiveIntegerField(db_index=True)
    gene = models.CharField(max_length=128, blank=True)
    chromosome = models.CharField(max_length=128, blank=True)
