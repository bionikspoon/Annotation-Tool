from django.views.generic import ListView, DetailView, CreateView, UpdateView

from braces.views import LoginRequiredMixin

from .models import Entry


class EntryMixin(object):
    model = Entry


class EntryFormMixin(LoginRequiredMixin, EntryMixin):
    template_name = 'pubmed/entry_form.html'
    fields = '__all__'


class EntryListView(EntryMixin, ListView):
    template_name = 'pubmed/entry_list.html'


class EntryDetailView(EntryMixin, DetailView):
    template_name = 'pubmed/entry_detail.html'


class EntryCreateView(EntryFormMixin, CreateView):
    pass


class EntryUpdateView(EntryFormMixin, UpdateView):
    pass
