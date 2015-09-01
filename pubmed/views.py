# coding=utf-8
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
    model = Entry


class EntryFormMixin(braces_views.LoginRequiredMixin,
                     braces_views.UserFormKwargsMixin, EntryMixin):
    form_class = EntryModelForm
    template_name = 'pubmed/entry_form.html'
    success_url = reverse_lazy('pubmed:list')

    @property
    def success_msg(self):
        return NotImplemented

    @property
    def action_text(self):
        return NotImplemented

    # noinspection PyUnresolvedReferences
    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super().form_valid(form)

    # noinspection PyUnresolvedReferences
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_text'] = self.action_text
        return context


class EntryListView(EntryMixin, braces_views.SelectRelatedMixin, ListView):
    template_name = 'pubmed/entry_list.html'
    select_related = ('structure', 'mutation_type')


class EntryDetailView(EntryMixin, DetailView):
    template_name = 'pubmed/entry_detail.html'


class EntryCreateView(EntryFormMixin, CreateView):
    success_msg = 'Entry Created'
    action_text = 'Create'


class EntryUpdateView(EntryFormMixin, UpdateView):
    success_msg = 'Entry Updated'
    action_text = 'Update'


class EntryViewSet(ReadOnlyModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = ('pubmed_id',)

    @list_route(renderer_classes=(TemplateHTMLRenderer,))
    def html(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        return Response(data={
            'entry_list': queryset
        }, template_name='pubmed/_entry_list_items.html')
