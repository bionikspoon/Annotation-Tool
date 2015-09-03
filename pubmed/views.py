# coding=utf-8
"""
Pubmed view definitions.
"""
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib import messages
from braces import views as braces_views
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

    def get_context_data(self, **kwargs) -> dict:
        """
        Add `action_text` to response context.

        :rtype : dict
        :param kwargs:
        :return: context
        """

        context = super().get_context_data(**kwargs)
        context['action_text'] = self.action_text
        return context

    def no_permissions_fail(self, request=None) -> HttpResponse:
        """
        Set response code to the proper 401.

        :param request:
        :return: response object
        :rtype: django.http.HttpResponse
        """

        response = super().no_permissions_fail(request)
        response.status_code = 401
        return response

    def form_valid(self, form) -> HttpResponse:
        """
        Set correct response code 200/201.  Inject flash message into
        response.

        :type form: pubmed.forms.forms.EntryModelForm
        :return: response object
        :rtype: django.http.HttpResponse
        """

        response = super().form_valid(form)
        response.status_code = self.form_success_code
        messages.info(self.request, self.success_msg)
        return response

    def form_invalid(self, form) -> HttpResponse:
        """
        Set correct response code for invalid form submission.

        :param form:
        :type form: pubmed.forms.forms.EntryModelForm
        :return: response object
        :rtype: django.http.HttpResponse
        """

        response = super().form_invalid(form)
        response.status_code = 304
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

    def html(self, request, *args, **kwargs) -> Response:
        """
            Get rendered HTML representation of pubmed entries.  (Filter by
            `pubmed_id`.)

            :param request:
            :param args:
            :param kwargs:
            :return:
            """
        queryset = self.filter_queryset(self.get_queryset())
        return Response(data={
            'entry_list': queryset
        }, template_name='pubmed/_entry_list_items.html')
