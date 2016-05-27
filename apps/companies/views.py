# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Company, Life


class CompanyListView(ListView):
    model = Company
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        return context


class CompanyDetailView(DetailView):
    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        return context


class CompanyLifeDetailView(DetailView):
    model = Life

    def get_object(self, queryset=None):
        # # Next, try looking up by primary key.
        company_slug = self.kwargs.get('slug', None)
        life_number = self.kwargs.get('life_number', None)

        try:
            company = Company.objects.get(slug=company_slug)
        except Company.DoesNotExist:
            raise Http404("No company found matching the query")
        else:
            try:
                obj = company.life_set.get(number=life_number)
            except Life.DoesNotExist:
                raise Http404("No life for given company was found")

        return obj

    def get_context_data(self, **kwargs):
        context = super(CompanyLifeDetailView, self).get_context_data(**kwargs)
        return context
