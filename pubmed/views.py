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
from .models import Entry
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
    form_success_code = NotImplemented
    """HTTP statuse code sent on successful form submit. (200 or 201"""
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
        # response.status_code = self.form_success_code
        messages.info(self.request, self.success_msg)
        return response


class EntryListView(EntryMixin, braces_views.SelectRelatedMixin, ListView):
    """
    List pubmed entries.
    """
    template_name = 'pubmed/entry_list.html'
    select_related = ('structure', 'mutation_type')


class EntryDetailView(EntryMixin, DetailView):
    """
    Show single pubmed entry.
    """
    template_name = 'pubmed/entry_detail.html'


class EntryCreateView(EntryFormMixin, CreateView):
    """
    Form. Create an entry.
    """
    success_msg = 'Entry Created'
    action_text = 'Create'
    form_success_code = 201


class EntryUpdateView(EntryFormMixin, UpdateView):
    """
    Form.  Update an existing entry.
    """
    success_msg = 'Entry Updated'
    action_text = 'Update'
    form_success_code = 200


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
        return Response(data={
            'entry_list': queryset
        }, template_name='pubmed/_entry_list_items.html')
