# coding=utf-8
"""
Pubmed view definitions.
"""
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib import messages
from braces import views as braces_views
from rest_framework.decorators import list_route
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .forms import EntryModelForm
from .models import Entry, EntryMeta
from .serializers import EntrySerializer


class EntryMixin(object):
    """
    Define model.
    """
    model = Entry


class EntryFormMixin(braces_views.LoginRequiredMixin,
                     braces_views.UserFormKwargsMixin, EntryMixin):
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


class EntryListView(EntryMixin, braces_views.SelectRelatedMixin, ListView):
    """
    List pubmed entries.
    """
    select_related = ('structure', 'mutation_type')


class EntryDetailView(EntryMixin, braces_views.SelectRelatedMixin, DetailView):
    """
    Show single pubmed entry.
    """
    select_related = EntryMeta.foreign_fields
    prefetch_related = EntryMeta.relationship_fields


class EntryCreateView(EntryFormMixin,

                      # braces_views.PrefetchRelatedMixin,
                      CreateView):
    """
    Form. Create an entry.
    """

    prefetch_related = (
        'assessed_patient_outcomes', 'significant_patient_outcomes')
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
    serializer_class = EntrySerializer
    filter_fields = ('pubmed_id',)

    # noinspection PyUnusedLocal
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

        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(page)
        return Response({
            'entry_list': page
        }, template_name='pubmed/_entry_list_items.html')
