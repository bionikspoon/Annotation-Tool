from rest_framework.filters import BaseFilterBackend


class IncludeOrExcludeIdFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        entry_id = request.query_params.get('id')
        """:type entry_id: str"""

        if not entry_id:
            return queryset

        if entry_id.startswith('-'):
            entry_id = entry_id.replace('-', '', 1)
            return queryset.exclude(id=entry_id)

        return queryset.filter(id=entry_id)
