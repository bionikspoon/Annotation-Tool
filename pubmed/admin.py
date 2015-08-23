from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Entry, EntryAdmin)
