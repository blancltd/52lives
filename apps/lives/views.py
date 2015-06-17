# -*- coding: utf-8 -*-

from django.contrib import messages
from django.views.generic import FormView
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView

from people.forms import SupportForm

from .models import Life


class LivesListView(ListView):
    queryset = Life.objects.active()
    model = Life
    paginate_by = 1


class SupportLife(SingleObjectMixin, FormView):
    template_name = 'lives/life_detail.html'
    model = Life
    form_class = SupportForm
    success_message = 'Your form has been submitted successfully.'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(SupportLife, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        person = form.save(commit=False)
        person.life = self.object
        person.save()
        return super(SupportLife, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.object.get_absolute_url()


class LifeDisplay(DetailView):
    queryset = Life.objects.active()
    model = Life

    def get_context_data(self, **kwargs):
        context = super(LifeDisplay, self).get_context_data(**kwargs)
        context['form'] = SupportForm()
        return context


class LifeDetailView(View):

    def get(self, request, *args, **kwargs):
        view = LifeDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = SupportLife.as_view()
        return view(request, *args, **kwargs)

