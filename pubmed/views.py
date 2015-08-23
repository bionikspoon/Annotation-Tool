from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib import messages

from braces.views import LoginRequiredMixin, UserFormKwargsMixin

from .models import Entry
from .forms import EntryModelForm


class EntryMixin(object):
    model = Entry


# noinspection PyUnresolvedReferences
class EntryFormMixin(LoginRequiredMixin, UserFormKwargsMixin, EntryMixin):
    form_class = EntryModelForm
    template_name = 'pubmed/entry_form.html'

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super().form_valid(form)


class EntryListView(EntryMixin, ListView):
    template_name = 'pubmed/entry_list.html'


class EntryDetailView(EntryMixin, DetailView):
    template_name = 'pubmed/entry_detail.html'


class EntryCreateView(EntryFormMixin, CreateView):
    success_msg = 'Entry Created'


class EntryUpdateView(EntryFormMixin, UpdateView):
    success_msg = 'Entry Updated'
