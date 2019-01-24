# -*- coding: utf-8 -*-

from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .models import Person
from .forms import NominateForm, NominatorFormSet


class NomineeCreateView(CreateView):
    form_class = NominateForm
    template_name = 'peoples/nominate_form.html'
    model = Person

    def get_all_forms(self):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        nominee_form = NominatorFormSet()
        context = {
            'form': form,
            'nominee_form': nominee_form,
        }
        return context

    def get(self, request, *args, **kwargs):
        self.object = None
        forms = self.get_all_forms()
        return self.render_to_response(
            self.get_context_data(**forms)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()

        form = self.get_form(form_class)
        nominee_form = NominatorFormSet(request.POST)
        if (form.is_valid() and nominee_form.is_valid()):
            return self.form_valid(form, nominee_form)
        nominee_form.is_valid()
        return self.form_invalid(form, nominee_form)

    def form_valid(self, form, nominee_form):
        self.object = form.save()
        nominee_form.instance = self.object
        nominees = nominee_form.save()
        return HttpResponseRedirect('/nominate/thanks/')

    def form_invalid(self, form, nominee_form):
        return self.render_to_response(
            self.get_context_data(
                form=form, nominee_form=nominee_form, is_invalid=True
            )
        )

    def get_context_data(self, **kwargs):
        context = super(NomineeCreateView, self).get_context_data(**kwargs)
        return context
