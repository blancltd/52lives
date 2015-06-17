# -*- coding: utf-8 -*-

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView

from persons.forms import SupportForm

from .models import Live


class LivesListView(ListView):
    queryset = Live.objects.active()
    model = Live
    paginate_by = 1


class SupportLive(SingleObjectMixin, FormView):
    template_name = 'lives/live_detail.html'
    model = Live
    form_class = SupportForm
    success_message = 'Your form has been submitted successfully.'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(SupportLive, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        person = form.save(commit=False)
        person.live = self.object
        person.save()
        return super(SupportLive, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.object.get_absolute_url()


class LiveDisplay(DetailView):
    queryset = Live.objects.active()
    model = Live

    def get_context_data(self, **kwargs):
        context = super(LiveDisplay, self).get_context_data(**kwargs)
        context['form'] = SupportForm()
        return context


class LiveDetailView(View):

    def get(self, request, *args, **kwargs):
        view = LiveDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = SupportLive.as_view()
        return view(request, *args, **kwargs)

