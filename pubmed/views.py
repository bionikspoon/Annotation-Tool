# coding=utf-8
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib import messages
from braces.views import (LoginRequiredMixin, UserFormKwargsMixin,
    SelectRelatedMixin)
from rest_framework.viewsets import ModelViewSet

from .forms import EntryModelForm
from .models import (Entry, StructureLookup, MutationTypeLookup, SyntaxLookup,
    OperatorLookup, RuleLevelLookup, BreakendStrandLookup,
    BreakendDirectionLookup, VariantTypeLookup, VariantConsequenceLookup,
    SexLookup, DiseaseLookup, PatientOutcomesLookup)
from .serializers import (EntrySerializer, StructureLookupSerializer,
    MutationTypeLookupSerializer, SyntaxLookupSerializer,
    OperatorLookupSerializer, RuleLevelLookupSerializer,
    BreakendStrandLookupSerializer, BreakendDirectionLookupSerializer,
    VariantTypeLookupSerializer, VariantConsequenceLookupSerializer,
    SexLookupSerializer, DiseaseLookupSerializer,
    PatientOutcomesLookupSerializer)


class EntryMixin(object):
    model = Entry


class EntryFormMixin(LoginRequiredMixin, UserFormKwargsMixin, EntryMixin):
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


class EntryListView(EntryMixin, SelectRelatedMixin, ListView):
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


class EntryViewSet(ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class LookupTableViewSet(ModelViewSet):
    pass


class StructureLookupViewSet(LookupTableViewSet):
    queryset = StructureLookup.objects.all()
    serializer_class = StructureLookupSerializer


class MutationTypeLookupViewSet(LookupTableViewSet):
    queryset = MutationTypeLookup.objects.all()
    serializer_class = MutationTypeLookupSerializer


class SyntaxLookupViewSet(LookupTableViewSet):
    queryset = SyntaxLookup.objects.all()
    serializer_class = SyntaxLookupSerializer


class OperatorLookupViewSet(LookupTableViewSet):
    queryset = OperatorLookup.objects.all()
    serializer_class = OperatorLookupSerializer


class RuleLevelLookupViewSet(LookupTableViewSet):
    queryset = RuleLevelLookup.objects.all()
    serializer_class = RuleLevelLookupSerializer


class BreakendStrandLookupViewSet(LookupTableViewSet):
    queryset = BreakendStrandLookup.objects.all()
    serializer_class = BreakendStrandLookupSerializer


class BreakendDirectionLookupViewSet(LookupTableViewSet):
    queryset = BreakendDirectionLookup.objects.all()
    serializer_class = BreakendDirectionLookupSerializer


class VariantTypeLookupViewSet(LookupTableViewSet):
    queryset = VariantTypeLookup.objects.all()
    serializer_class = VariantTypeLookupSerializer


class VariantConsequenceLookupViewSet(LookupTableViewSet):
    queryset = VariantConsequenceLookup.objects.all()
    serializer_class = VariantConsequenceLookupSerializer


class SexLookupViewSet(LookupTableViewSet):
    queryset = SexLookup.objects.all()
    serializer_class = SexLookupSerializer


class DiseaseLookupViewSet(LookupTableViewSet):
    queryset = DiseaseLookup.objects.all()
    serializer_class = DiseaseLookupSerializer


class PatientOutcomesLookupViewSet(LookupTableViewSet):
    queryset = PatientOutcomesLookup.objects.all()
    serializer_class = PatientOutcomesLookupSerializer
