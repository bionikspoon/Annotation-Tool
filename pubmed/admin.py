from django.contrib import admin

from .models import Entry, LookupTable

lookup_tables = (lookup_table for lookup_table in LookupTable.__subclasses__())

FOREIGN_FIELDS = (
    'user', 'structure', 'mutation_type', 'syntax', 'operator', 'rule_level',
    'breakend_strand', 'breakend_direction', 'mate_breakend_strand',
    'mate_breakend_direction', 'variant_type', 'variant_consequence', 'sex',)

MANY_FIELDS = (
    'disease', 'assessed_patient_outcomes', 'significant_patient_outcomes',)

TEXT_FIELDS = (

    'gene', 'syntax_text', 'chromosome', 'mate_chromosome',
    'coordinate_predicate', 'partner_coordinate_predicate', 'treatment_1',
    'treatment_2', 'treatment_3', 'treatment_4', 'treatment_5', 'ethnicity',
    'design', 'reference_claims', 'comments',)

INT_FIELDS = ('pubmed_id', 'start', 'stop', 'mate_start', 'mate_end',
              'minimum_number_of_copies', 'maximum_number_of_copies',
              'variant_clinical_grade', 'population_size',)


@admin.register(*lookup_tables)
class LookupTableAdmin(admin.ModelAdmin):
    fields = ('choice',)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'pubmed', 'show_url', 'user', 'modified', 'gene', 'structure',
        'mutation_type', 'syntax', 'syntax_text', 'operator', 'rule_level',
        'variant_type', 'variant_consequence', 'variant_clinical_grade',)
    readonly_fields = ('show_url', 'created', 'modified')
    filter_horizontal = MANY_FIELDS
    list_filter = [(field, admin.RelatedOnlyFieldListFilter) for field in
                   FOREIGN_FIELDS + MANY_FIELDS]
    radio_fields = {field: admin.HORIZONTAL for field in
                    FOREIGN_FIELDS + ('variant_clinical_grade',)}

    list_select_related = True
    search_fields = ('pubmed_id',)

    def pubmed(self, obj):
        return str(obj)

    pubmed.short_description = "Pubmed Id"
    pubmed.admin_order_field = 'pubmed_id'

    def show_url(self, obj):
        if obj.pk:
            template = """<a href="{0}">{0}</a>"""
            url = obj.get_absolute_url()
            return template.format(url)

    show_url.short_description = "See Entry"
    show_url.allow_tags = True
    show_url.admin_order_field = 'id'

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
