from django.contrib import admin

from .models import EntryMeta


@admin.register(EntryMeta.model)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('pubmed', 'show_url',) + EntryMeta.summary_fields

    readonly_fields = ('show_url', 'created', 'modified')
    filter_horizontal = EntryMeta.many_to_many_fields

    list_filter = tuple((field, admin.RelatedOnlyFieldListFilter) for field in
                        EntryMeta.relationship_fields)
    radio_fields = {field: admin.HORIZONTAL for field in
                    EntryMeta.foreign_fields + ('variant_clinical_grade',)}

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
