"""
Pubmed view definitions.
"""

# Django Packages
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

# Third Party Packages
from braces.views import LoginRequiredMixin, SelectRelatedMixin, UserFormKwargsMixin
from rest_framework.decorators import list_route
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

# Local Application
from .forms import EntryModelForm
from .models import Entry, EntryMeta
from .serializers import EntryListSerializer, EntryDetailSerializer


class EntryMixin(object):
    """
    Define model.
    """
    model = Entry


class EntryFormMixin(LoginRequiredMixin, UserFormKwargsMixin, EntryMixin):
    """
    Common form configuration.
    """
    form_class = EntryModelForm
    template_name = 'pubmed/entry_form.html'
    success_url = reverse_lazy('pubmed:list')
    success_msg = NotImplemented
    """Flash message sent on successful form submit."""
    action_text = NotImplemented
    """(Update/Create) Descriptive text used for buttons and headers."""

    def get_context_data(self, **kwargs):
        """
        Add `action_text` to response context.

        :param kwargs:
        :return: context
        :rtype : dict
        """

        # noinspection PyUnresolvedReferences
        context = super().get_context_data(**kwargs)
        context['action_text'] = self.action_text
        return context

    def form_valid(self, form):
        """
        Set correct response code 200/201.  Inject flash message into
        response.

        :type self: django.views.generic.base.View | self
        :type form: pubmed.forms.forms.EntryModelForm
        :param form:
        :return: response object
        :rtype: django.http.response.HttpResponse
        """

        # noinspection PyUnresolvedReferences
        response = super().form_valid(form)
        messages.info(self.request, self.success_msg)
        return response


class EntryListView(EntryMixin, SelectRelatedMixin, ListView):
    """
    List pubmed entries.
    """
    select_related = ('structure', 'mutation_type')


class EntryDetailView(EntryMixin, SelectRelatedMixin, DetailView):
    """
    Show single pubmed entry.
    """
    select_related = EntryMeta.foreign_fields


class EntryCreateView(EntryFormMixin, CreateView):
    """
    Form. Create an entry.
    """
    success_msg = 'Entry Created'
    action_text = 'Create'


class EntryUpdateView(EntryFormMixin, UpdateView):
    """
    Form.  Update an existing entry.
    """
    success_msg = 'Entry Updated'
    action_text = 'Update'


class EntryViewSet(ReadOnlyModelViewSet):
    """
    Pubmed entry api.
    """

    queryset = Entry.objects.all()

    filter_fields = ('pubmed_id',)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset_map = {
            'list': lambda query: query.prefetch_related(*EntryMeta.many_to_many_fields),
            'html': lambda query: query.prefetch_related(*EntryMeta.many_to_many_fields),
            'retrieve': lambda query: query.select_related(*EntryMeta.foreign_fields)
        }
        return queryset_map[self.action](queryset)

    def get_serializer_class(self):
        serial_map = {
            'list': EntryListSerializer,
            'retrieve': EntryDetailSerializer
        }
        return serial_map[self.action]

    @list_route(renderer_classes=(TemplateHTMLRenderer,))
    def html(self, request, *args, **kwargs):
        """
        Get rendered HTML representation of pubmed entries.
        (Filter by `pubmed_id`.)

        :param request:
        :param args:
        :param kwargs:
        :return:
        :rtype : rest_framework.response.Response
        """
        queryset = self.filter_queryset(self.get_queryset())

        exclude = request.query_params.get('exclude__entry')
        if exclude:
            queryset = queryset.exclude(id=exclude)

        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(page)
        return Response(

            {
                'entry_list': queryset
            },

            headers={
                'count': queryset.count()
            },

            template_name='pubmed/_entry_list_items.html'

        )
